# Challenge 1: File Read & Write Challenge 🖋️
def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        # Modify the content (e.g., remove empty lines and convert to uppercase)
        modified_content = [line.upper() for line in content if line.strip() != ""]

        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_content)

        print(f"Successfully wrote modified content to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Challenge 2: Error Handling Lab
def user_input_file_reader():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
          
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to open this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run both challenges

def main():
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write the modified content to: ")
    read_and_write_file(input_filename, output_filename)

if __name__ == "__main__":
    main()