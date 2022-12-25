import tkinter as tk

# Main window
window = tk.Tk()
window.title("Weight Converter")

# Conversion function
def convert():
    # Get the value to convert and the units
    kilograms = float(input_value.get())
    pounds = kilograms * 2.20462
    # Update the result label with the converted value
    result_label.config(text=f"{pounds:.2f} lbs")

# Input field
input_value = tk.StringVar()
input_field = tk.Entry(window, textvariable=input_value)
input_field.pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main loop
window.mainloop()
