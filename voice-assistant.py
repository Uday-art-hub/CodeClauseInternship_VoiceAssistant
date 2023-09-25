import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('mpg321 output.mp3')

# Function to perform actions based on voice commands
def assistant():
    try:
        with sr.Microphone() as source:
            voice_input.delete(1.0, tk.END)  # Clear the previous text
            voice_input.insert(tk.END, "Listening...")
            voice_input.update()
            audio = recognizer.listen(source)
            voice_input.delete(1.0, tk.END)  # Clear the "Listening..." message
            voice_input.update()
            voice_input.insert(tk.END, "Recognizing...")
            voice_input.update()
            command = recognizer.recognize_google(audio)
            voice_input.delete(1.0, tk.END)  # Clear the "Recognizing..." message
            voice_input.insert(tk.END, f"You said: {command}")
            voice_input.update()
            response = get_response(command)
            voice_input.insert(tk.END, f"\nAssistant: {response}")
            voice_input.update()
            speak(response)
    except Exception as e:
        print(e)

# Function to define assistant responses
def get_response(command):
    if 'hello' in command:
        return 'Hello! How can I assist you today?'
    elif 'what is your name' in command:
        return 'I am your Python voice assistant.'
    elif 'exit' in command:
        return 'Goodbye!'
    else:
        return "I'm sorry, I don't understand that command."

# Create the main GUI window
window = tk.Tk()
window.title("Voice Assistant")

# Create a scrolled text widget to display the conversation
voice_input = scrolledtext.ScrolledText(window, width=40, height=10)
voice_input.grid(column=0, row=0, padx=10, pady=10)

# Create a button to trigger voice assistant
assistant_button = tk.Button(window, text="Assistant", command=assistant)
assistant_button.grid(column=0, row=1, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
