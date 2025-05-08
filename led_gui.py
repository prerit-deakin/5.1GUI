import tkinter as tk
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
red = 17  # GPIO pin for Red LED
green = 27  # GPIO pin for Green LED
blue = 22  # GPIO pin for Blue LED

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Function to turn on the selected LED
def turn_on_led(color):
    GPIO.output(red, color == "red")
    GPIO.output(green, color == "green")
    GPIO.output(blue, color == "blue")

# Create the main window
window = tk.Tk()
window.title("LED Control")

# Add radio buttons for each LED color
tk.Radiobutton(window, text="Red", value="red", command=lambda: turn_on_led("red")).pack()
tk.Radiobutton(window, text="Green", value="green", command=lambda: turn_on_led("green")).pack()
tk.Radiobutton(window, text="Blue", value="blue", command=lambda: turn_on_led("blue")).pack()

# Exit button
tk.Button(window, text="Exit", command=window.quit).pack()

# Start the GUI
window.mainloop()

# Clean up
GPIO.cleanup()
