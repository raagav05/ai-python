from textblob import TextBlob
import tkinter as tk
from tkinter import scrolledtext

def autocorrect(text):
    # Split text into words
    words = text.split()
    corrected_text = []
    for word in words:
        if word.isalpha():  # Consider only alphabetic tokens
            corrected_word = TextBlob(word).correct().string.strip()
            corrected_text.append(corrected_word)
        else:
            corrected_text.append(word)
    return ' '.join(corrected_text)

def correct_text():
    input_text = text_entry.get("1.0", tk.END).strip()
    corrected = autocorrect(input_text)
    corrected_text.config(state=tk.NORMAL)
    corrected_text.delete("1.0", tk.END)
    corrected_text.insert(tk.END, corrected)
    corrected_text.config(state=tk.DISABLED)

# Set up the main application window
root = tk.Tk()
root.title("AI-Driven Autocorrect Tool")
root.configure(bg="#797d7f")  # Set window background color

# Set up the widgets
text_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, bg="#c39bd3", fg="#333333", font=("Helvetica", 12))
correct_button = tk.Button(root, text="Correct Text", command=correct_text, bg="#f04341", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
corrected_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED, bg="#c39bd3", fg="#333333", font=("Helvetica", 12))

# Arrange the widgets using grid layout
text_entry.grid(row=0, column=0, padx=10, pady=10)
correct_button.grid(row=1, column=0, padx=10, pady=10)
corrected_text.grid(row=2, column=0, padx=10, pady=10)

# Run the application
root.mainloop()
