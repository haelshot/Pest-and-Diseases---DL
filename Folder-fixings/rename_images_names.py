import os

def rename_images(folder_path):
    # Get the list of subdirectories (disease folders) in the train or validation folder
    disease_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    for disease_folder in disease_folders:
        # Get the list of images in the disease folder
        image_files = [f for f in os.listdir(os.path.join(folder_path, disease_folder)) if os.path.isfile(os.path.join(folder_path, disease_folder, f))]

        # Rename each image with folder name coupled with numbers
        for i, image_file in enumerate(image_files, start=1):
            # Get the file extension
            _, extension = os.path.splitext(image_file)

            # Create the new filename
            new_filename = f"{disease_folder}_{i:02d}{extension}"

            # Rename the image file
            old_path = os.path.join(folder_path, disease_folder, image_file)
            new_path = os.path.join(folder_path, disease_folder, new_filename)
            os.rename(old_path, new_path)

            print(f"Renamed: {image_file} to {new_filename}")

if __name__ == "__main__":
    # Specify the base folder containing rice and corn folders
    base_folder = "/home/hael/Desktop/Pest-and-Diseases---DL/Folder-fixings"  # Replace with your actual base folder path

    # Rename images in both rice and corn train folders
    rename_images(os.path.join(base_folder, 'rice', 'train'))
    rename_images(os.path.join(base_folder, 'rice', 'validation'))
    rename_images(os.path.join(base_folder, 'corn', 'train'))
    rename_images(os.path.join(base_folder, 'corn', 'validation'))
