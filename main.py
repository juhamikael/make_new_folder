import os
import shutil


# inpt = input("path:")  # Folder to "go through"
inpt = "D:/53 September 2021"
path = inpt


# def check_ending(dir_names, files_dict ):
#     dirs = dir_names


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
folder_names = (
    # Folder names to match 'file_types'
    "Documents",
    "Images",
    "Audio",
    "Installers",
    "Packed Files",
    "Music Production",
    "Midi",
    "Video",
    "Excel",
    "Sound Banks & Presets",
    "Photoshop",
    "Torrent",
    # Make new "folder here
    "PDF",
    "Misc"
)
print(type(folder_names))
file_map = {

    "Documents": [],
    "Images": [],
    "Audio": [],
    "Installers": [],
    "Packed Files": [],
    "Music Production": [],
    "Midi": [],
    "Video": [],
    "Excel": [],
    "Sound Banks & Presets": [],
    "Photoshop": [],
    "Torrent": [],
    # Make new "folder here"
    "PDF": [],
    "Misc": []
}
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
    # Checking files in the path folder
    # If file ends with .pdf, .docx, .rtf etc, adding it to filemap documents, check lines 7-18
    if file.endswith(tuple(file_types['Documents'])):
        file_map["Documents"].append(file)
    elif file.endswith(tuple(file_types['Images'])):
        file_map["Images"].append(file)
    elif file.endswith(tuple(file_types['Audio'])):
        file_map["Audio"].append(file)
    elif file.endswith(tuple(file_types['Installers'])):
        file_map["Installers"].append(file)
    elif file.endswith(tuple(file_types['Packed Files'])):
        file_map["Packed Files"].append(file)
    elif file.endswith(tuple(file_types['Music Production'])):
        file_map["Music Production"].append(file)
    elif file.endswith(tuple(file_types['Midi'])):
        file_map["Midi"].append(file)
    elif file.endswith(tuple(file_types['Video'])):
        file_map["Video"].append(file)
    elif file.endswith(tuple(file_types['Excel'])):
        file_map["Excel"].append(file)
    elif file.endswith(tuple(file_types['Sound Banks & Presets'])):
        file_map["Sound Banks & Presets"].append(file)
    elif file.endswith(tuple(file_types['Photoshop'])):
        file_map["Photoshop"].append(file)
    elif file.endswith(tuple(file_types['Torrent'])):
        file_map["Torrent"].append(file)
    elif file.endswith(tuple(file_types['PDF'])):
        file_map["PDF"].append(file)
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