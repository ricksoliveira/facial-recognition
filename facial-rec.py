import face_recognition
import cv2
import discord
from datetime import datetime

def load_known_faces(image_paths):
    known_face_encodings = []
    known_face_names = []

    for image_path in image_paths:
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(image_path.split('/')[-2])  # Folder name as the persons name

    return known_face_encodings, known_face_names

def unlock_action():

    access_date = str(datetime.now())
    msg = "Unauthorized Access at: " + access_date # You cen set a custom message to go along the image here

    ret, frame = video_capture.read()
    image_path = 'captured_image.jpg'
    
    if ret:
        cv2.imwrite(image_path, frame)

    TOKEN = 'token' # Your discord Bot TOKEN
    CHANNEL_ID = 12345 # ID of the Discord Channel you wish for the image to be sent

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

        channel = client.get_channel(CHANNEL_ID)

        if channel:
            with open(image_path, 'rb') as f:
                await channel.send(content = msg, file=discord.File(f, filename='captured_image.jpg'))

            print('Image sent successfully!')

        else:
            print('Channel not found.')

        await client.close()

    client.run(TOKEN)

action_unlocked = False

video_capture = cv2.VideoCapture(0)
image_paths = [] # List of paths to the known images
known_face_encodings, known_face_names = load_known_faces(image_paths)

while True:

    # Capture frame-by-frame and find faces in current frame
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    current_face_recognized = False

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        if True in matches:

            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            current_face_recognized = True

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, "Unauthorized", (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

        if current_face_recognized:
            action_unlocked = False  

        if not current_face_recognized and not action_unlocked:
            unlock_action()
            action_unlocked = True # Flag to prevent action to be repeated

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()