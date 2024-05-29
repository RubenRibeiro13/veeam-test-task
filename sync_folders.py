# Import built-in libraries

import os
import shutil
import hashlib
import time
import logging
import argparse

# Calculate MD5 checksum for a file

def calculate_md5(file_path):
    # Create an MD5 hash object
    hash_md5 = hashlib.md5()

    # Read the file in chunks and continuously update the MD5 hash object with the contents of each chunk
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    
    # Return the hexadecimal representation of the updated MD5 hash object
    return hash_md5.hexdigest()

# Synchronize source and replica folders

def sync_folders(source_folder, replica_folder):
    # Copy directories and files in the source folder to the replica folder
    for source_dir, _, source_files in os.walk(source_folder):
        replica_dir = source_dir.replace(source_folder, replica_folder, 1)

        if not os.path.exists(replica_dir):
            os.makedirs(replica_dir)
            logging.info(f"Created {replica_dir}")

        for file_name in source_files:
            source_file = os.path.join(source_dir, file_name)
            replica_file = os.path.join(replica_dir, file_name)

            source_file_md5 = calculate_md5(source_file)
            replica_file_md5 = calculate_md5(replica_file) if os.path.exists(replica_file) else None

            if not replica_file_md5 or source_file_md5 != replica_file_md5:
                shutil.copy2(source_file, replica_file)
                logging.info(f"Created {replica_file}") if not replica_file_md5 else logging.info(f"Updated {replica_file}")

    # Remove directories and files in the replica folder that do not exist in the source folder
    for replica_dir, replica_subdirs, replica_files in os.walk(replica_folder, topdown = False):
        source_dir = replica_dir.replace(replica_folder, source_folder, 1)

        for file_name in replica_files:
            replica_file = os.path.join(replica_dir, file_name)
            source_file = os.path.join(source_dir, file_name)

            if not os.path.exists(source_file):
                os.remove(replica_file)
                logging.info(f"Removed {replica_file}")

        for subdir_name in replica_subdirs:
            replica_subdir = os.path.join(replica_dir, subdir_name)
            source_subdir = os.path.join(source_dir, subdir_name)

            if not os.path.exists(source_subdir):
                shutil.rmtree(replica_subdir)
                logging.info(f"Removed {replica_subdir}")

# Main function

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Synchronize source and replica folders.")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("interval", type=int, help="Synchronization interval (in seconds)")
    args = parser.parse_args()

    # Ensure source and replica folders exist
    if not os.path.exists(args.source_folder) or not os.path.exists(args.replica_folder):
        if not os.path.exists(args.source_folder):
            logging.error("Source folder does not exist.")

        if not os.path.exists(args.replica_folder):
            logging.error("Replica folder does not exist.")
        
        return

    # Set up logging to log file and console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(args.log_file),
            logging.StreamHandler()
        ]
    )

    # Synchronize folders periodically
    while True:
        sync_folders(args.source_folder, args.replica_folder)
        time.sleep(args.interval)

# Call main function when the script is run directly

if __name__ == "__main__":
    main()