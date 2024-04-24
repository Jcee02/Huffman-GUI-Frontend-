# Huffman-GUI-Frontend-
Huffman algorithm assignment for Analysis of Algorithms course at Universidad de Guadalajara
The code starts by importing the necessary libraries: tkinter for GUI creation and filedialog for file selection. It also imports the string library to generate a list of all possible characters to be counted in the file.

Next, define a list called characters that contains all possible characters to be counted in the file. Then, it defines a function called count_characters that takes a file handle as input, goes through the file line by line and counts the frequency of each character in the file. This function returns a dictionary where the keys are the characters and the values are the frequencies.

Next, it defines a function called open_file that allows the user to select a text file, calls the count_characters function to count the frequency of characters in the selected file and displays the results in a text widget in the GUI.

In addition, the code defines two incomplete functions called compress and decompress that are supposed to implement compression and decompression algorithms for the file contents. These functions are marked as pending tasks.

Finally, it creates the main application window, adds a text widget to display the results, and buttons to open a file, compress and decompress the content (although these last two functionalities are not fully implemented).

