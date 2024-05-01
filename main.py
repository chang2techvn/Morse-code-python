import tkinter as tk
from tkinter import messagebox
import pyperclip


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----', '0': '-----', '': '/'
}

reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + '/'
        else:
            morse_code += char
    return morse_code.strip('/')

def morse_to_text(morse_code):
     words = morse_code.split('/')
     text = ''
     for word in words:
         letters = word.split()
         for letter in letters:
             if letter in reverse_morse_code_dict:
                 text += reverse_morse_code_dict[letter]
             else:
                 text += letter
         text += ''
     return text.strip()

def convert():
    user_input = entry.get()
    if any(char in user_input for char in ['.', '-', '/']):
        result = morse_to_text(user_input)
        print("Converted text:", result)
        result_label.config(text="Convert text: " + result)
        pyperclip.copy(result)
        messagebox.showinfo("Copied!", "Text copied to clipboard!")
    else:
        result = text_to_morse(user_input)
        print("Morse code:", result)
        result_label.config(text="Morse code: " + result)
        pyperclip.copy(result)
        messagebox.showinfo("Copied!", "Text copied to clipboard!")


#Create Tkinter window
root = tk.Tk()
root.title("Morse Code")
root.geometry("300x300")


#Create label and entry for input
tk.Label(root, text='Enter a string to convert: ').pack()
entry = tk.Entry(root)
entry.pack()

#Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()


#Create convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()




root.mainloop()