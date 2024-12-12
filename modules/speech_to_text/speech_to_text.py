
import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_and_convert(self):
        """
        Listen to audio input and convert it to text
        Returns: str - transcribed text or error message
        """
        try:
            with sr.Microphone() as source:
                print("Listening... Speak now!")
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Listen for audio input
                audio = self.recognizer.listen(source)
                
                print("Processing speech...")
                # Convert speech to text using Google's speech recognition
                text = self.recognizer.recognize_google(audio)
                return text
        except sr.RequestError:
            return "Error: Could not connect to speech recognition service"
        except sr.UnknownValueError:
            return "Error: Could not understand audio"
        except Exception as e:
            return f"Error: {str(e)}"