# How it works?


This script check files ending (ex. random_photo **.jpg** ) in a folder and moves files into seperate folders.

### Lets say that you have lot of differrent jpg, png, zip, mp3, wav and pdf files

This script makes folder named:
- "Images" and moves all files which end with **.jpg** and **.png** inside 
- "Packed Files" and moves all files which end with **.zip** inside
- "Audio" and moves all files which end with **.wav** and **.mp3** inside
- "PDF" and moves all files which end with **.pdf** inside

You can edit main.py and the code below to decide what Folder names you want to have and which files goes inside what!

```     
    "Documents": ["docx", "odt", "rtf", "txt", "ods", "pptx", "dotx", "doc", "ppt"],
    "Images": ["jpg", "png", "jpeg", "ico", "jfif"],
    "Audio": ["mp3", "wav", "aac", "ogg", "aif", "m4a"],
    "Installers": ["exe", "msi"],
    "Packed Files": ["zip", "rar", "gz", "7z"],
    "Music Production": ["flp", "fst", "als"],
    "Midi": ["midi", "mid"],
    "Video": ["mp4", "gif", "mpeg", "mkv"],
    "Excel": ["xlsx", "csv", "xlsm", "xls"],
    "Sound Banks & Presets": ["fxp", "nmsv", "spf", "fxb"],
    "Photoshop": ["psd"],
    "Torrent": ["torrent"],
    "PDF": ["pdf"],    
```


# You need python3 installed on your device (NOTICE!! TESTED ONLY IN WIN10 MACHINE!)

## Check the link below if you dont have it installed yet:
[Python 3 Installation & Setup Guide](https://realpython.com/installing-python/#step-2-install-the-python-app)

## Download this script and run the script
DL with Git Clone or Zipped file
1. Open CMD
2. cd to directory you
3. type `python main.py`
4. Enter your directory, which you want to rearrange. ex. `E:\2021\Projects`

5. [Watch this if you dont know how run this](https://www.youtube.com/watch?v=Qi28uPKaH_A)
