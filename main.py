import os
import shutil

inpt = input("root:")  # Folder to "go through"
root = inpt

file_types = {
    # File types which are used in for loop in line 51-72
    "Documents": ["pdf", "docx", "odt", "rtf", "txt", "ods", "pptx", "dotx", "doc", "ppt"],
    "Images": ["jpg", "png", "jpeg"],
    "Audio": ["mp3", "wav", "aac"],
    "Installers": ["exe", "msi"],
    "Packed Files": ["zip", "rar"],
    "FLP": ["flp"],
    "Midi": ["midi", "mid"],
    "Video": ["mp4", "gif", "mpeg", "mkv"],
    "Excel": ["xlsx", "csv", "xlsm", "xls"],
    "Misc": []
}
folder_names = (
    # Folder names to match 'file_types'
    "Documents",
    "Images",
    "Audio",
    "Installers",
    "Packed Files",
    "FLP",
    "Midi",
    "Video",
    "Excel",
    "Misc"
)
file_map = {

    "Documents": [],
    "Images": [],
    "Audio": [],
    "Installers": [],
    "Packed Files": [],
    "FLP": [],
    "Midi": [],
    "Video": [],
    "Excel": [],
    "Misc": []
}

for files in os.walk(root):
    for file in files[2]:
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
        elif file.endswith(tuple(file_types['FLP'])):
            file_map["FLP"].append(file)
        elif file.endswith(tuple(file_types['Midi'])):
            file_map["Midi"].append(file)
        elif file.endswith(tuple(file_types['Video'])):
            file_map["Video"].append(file)
        elif file.endswith(tuple(file_types['Video'])):
            file_map["Video"].append(file)
        elif file.endswith(tuple(file_types['Excel'])):
            file_map["Excel"].append(file)
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
