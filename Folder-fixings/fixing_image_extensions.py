from PIL import Image
import os

def convert_images_to_jpg(folder_path):
    # Get the list of subdirectories (disease folders) in the train or validation folder
    disease_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    for disease_folder in disease_folders:
        # Get the list of images in the disease folder
        image_files = [f for f in os.listdir(os.path.join(folder_path, disease_folder)) if os.path.isfile(os.path.join(folder_path, disease_folder, f))]

        # Convert each image to JPG format
        for image_file in image_files:
            image_path = os.path.join(folder_path, disease_folder, image_file)
            # Open the image
            with Image.open(image_path) as img:
                # Save the image in JPG format (overwrite the original)
                img.convert("RGB").save(image_path.replace(os.path.splitext(image_file)[1], ".jpg"), "JPEG")
            print(f"Converted: {image_file} to JPG format")

if __name__ == "__main__":
    # Specify the base folder containing rice and corn folders
    base_folder = "/home/hael/Desktop/Pest-and-Diseases---DL/Folder-fixings"  # Replace with your actual base folder path

    # Convert images to JPG format in both rice and corn train folders
    convert_images_to_jpg(os.path.join(base_folder, 'rice', 'train'))
    convert_images_to_jpg(os.path.join(base_folder, 'rice', 'validation'))
    convert_images_to_jpg(os.path.join(base_folder, 'corn', 'train'))
    convert_images_to_jpg(os.path.join(base_folder, 'corn', 'validation'))
