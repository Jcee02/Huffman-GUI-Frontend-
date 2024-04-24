import tkinter as tk
from tkinter import filedialog
import string

characters = string.printable

# la neta los saltos de linea tabs y así salen bn verguiados ajaja pero mejor usa el atributo printable en vez de mi cochinero 

#Count the characters (nested for lmao)
def count_characters(file_handle):
    """Traverse a file and compute the number of occurences of each letter
    return results as a simple 26 element list of integers."""
    results = {char: 0 for char in characters}
    for line in file_handle:
        for char in line:
            char = char.lower()
            if char in characters:
                results[char] += 1

    return results


# Create function for later examine widget
def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a Text File", filetypes=[("Text files", "*.txt")])
    if file_path:
        sourcedata = open(file_path, encoding="utf8")
        charcounts = count_characters(sourcedata)
        text_widget.delete(1.0, tk.END)
        for char, count in charcounts.items():
            content = "%s=%d\n" % (char, count)
            text_widget.insert(tk.END, content)


# TO-DO
def compress():
    text_widget.delete(1.0, tk.END)
    content = "To do: compressing algorithm"
    text_widget.insert(tk.END, content)


# TO-DO
def decompress():
    text_widget.delete(1.0, tk.END)
    content = "To do: compressing algorithm"
    text_widget.insert(tk.END, content)


# Create the main window
root = tk.Tk()
root.title("Char counter")
# Create a Text widget to display the content
text_widget = tk.Text(root, wrap="word", width=40, height=10)
text_widget.pack(pady=10)
open_button = tk.Button(root, text="Examine", fg="green", command=open_file)
compress_button = tk.Button(root, text="Compress", fg="red", command=compress)
decompress_button = tk.Button(root, text="Decompress", fg="blue", command=decompress)
open_button.pack(pady=10)
compress_button.pack(pady=10)
decompress_button.pack()
root.mainloop()
