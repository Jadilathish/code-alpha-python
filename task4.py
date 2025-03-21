import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return
    
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Others": []
    }
    
    for category in file_types.keys():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, file))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", file))
    
    print("Files have been organized successfully!")

if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    organize_files(target_directory)
