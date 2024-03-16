import os
import sys
import hashlib
import send2trash


def find_duplicates(parent_dir):
    """
    Find and remove duplicate image files in the given parent directory and its
    subdirectories. The duplicate files are moved to the system trash can.
    :param parent_dir: The path to the parent directory to search for duplicates.
    """
    # list to store image hashes
    hashes = []

    # walk through all subdirectories recursively
    for root, dirs, files in os.walk(parent_dir):
        for filename in files:
            # skip non-image files
            if not filename.lower().endswith(
                (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
            ):
                continue
            # open the image and calculate its SHA-256 hash
            image_path = os.path.join(root, filename)
            with open(image_path, "rb") as f:
                data = f.read()
                hash = hashlib.sha256(data).hexdigest()
            # check if the hash already exists in the list
            if hash in hashes:
                print(f"Duplicate found: {image_path}")
                send2trash.send2trash(image_path)
            else:
                hashes.append(hash)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python find_duplicates.py <parent_directory>")
        sys.exit(1)

    parent_directory = sys.argv[1]
    find_duplicates(parent_directory)
