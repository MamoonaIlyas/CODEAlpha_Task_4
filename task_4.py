import os
import shutil

# Define folder mappings based on file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".sh", ".bat"]
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        file_extension = os.path.splitext(filename)[1].lower()
        
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_path = os.path.join(directory, category)
                
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved {filename} to {category}/")
                break

if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ")
    organize_files(folder_path)
    print("File organization completed!")
