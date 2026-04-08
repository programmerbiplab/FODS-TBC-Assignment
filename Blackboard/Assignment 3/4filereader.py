'''The following program asks input 
file name from the user and
writes ontop of the output file and
displays message if not'''

# Defining a function
def copy_file():
    try:
        # Asking for input file name
        input_file = input("Enter the name of the input file: ")
        # Trying to open input file
        with open(input_file, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return

    try:
        # Asking for output file name
        output_file = input("Enter the name of the output file: ")
        # Checking if output file already exists
        with open(output_file, 'x') as outfile:
            outfile.write(content)
        print(f"File has been successfully copied to '{output_file}'.")
    except FileExistsError:
        print(f"Error: The output file '{output_file}' already exists. Choose a different name.")
    except Exception as e:
        print(f"An unexpected error occurred while writing the file: {e}")

# Calling the function
copy_file()

# by Biplab Prasad Gajurel 25024641