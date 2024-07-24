# Facial Recognition to Discord Channel

This is a small project that sends a picture to a discord channel using a discord bot, if the webcam detects a unknown face.
Script made using `Python` with the libs `face_recognition`, `dlib`, `cv2` and `discord`.

The object of this is to catch curious people that try to sneak in your stuff.

<br/>

## Requirements ?

> - **[Python](https://www.python.org)**
> - **[PIP](https://pip.pypa.io/en/stable/installation/)**
> - **[DLIB - Download Link](https://github.com/Murtaza-Saeed/dlib)**
> - **[DLIB - Full instalation guide](https://www.youtube.com/watch?v=9zeb902f98s)**
> - **A discord BOT Token**
> - **A discord channel ID**
> - **Internet Connection** (To connect to your discord app)
> - **A webcam**

<br/>

## How to run it

> 1) Download this `.py` file.
>
> 2) This script utilizes the following libraries:
>    - face_recognition
>    - cv2
>    - discord
>
> - To install them, use the following commands:
>
>   ```
> 	pip install face_recognition
>   pip install opencv-python
>   pip install discord.py
>   ```
>   
> 3) Change the following on the code on lines 29, 30 and 59:
>    - `TOKEN` - Paste your discord bot token here
>    - `CHANNEL_ID` - Paste the channel ID you want to send the images here
>    - `image_paths` - Paste a list of paths to the images of KNOWN faces
>
> 4) Wait for the webcam capture window to open.
> 5) Any face that appears in front of camera that is not on the KNOW faces list provided, the script will take a snapshot and send to the channel selected

<br/>
