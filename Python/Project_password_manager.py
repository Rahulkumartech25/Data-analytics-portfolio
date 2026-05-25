import pyperclip
import os

FILE_NAME = "password.txt"

def save_password():
    Website = input("Enter website: ")
    Password = input("Enter password: ")
    with open(FILE_NAME, "a") as f:
        f.write(f"{Website}<||>{Password}\n")

def get_password():
    Website = input("Enter website: ")
    with open(FILE_NAME, "r") as f:
        for line in f:
            if Website in line:
                password = line.split("<||>")[1].strip()
                pyperclip.copy(password)
                print("Password copied to clipboard.")
                break
        else:
            print("Website not found.")

def main():
    while True:
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")
        choice = input("Chose an option: ")

        if choice == "1":
            save_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
