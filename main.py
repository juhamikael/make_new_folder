import os
import shutil

# inpt = input("Input root:")
root = "E:/2017/49 May 2021"


def file_types(file_type):
    input_in_lower = file_type.lower()
    if input_in_lower == "documents":
        return ["pdf", "docx", "odt", "rtf", "txt", "ods", "pptx", "dotx", "doc", "ppt"]
    if input_in_lower == "images":
        return ["jpg", "png", "jpeg"]
    if input_in_lower == "audio":
        return ["mp3", "wav", "aac"]
    if input_in_lower == "application":
        return ["exe", "msi"]
    if input_in_lower == "packed_files":
        return ["zip", "rar"]
    if input_in_lower == "flp":
        return ["flp"]
    if input_in_lower == "midi":
        return ["midi", "mid"]
    if input_in_lower == "video":
        return ["mp4", "gif", "mpeg", "mkv"]
    if input_in_lower == "excel":
        return ["xlsx", "csv", "xlsm", "xls"]


folder_names = [
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
]
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
        for filetype in folder_names:
            if file.endswith(tuple(file_types("documents"))):
                file_map["Documents"].append(file)
            elif file.endswith(tuple(file_types("images"))):
                file_map["Images"].append(file)
            elif file.endswith(tuple(file_types("audio"))):
                file_map["Audio"].append(file)
            elif file.endswith(tuple(file_types("application"))):
                file_map["Installers"].append(file)
            elif file.endswith(tuple(file_types("packed_files"))):
                file_map["Packed Files"].append(file)
            elif file.endswith(tuple(file_types("flp"))):
                file_map["FLP"].append(file)
            elif file.endswith(tuple(file_types("midi"))):
                file_map["Midi"].append(file)
            elif file.endswith(tuple(file_types("video"))):
                file_map["Video"].append(file)
            elif file.endswith(tuple(file_types("excel"))):
                file_map["Excel"].append(file)
            elif file.endswith(tuple(file_types("video"))):
                file_map["Video"].append(file)
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
            # print(exc)
            print("Folder alreay exists, skipping folder creation")
        for file in files_for_folder:
            path_for_folder = os.path.join(root, folder_name)
            path_for_file = os.path.join(root, file)
            try:
                shutil.move(path_for_file, path_for_folder)
            except Exception as exc:
                pass
                # print(exc)
                print(file, " already exists in the folder")

