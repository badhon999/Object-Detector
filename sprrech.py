# Install required libraries
!pip install SpeechRecognition pydub

# Import necessary libraries
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

def recognize_speech_from_file(audio_path):
    recognizer = sr.Recognizer()

    # Load the audio file
    audio = AudioSegment.from_file(audio_path)

    # Convert stereo to mono (if needed)
    if audio.channels == 2:
        audio = audio.set_channels(1)

    # Export the audio file back to WAV format (required by SpeechRecognition)
    audio.export("mono_audio.wav", format="wav")

    with sr.AudioFile("mono_audio.wav") as source:
        print("Recognizing...")
        audio_data = recognizer.record(source)

        try:
            # Use the Google Web Speech API to convert audio to text
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error making the request to Google Speech Recognition service; {e}")

# Upload an audio file to Colab
from google.colab import files
uploaded = files.upload()

# Get the uploaded file path
audio_path = next(iter(uploaded))

# Perform speech recognition on the uploaded file
recognize_speech_from_file(audio_path)