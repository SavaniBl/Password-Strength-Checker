
import tkinter as tk
from tkinter import messagebox
import re
import random
import string

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Length < 8 characters": length_error,
        "Missing uppercase letter": uppercase_error,
        "Missing lowercase letter": lowercase_error,
        "Missing number": digit_error,
        "Missing special character": special_char_error,
    }

    strength = 5 - sum(errors.values())
    return strength, errors

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(12))

def evaluate_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, errors = check_password_strength(password)

    # Determine color based on strength
    if strength <= 2:
        color = "red"
    elif strength < 5:
        color = "orange"
    else:
        color = "green"

    # Display strength text
    result_text = f"Password Strength: {strength}/5\n"
    if strength == 5:
        result_text += "✅ Your password is strong!"
    else:
        result_text += "❌ Your password is weak.\nSuggestions:\n"
        for issue, has_issue in errors.items():
            if has_issue:
                result_text += f"- {issue}\n"
        result_text += f"\n🔐 Suggested Strong Password:\n{generate_strong_password()}"

    result_label.config(text=result_text, fg=color)

def toggle_password_visibility():
    if show_password_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

# GUI Setup
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("420x460")
window.resizable(False, False)
window.config(bg="#f2f2f2")

# Widgets
title = tk.Label(window, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="#f2f2f2")
title.pack(pady=10)

entry = tk.Entry(window, width=30, font=("Arial", 12), show="*")
entry.pack(pady=10)

# Show/Hide Password checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(
    window, text="Show Password", variable=show_password_var, onvalue=True, offvalue=False,
    command=toggle_password_visibility, bg="#f2f2f2", font=("Arial", 10)
)
show_password_checkbox.pack()

check_button = tk.Button(window, text="Check Strength", command=evaluate_password, bg="#4CAF50", fg="white", font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(window, text="", justify="left", font=("Arial", 11), bg="#f2f2f2", wraplength=370)
result_label.pack(pady=20)

window.mainloop()
