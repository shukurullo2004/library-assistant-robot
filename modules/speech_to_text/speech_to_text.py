import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_and_convert(self):
        """
        Listen to audio input and convert it to text
        Returns: str - transcribed text or error message
        """
        with self.microphone as source:
            print("Listening... Speak now!")

            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
        try:
            print("Processing speech...")
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.RequestError:
            return "API unavailable"
        except sr.UnknownValueError:
            return "Unable to recognize speech"
        except Exception as e:
            return f"Error: {str(e)}"