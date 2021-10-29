import os
import shutil

inpt = input("root:")  # Folder to "go through"
root = inpt

file_types = {
    # File types which are used in for loop in line 51-72
    "Documents": ["docx", "odt", "rtf", "txt", "ods", "pptx", "dotx", "doc", "ppt"],
    "Images": ["jpg", "png", "jpeg","ico"],
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

for root, dirs, files in os.walk(root):
    exclude = tuple(set(dirs) - set(list(folder_names)))
    dirs[:] = [dirname for dirname in dirs if dirname not in exclude]
    for file in files:
        # Checking files in the root folder
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
        path_ext = os.path.join(root, folder_name)
        try:
            os.makedirs(path_ext, exist_ok=True)
        except Exception as exc:
            pass
            print(exc)
            print("Folder already exists, skipping folder creation")
        for file in files_for_folder:
            path_for_folder = os.path.join(root, folder_name)
            path_for_file = os.path.join(root, file)
            try:
                shutil.move(path_for_file, path_for_folder)
            except Exception as exc:
                pass
                # print(exc)
                print(file, " already exists in the folder")
