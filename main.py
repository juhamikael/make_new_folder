import os
import shutil

inpt = input("path:")  # Folder to "go through"
# inpt = "D:/53 September 2021"
path = inpt

file_types = {
    # File types which are used in for loop in line 51-72
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
    # Make new "folder here"
    "Misc": []
}
folder_names = tuple([key for key in file_types.keys()])
file_map = {}
for new_key in folder_names:
    file_map[new_key] = []

file_or_folder_map = {
    "Files": [],
    "Folders": []
}

listdir = os.listdir(path)
for item in listdir:
    if os.path.isfile(f"{path}/{item}"):
        file_or_folder_map["Files"].append(item)
    elif os.path.isdir(f"{path}/{item}"):
        file_or_folder_map["Folders"].append(item)

for item in listdir:
    if os.path.isfile(f"{path}/{item}"):
        file_or_folder_map["Files"].append(item)
    elif os.path.isdir(f"{path}/{item}"):
        file_or_folder_map["Folders"].append(item)

for file in file_or_folder_map["Files"]:
    for folder in folder_names:
        if file.endswith(tuple(file_types[f'{folder}'])):
            file_map[f"{folder}"].append(file)
        else:
            file_map["Misc"].append(file)

for folder_name in folder_names:
    files_for_folder = file_map[folder_name]
    has_files = len(files_for_folder) > 0
    if has_files:
        path_ext = os.path.join(path, folder_name)
        try:
            os.makedirs(path_ext, exist_ok=True)
        except Exception as exc:
            pass
            print(exc)
            print("Folder already exists, skipping folder creation")
    for file in files_for_folder:
        path_for_folder = os.path.join(path, folder_name)
        path_for_file = os.path.join(path, file)
        try:
            shutil.move(path_for_file, path_for_folder)
        except Exception as exc:
            pass
            # print(exc)
            # print(file, " already exists in the folder")
