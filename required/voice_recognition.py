
import speech_recognition as sr

def get_voice_input(input_text=""):
    r = sr.Recognizer()
    print(input_text)
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        recognized_text = r.recognize_google(audio)
        print(f"User said: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


def main(input_text=""):
    return get_voice_input(input_text)