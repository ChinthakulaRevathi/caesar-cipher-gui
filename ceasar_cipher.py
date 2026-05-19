from tkinter import *
from tkinter import messagebox

# Function to encrypt text
def encrypt():
    text = message_entry.get()
    shift = shift_entry.get()

    if not text or not shift:
        messagebox.showerror("Error", "Please enter message and shift value")
        return

    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number")
        return

    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26

            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char

    result_label.config(text="Encrypted Text: " + result)


# Function to decrypt text
def decrypt():
    text = message_entry.get()
    shift = shift_entry.get()

    if not text or not shift:
        messagebox.showerror("Error", "Please enter message and shift value")
        return

    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number")
        return

    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = (-shift) % 26

            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char

    result_label.config(text="Decrypted Text: " + result)


# Create GUI Window
root = Tk()
root.title("Caesar Cipher")
root.geometry("500x350")
root.config(bg="lightblue")

# Title
title_label = Label(root, text="Caesar Cipher Encryption & Decryption",
                    font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=15)

# Message Input
Label(root, text="Enter Message:", font=("Arial", 12),
      bg="lightblue").pack()

message_entry = Entry(root, width=40, font=("Arial", 12))
message_entry.pack(pady=5)

# Shift Input
Label(root, text="Enter Shift Value:", font=("Arial", 12),
      bg="lightblue").pack()

shift_entry = Entry(root, width=10, font=("Arial", 12))
shift_entry.pack(pady=5)

# Buttons
encrypt_button = Button(root, text="Encrypt", font=("Arial", 12, "bold"),
                         bg="green", fg="white", command=encrypt)
encrypt_button.pack(pady=10)

decrypt_button = Button(root, text="Decrypt", font=("Arial", 12, "bold"),
                         bg="red", fg="white", command=decrypt)
decrypt_button.pack(pady=5)

# Result Label
result_label = Label(root, text="Result will appear here",
                     font=("Arial", 12, "bold"), bg="lightblue")
result_label.pack(pady=20)

# Run GUI
root.mainloop()