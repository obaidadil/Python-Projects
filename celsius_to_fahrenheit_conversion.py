import tkinter as tk

# Main window
window = tk.Tk()
window.title("Temperature Converter")

# Conversion function
def convert():
    # Get the value to convert and the units
    celsius = float(input_value.get())
    fahrenheit = celsius * 9 / 5 + 32
    # Update the result label with the converted value
    result_label.config(text=f"{fahrenheit:.2f}°F")

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
