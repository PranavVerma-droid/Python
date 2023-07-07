import tkinter as tk
import openai


# Apply the API Key
openai.api_key = "Your API Key Here HEHE BOI"

# Generate a response using OpenAI GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )



    message = completions.choices[0].text # type: ignore
    return message

# GUI interface
def display_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("600x700")

# Create the input field
input_field = tk.Entry(root, font=("Arial", 14))
input_field.pack(pady=10)

# Create the submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=display_response)
submit_button.pack(pady=10)

# Create the output field
output_field = tk.Text(root, font=("Arial", 14), state='disabled')
output_field.pack(pady=10)

# Start the GUI event loop
root.mainloop()