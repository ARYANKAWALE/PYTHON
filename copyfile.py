def copy_file():
    source_name = input("Enter the name of the source file: ")
    destination_name = input("Enter the name of the destination file: ")
    try:
        with open(source_name, 'r') as source_file:
            contents = source_file.read()
        with open(destination_name, 'w') as dest_file:
            dest_file.write(contents)
        print(f"Successfully copied contents from '{source_name}' to '{destination_name}'.")
    except FileNotFoundError:
        print(f"Error: The source file '{source_name}' was not found. Please check the name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    copy_file()