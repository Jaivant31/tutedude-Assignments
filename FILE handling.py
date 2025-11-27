try:
    # Attempt to open and read the file
    file = open("sample.txt", "r")

    print("Reading file content:\n")

    # Read and print each line with line numbers
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}")
        line_number += 1

    file.close()

except FileNotFoundError:
    # Display formatted error message if file doesn't exist
    print("Error: The file 'sample.txt' was not found.")
