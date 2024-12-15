import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from modules.speech_to_text.speech_to_text import SpeechToText

def main():
    stt = SpeechToText()
    
    while True:
        try:
            print("\nStarting new recording session...")
            text = stt.listen_and_convert()
            print(f"Recognized text: {text}")
            
            if text.lower() in ['quit', 'exit', 'stop']:
                print("Exiting program...")
                break
                
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
            break

if __name__ == "__main__":
    main()