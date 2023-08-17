import tkinter as tk
import random
import openai

# Set your OpenAI API key here
openai.api_key = "Your-Api-Key"

def generate_pickup_line():
    prompt = "Generate a pickup line that I can use to impress my crush."
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose an appropriate engine
        prompt=prompt,
        max_tokens=30  # Adjust the desired length of the pickup line
    )

    pickup_line = response.choices[0].text.strip()
    return pickup_line

def impress_crush():
    pickup_line = generate_pickup_line()
    label.config(text=pickup_line)

# Create the main window
window = tk.Tk()
window.title("Pickup Line Generator")
window.geometry("400x300")

# Create a label to display the pickup lines
label = tk.Label(window, text="Push The Button")
label.pack(pady=20)

# Create a button
button = tk.Button(window, text="Generate Pickup Line", command=impress_crush)
button.pack()

# Start the main event loop
window.mainloop()
