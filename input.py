# Specify the file name
file_name = 'com_data_file.txt'

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

        # Display the contents
        print("File Contents:")
        print(file_contents)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"Error: {e}")
