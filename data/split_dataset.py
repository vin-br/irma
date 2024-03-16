import os
import random
import shutil


def create_test_sample(parent_folder, selection_rate=0.20):
    """
    Create a test sample by selecting a random subset of images from each label folder
    in the given parent folder and moving them to a separate "testing" directory.

    Args:
    parent_folder (str): Path to the parent folder containing the label folders.
    selection_rate (float): The proportion of images to select from each label folder.
    Default is 0.20 (20%).

    Returns:
    None
    """
    # Destination directory for test images
    test_dataset_dir = os.path.join(parent_folder, "testing")

    # Create the test directory if it doesn't exist
    os.makedirs(test_dataset_dir, exist_ok=True)

    # List of label folders
    label_folders = ["glioma_tumor", "meningioma_tumor", "no_tumor", "pituitary_tumor"]

    # Loop through the label folders
    for label_folder in label_folders:
        # Get the full path to the label folder
        label_folder_path = os.path.join(parent_folder, label_folder)

        # Count the total number of images in this folder
        images = [
            f
            for f in os.listdir(label_folder_path)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
        ]
        total_images = len(images)

        # Select a random sample of the specified proportion of images
        num_images_to_select = int(total_images * selection_rate)
        selected_images = random.sample(images, num_images_to_select)

        # Create a subdirectory for this label in the test directory
        test_label_dir = os.path.join(test_dataset_dir, label_folder)
        os.makedirs(test_label_dir, exist_ok=True)

        # Move the selected images to the test directory
        for image in selected_images:
            source_path = os.path.join(label_folder_path, image)
            destination_path = os.path.join(test_label_dir, image)
            shutil.move(source_path, destination_path)

    print("Test sample created successfully.")


if __name__ == "__main__":
    parent_folder = input("Enter the path to the parent folder: ")
    create_test_sample(parent_folder)
