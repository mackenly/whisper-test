import os
import tkinter as tk
from tkinter import filedialog

import openai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()


# Main function calls the other functions and validates the file
def main():
    file_path = pick_file()
    if file_path:
        print(f"File selected: {file_path}")
        transcribe_file(file_path)
    else:
        print("No file selected")


# This function picks a file
def pick_file():
    root = tk.Tk()
    root.withdraw()  # This hides the root window
    path = filedialog.askopenfilename()  # This opens the file picker
    return path


# This function transcribes the file using the OpenAI API
def transcribe_file(path):
    openai.api_key = os.getenv('API_KEY')
    audio_file = open(path, "rb")
    print("Transcribing... (this may take a few minutes)")
    transcript = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        response_format="json"
    )

    # get the file name from the path, without the extension
    file_name = os.path.splitext(os.path.basename(path))[0]
    file_name = file_name + "_output.txt"

    # write the transcript to a file named "output.txt"
    with open(file_name, "w") as f:
        f.write(transcript['text'])
        print(f"Transcript written to: {file_name}")

    # print the transcript to the console
    print(transcript["text"])


if __name__ == "__main__":
    main()
