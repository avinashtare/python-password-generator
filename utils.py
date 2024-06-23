import string
import random
from tkinter import messagebox

def generate_password(length, include_numbers, include_special_chars, include_uppercase):
    characters = string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def genrate_password(length, include_numbers, include_special_chars, include_uppercase):
    try:
        length = int(length)
    except Exception as e:
        messagebox.showerror("error","Please Insert a number in length input.")
    if not isinstance(length, int) or length < 8:
        messagebox.showerror("error","Length must be equal to 8.")
        raise ValueError("Length must be equal to 8.")

    
    if not isinstance(include_numbers, bool):
        raise ValueError("include_numbers must be a boolean.")
    if not isinstance(include_special_chars, bool):
        raise ValueError("include_special_chars must be a boolean.")
    if not isinstance(include_uppercase, bool):
        raise ValueError("include_uppercase must be a boolean.")
    
    password = generate_password(length, include_numbers, include_special_chars, include_uppercase)

    return password
