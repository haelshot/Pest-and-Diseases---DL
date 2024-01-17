import os
import shutil

def merge_duplicate_folders(base_folder):
    # Get the list of subdirectories (disease folders) in the train folder
    disease_folders = [f for f in os.listdir(os.path.join(base_folder, 'train')) if os.path.isdir(os.path.join(base_folder, 'train', f))]

    for disease_folder in disease_folders:
        # Identify duplicates by checking for folders with "_2" suffix
        duplicate_folder = f"{disease_folder}_2"
        original_folder = disease_folder

        # Check if the duplicate folder exists
        if os.path.exists(os.path.join(base_folder, 'train', duplicate_folder)):
            # Get the list of images in the duplicate folder
            duplicate_images = os.listdir(os.path.join(base_folder, 'train', duplicate_folder))

            # Move each image from duplicate folder to the original folder
            for image in duplicate_images:
                source_path = os.path.join(base_folder, 'train', duplicate_folder, image)
                destination_path = os.path.join(base_folder, 'train', original_folder, image)
                shutil.move(source_path, destination_path)

            # Remove the empty duplicate folder
            os.rmdir(os.path.join(base_folder, 'train', duplicate_folder))
            print(f"Merged images in {disease_folder} and {duplicate_folder}")

if __name__ == "__main__":
    # Specify the base folder containing rice and corn folders
    base_folder = "/home/hael/Desktop/Pest-and-Diseases---DL/Folder-fixings"  # Replace with your actual base folder path

    # Merge duplicate folders in both rice and corn train folders
    merge_duplicate_folders(os.path.join(base_folder, 'rice'))
    merge_duplicate_folders(os.path.join(base_folder, 'corn'))
