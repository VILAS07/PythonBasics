def write_note():
    text = input("Enter text to write into the notepad:\n")
    with open("notepad.txt", "w") as file:
        file.write(text + "\n")
    print("Note written successfully!\n")


def read_note():
    try:
        with open("notepad.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("\nNotepad is Empty\n")
            else:
                print("\nNotepad Content ")
                print(content, end="")
                print("\n")
    except FileNotFoundError:
        print("\nNo notes found! Write something first.\n")


def append_note():
    text = input("Enter text to append to the notepad:\n")
    with open("notepad.txt", "a") as file:
        file.write(text + "\n")
    print("Note appended successfully!\n")


def menu():
    while True:
        print("===== Simple Notepad =====")
        print("1. Write Note (Overwrite)")
        print("2. Read Note")
        print("3. Append Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            write_note()
        elif choice == "2":
            read_note()
        elif choice == "3":
            append_note()
        elif choice == "4":
            print("Exiting Notepad. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


menu()
