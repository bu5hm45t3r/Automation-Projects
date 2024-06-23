import os
import datetime
import shutil

# Define the path to the desktop and the main folder
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
main_folder = 'Desktop Files'

# Create the main folder if it does not exist
if not os.path.exists(os.path.join(desktop_path, main_folder)):
    os.makedirs(os.path.join(desktop_path, main_folder))

# Loop through all files on the desktop
for filename in os.listdir(desktop_path):
    # Check if the file is not the main folder
    if filename != main_folder:
        # Get the file extension
        file_ext = os.path.splitext(filename)[1][1:]

        # Create the child folder if it does not exist
        child_folder_path = os.path.join(desktop_path, main_folder, file_ext)
        if not os.path.exists(child_folder_path):
            os.makedirs(child_folder_path)

        # Get the file date
        file_date = datetime.datetime.now()

        # Create a folder for the file date if it does not exist
        date_folder_path = os.path.join(child_folder_path, str(file_date.date()))
        if not os.path.exists(date_folder_path):
            os.makedirs(date_folder_path)

        # Move the file to its new location
        shutil.move(os.path.join(desktop_path, filename), date_folder_path)

        # Check for duplicates
        if os.listdir(date_folder_path):
            for file in os.listdir(date_folder_path):
                if file != filename:
                    # Check if the file is a duplicate
                    if os.path.getsize(os.path.join(date_folder_path, file)) == os.path.getsize(os.path.join(date_folder_path, filename)):
                        # Handle the duplicate
                        print(f"Duplicate file found: {file}")
                        os.remove(os.path.join(date_folder_path, file))

# Print a success message
print("Files organized successfully.")
