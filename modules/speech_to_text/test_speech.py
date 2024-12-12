
from modules.stt.speech_to_text import SpeechToText

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