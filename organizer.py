import os
import shutil

# Define the directory to clean (e.g., your Downloads folder)
# Use "." for the current directory where the script is located
target_dir = "."

# Map extensions to folder names
EXTENSIONS_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Archives': ['.zip', '.tar', '.rar', '.7z'],
    'Audio_Video': ['.mp3', '.wav', '.mp4', '.mkv', '.mov'],
    'Scripts': ['.py', '.js', '.html', '.css', '.cpp']
}

def organize_folder():
    for filename in os.listdir(target_dir):
        # Skip the script itself and directories
        if filename == "organizer.py" or os.path.isdir(filename):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        
        for folder_name, extensions in EXTENSIONS_MAP.items():
            if file_ext in extensions:
                # Create category folder if it doesn't exist
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                
                # Move the file
                shutil.move(filename, os.path.join(folder_name, filename))
                print(f"Moved: {filename} -> {folder_name}")
                break

if __name__ == "__main__":
    print("Starting organization...")
    organize_folder()
    print("Done!")