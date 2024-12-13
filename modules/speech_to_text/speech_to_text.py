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
            return self.process_command(text)
        except sr.RequestError:
            return "API unavailable"
        except sr.UnknownValueError:
            return "Unable to recognize speech. Can you repeat?"
        except Exception as e:
            return f"Error: {str(e)}"

    def process_command(self, text):
        """
        Process the recognized text and map it to TurtleBot commands
        Returns: str - response based on the command
        """
        commands = {
            "turn right": "Turning right",
            "turn left": "Turning left",
            "move forward": "Moving forward",
            "move backward": "Moving backward",
            "stop": "Stopping"
        }

        for command, response in commands.items():
            if command in text.lower():
                return response

        return "Command not recognized. Can you repeat?"

# Example usage
if __name__ == "__main__":
    stt = SpeechToText()
    print(stt.listen_and_convert())