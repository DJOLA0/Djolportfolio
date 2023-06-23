# code for running a code from the start 
# use try and except to catch any errors when opening the file

while True:
    choice = input("Enter 'open' to open a file or 'repeat' to choose a different file")
    if choice == 'open':
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
    elif choice == 'repeat':
        continue
    else:
        print("Invalid choice. Please enter 'open' or 'repeat'.")