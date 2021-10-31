def check_ending(dir_names, file_map, files_dict, endings):

    files = files_dict
    for file in files:
        for ending in endings:
            for folder_name in dir_names:
                if file.endswith(tuple(ending[folder_name])):
                    file_map[folder_name].append(file)
    return file_map
