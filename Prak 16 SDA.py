import tkinter as tk
from tkinter import messagebox

def pancake_sort(arr):
    arr_len = len(arr)

    while arr_len > 1:
        max_index = arr.index(max(arr[:arr_len]))
        arr = arr[max_index::-1] + arr[max_index + 1:]
        arr = arr[:arr_len][::-1] + arr[arr_len:]
        arr_len -= 1

    return arr

window = tk.Tk()
window.title("Pancake Sort Visualization")

input_label = tk.Label(window, text="Input Numbers (separated by commas):")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

output_label = tk.Label(window, text="Sorted Numbers:")
output_label.pack()
output_text = tk.StringVar()
output_display = tk.Label(window, textvariable=output_text)
output_display.pack()

def sort_button_clicked():
    try:
        # Request input numbers and convert them to integers
        input_string = input_entry.get()
        input_list = [int(x) for x in input_string.split(",")]
        
        # Sort the list using pancake sort
        sorted_list = pancake_sort(input_list.copy())
        
        # Update the output text
        output_text.set(f"Sorted Numbers: {', '.join(map(str, sorted_list))}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input: Please enter comma-separated numbers.")

# Sort button
sort_button = tk.Button(window, text="Sort", command=sort_button_clicked)
sort_button.pack()

# Run the main event loop
window.mainloop()
