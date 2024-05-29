# Folder Synchronization Script
## Description
This Python script synchronizes the contents of two folders and logs the corresponding operations to a log file and to the console output. The synchronization is periodic and one-way, which means the replica folder is a mirror of the source folder.

## Usage
### Basic Usage
```bash
python sync_folders.py source_folder replica_folder log_file interval
```

### Command-Line Arguments
- source_folder: Path to the source folder.
- replica_folder: Path to the replica folder.
- log_file: Path to the log file.
- interval: Synchronization interval (in seconds).

## Tests Performed
1. Initial Sync:
- Test: Run the script with a source folder containing files and directories and an empty replica folder.
- Result: All files and directories from the source folder are copied to the replica folder.

2. No Changes:
- Test: Run the script again without making any changes to the source folder.
- Result: No changes happen in the replica folder.

3. File Modification (Source Folder)
- Test: Modify a file in the source folder and run the script.
- Result: The modified file is updated in the replica folder.

4. File Addition (Source Folder)
- Test: Add a new file to the source folder and run the script.
- Result: The new file is copied to the replica folder.

5. File Deletion (Source Folder)
- Test: Delete a file from the source folder and run the script.
- Result: The corresponding file is deleted from the replica folder.

6. Directory Addition (Source Folder)
- Test: Add a new directory with files to the source folder and run the script.
- Result: The new directory and its contents are copied to the replica folder.

7. Directory Deletion (Source Folder)
- Test: Delete a directory from the source folder and run the script.
- Result: The corresponding directory and its contents are deleted from the replica folder.

8. File Modification (Replica Folder)
- Test: Modify a file in the replica folder (close the file right after saving it) and run the script.
- Result: The modified file reverts back to its previous state.

9. File Addition (Replica Folder)
- Test: Add a new file to the replica folder and run the script.
- Result: The new file is deleted from the replica folder.

10. File Deletion (Replica Folder)
- Test: Delete a file from the replica folder and run the script.
- Result: The deleted file is added back to the replica folder.

11. Directory Addition (Replica Folder)
- Test: Add a new directory with files to the replica folder and run the script.
- Result: The new directory and its contents are deleted from the replica folder.

12. Directory Deletion (Replica Folder)
- Test: Delete a directory from the replica folder and run the script.
- Result: The deleted directory and its contents are added back to the replica folder.

13. Empty Source Folder
- Test: Empty the source folder and run the script.
- Result: The replica folder is also emptied.

14. Performance and Stress
- Test: Use a source folder with large files (at least 100 MB) and/or a large number of files (at least 1000) and run the script.
- Result: The script completes the synchronization successfully within a reasonable amount of time.

15. Periodic Sync
- Test: Run the script with a short synchronization interval and make changes to the source folder between intervals.
- Result: Changes are synchronized to the replica folder at the end of each interval.

16. Non-Existent Source and/or Replica Folders
- Test: Use non-existent source and/or replica folders and run the script.
- Result: A custom error message is logged to the console, and the script is not run.

17. Log File Creation
- Test: Use a non-existent log file and run the script.
- Result: The log file is created, and all the operations performed are written to it.

18. Invalid Arguments
- Test: Run the script with invalid or missing command line arguments (e.g., non-integer synchronization interval).
- Result: An error message is logged to the console, and the script is not run.

## Notes
- The script is designed to work on multiple operating systems, including Windows, MacOS, and Linux.
- The script is optimized in terms of efficiency, since it uses built-in libraries and processes files in chunks.
- No third-party libraries are used because the built-in modules offer sufficient capabilities and keep the code lightweight.
- Files are compared using MD5 checksum calculation instead of the `filecmp.cmp` function to provide an additional layer of accuracy, especially when dealing with large files.
- While MD5 is a reliable choice for basic file comparison, it is not suitable for security-related tasks due to its vulnerabilities.