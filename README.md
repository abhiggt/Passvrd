# Passvrd - Password Generator & Vault

This Python script generates passwords based on user-defined criteria using a graphical user interface (GUI) built with Tkinter, User can save the passwords in the Vault that only opens on correct key entered.

`Trailer/Walkthrough` == https://youtu.be/2CLWf0NArmo?si=bnIksampo0lB2phT

## Description

The script allows users to generate passwords of varying strengths (Low, Medium, Strong) and lengths. It provides options to copy the generated password to the clipboard and save it for future use.

## Dependencies

- Python 3.12
- `pyperclip` library (to copy passwords to clipboard)
- `tkinter` library (for GUI)

## Usage

1. Run the Script
2. The GUI window appears, titled "Passvrd - Password Generator."
3. Choose the password strength (Low, Medium, Strong) and length using radio buttons and a slider, respectively.
4. Click the "Generate" button to create a password based on the chosen criteria.
5. The generated password appears in the designated text entry field.
6. Click the "Copy" button to copy the password to the clipboard.
7. You can save it by going to Open Vault button

## Functionality

- The script utilizes the `random` module to generate passwords.
- Tkinter is used to create a user-friendly GUI.
- Users can select the strength and length of the password.
- Passwords are generated based on the selected criteria and displayed in the GUI.
- The `pyperclip` library enables copying the generated password to the clipboard.
- Upon clicking the "Copy" button, the password is copied to the clipboard and a success message is displayed using a messagebox.

## Notes

- Ensure `pyperclip` and `tkinter` libraries are installed to run the script.
- This script provides a simple way to generate passwords using a GUI, making it user-friendly and accessible.
