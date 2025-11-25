import os
import shutil

folder_path = r"C:\Users\hp\Desktop\PrimeBatch\Day-5"

while True:
    print("\n--- File Manager ---")
    print("1. Create new file")
    print("2. Write to file (overwrite)")
    print("3. Append to file")
    print("4. Read file")
    print("5. Delete file")
    print("6. Rename file")
    print("7. Show all files")
    print("8. Copy file")
    print("9. Exit")

    choice = input("Enter your choice: ")

    # 1. Create file
    if choice == "1":
        file_name = input("Enter file name (example: sample3.txt): ")
        path = os.path.join(folder_path, file_name)

        try:
            f = open(path, "x")
            f.write("New file created.\n")
            f.close()
            print("File created at:", path)
        except FileExistsError:
            print("Error: File already exists.")

    # 2. Write file
    elif choice == "2":
        file_name = input("Enter file name to WRITE: ")
        path = os.path.join(folder_path, file_name)

        f = open(path, "w")
        text = input("Enter text to write: ")
        f.write(text)
        f.close()
        print("File overwritten successfully.")

    # 3. Append file
    elif choice == "3":
        file_name = input("Enter file name to APPEND: ")
        path = os.path.join(folder_path, file_name)

        f = open(path, "a")
        text = input("Enter text to append: ")
        f.write("\n" + text)
        f.close()
        print("Text appended successfully.")

    # 4. Read file
    elif choice == "4":
        file_name = input("Enter file name to READ: ")
        path = os.path.join(folder_path, file_name)

        if os.path.exists(path):
            f = open(path, "r")
            content = f.read()
            f.close()
            print("\n--- File Content ---\n")
            print(content)
        else:
            print("Error: File does not exist.")

    # 5. Delete file
    elif choice == "5":
        file_name = input("Enter file name to DELETE: ")
        path = os.path.join(folder_path, file_name)

        if os.path.exists(path):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("Error: File not found.")

    # 6. Rename file
    elif choice == "6":
        old_name = input("Enter file name to RENAME: ")
        new_name = input("Enter NEW file name: ")

        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print("File renamed successfully.")
        else:
            print("Error: File not found.")

    # 7. Show all files
    elif choice == "7":
        print("\n--- Files in Day-5 Folder ---")
        files = os.listdir(folder_path)
        for file in files:
            print(file)

    # 8. Copy file
    elif choice == "8":
        src = input("Enter file name to COPY: ")
        dst = input("Enter new file name (copy result): ")

        src_path = os.path.join(folder_path, src)
        dst_path = os.path.join(folder_path, dst)

        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
            print("File copied successfully.")
        else:
            print("Error: Source file does not exist.")

    # 9. Exit
    elif choice == "9":
        print("Exiting program...")
        break

    else:
        print("Invalid option, try again.")
