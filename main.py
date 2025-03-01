import os
import shutil




extension_to_file_type = {
    ".txt": "Plain Text File",
    ".docx": "Microsoft Word Document",
    ".pdf": "Portable Document Format",
    ".xlsx": "Microsoft Excel Spreadsheet",
    ".pptx": "Microsoft PowerPoint Presentation",
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".png": "Portable Network Graphics",
    ".gif": "Graphics Interchange Format",
    ".bmp": "Bitmap Image File",
    ".svg": "Vector Image File",
    ".mp3": "MP3 Audio File",
    ".wav": "Waveform Audio File",
    ".aac": "Advanced Audio Codec",
    ".mp4": "MPEG-4 Video File",
    ".avi": "Audio Video Interleave File",
    ".mov": "Apple QuickTime Movie",
    ".zip": "ZIP Archive",
    ".rar": "RAR Archive",
    ".exe": "Windows Executable File",
    ".bat": "Batch File",
    ".lnk": "Shortcut File",
    ".url": "Internet Shortcut File",
    ".html": "Hypertext Markup Language File",
    ".css": "Cascading Style Sheets File",
    ".js": "JavaScript File",
}   

folder_categories = {
    "Documents": [".txt", ".docx", ".pdf", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".avi", ".mov"],
    "Compressed Files": [".zip", ".rar"],
    "Executables": [".exe", ".bat"],
    "Shortcuts": [".lnk"],
    "Steam Shortcuts": [".url"],
    "Web": [".html", ".css", ".js"]
}

dir_path = r"C:\Users\anugr\OneDrive\Desktop"

def files_in_folder():
    for files in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path,files)):
            # folder_files = str(os.path.join(dir_path,files))
            yield(files + " [FOLDER] ")
        else:
            yield(files)

# files_in_folder()

def get_file_extensions():
    file_names = files_in_folder()
    for file in file_names:
        ext = os.path.splitext(file)
        if (ext[1] == "" or ext[1] == ".ini"):
            pass
        else:
            yield(ext)

def get_file_types():
    file_extensions = get_file_extensions()
    file_ext_dict = dict((x,y) for x, y in file_extensions)

    file_with_file_type = {}

    for k, v in file_ext_dict.items():
        if v in extension_to_file_type:
            file_with_file_type[k] = extension_to_file_type[v]
    yield(file_with_file_type)


def organize_files():
    file_with_extensions = get_file_extensions()

    for k, v in file_with_extensions:
        file_fname = k + v
        file_path = str(os.path.join(dir_path,file_fname))
        if v in folder_categories["Documents"]:
            folder_path = f"{dir_path}/Documents"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Images"]:
            folder_path = f"{dir_path}/Images"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Audio"]:
            folder_path = f"{dir_path}/Audio"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Video"]:
            folder_path = f"{dir_path}/Video"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Compressed Files"]:
            folder_path = f"{dir_path}/Compressed Files"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Executables"]:
            folder_path = f"{dir_path}/Executables"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Shortcuts"]:
            folder_path = f"{dir_path}/Shortcuts"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Steam Shortcuts"]:
            folder_path = f"{dir_path}/Steam Shortcuts"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        elif v in folder_categories["Web"]:
            folder_path = f"{dir_path}/Web"
            if os.path.exists(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.makedirs(folder_path)
                shutil.move(file_path, folder_path)

        else:
            pass

organize_files()

