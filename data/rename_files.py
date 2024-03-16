import os


def rename_files_in_folder():
    """
    Prompt the user to input the path to a folder, then rename all files in the folder
    using the first letter of the folder name (capitalized) followed by an underscore
    and the iterative number of the picture.
    """
    folder_path = input("Enter the path to the folder containing the files to rename: ")

    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("Error: The specified folder does not exist.")
        return

    # Get a list of all files in the folder
    files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    # Get the first letter of the folder name and capitalize it
    folder_name_first_letter = os.path.basename(folder_path).capitalize()[0]

    # Sort the files by filename to ensure consistent renaming order
    files.sort()

    # Rename each file
    for i, filename in enumerate(files):
        old_filepath = os.path.join(folder_path, filename)
        new_filename = f"{folder_name_first_letter}_{i:04}.{filename.split('.')[-1]}"
        new_filepath = os.path.join(folder_path, new_filename)
        os.rename(old_filepath, new_filepath)

    print("Files renamed successfully!")


if __name__ == "__main__":
    rename_files_in_folder()
