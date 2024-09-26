# 🎤 Text to Speech Application

This is a simple **Text-to-Speech (TTS)** web application that converts text from user input or uploaded documents (PDF or DOCX) into speech. The application automatically detects the language of the text and uses **Google Text-to-Speech (gTTS)** to generate speech audio.

## Features

- **Upload PDF or DOCX Files**: Extracts text from uploaded files and converts it to speech.
- **Text Area Input**: Converts text entered by the user into speech.
- **Language Detection**: Automatically detects the language of the input text or uploaded file before converting it to speech.
- **Audio Playback**: After generating speech, the app allows users to play the audio directly within the interface.

---

## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.7 or above
- Required Python libraries (see [Installation](#installation))

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/nathe444/text-to-speech.git
    cd text-to-speech
    ```

2. **Install the required dependencies**:

    You can install the necessary Python packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run

1. **Run the Streamlit app**:

    After setting up everything, you can start the app by running the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

2. **Upload a PDF/DOCX File or Enter Text**:

    - Use the sidebar to upload a PDF or DOCX file. The app will automatically extract text and convert it to speech.
    - Alternatively, enter text in the provided text area, and it will be converted to speech when you click the "Convert to Speech" button.

---

## Contact me

email - natnaelm5552@gmail.com

