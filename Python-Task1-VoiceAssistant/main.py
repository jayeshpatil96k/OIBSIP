import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except Exception:
        speak("Sorry, I didn't understand. Please repeat.")
        return ""

def process_command(command):

    if "hello" in command:
        speak("Hello Jayesh! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "open youtube" in command:
         speak("Opening YouTube")
         webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open github" in command:
         speak("Opening GitHub")
         webbrowser.open("https://github.com")

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching for {query}")
        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I can only help with hello, date, time, and search commands.")

    return True


speak("Voice Assistant Started.")

while True:
    command = take_command()

    if command:
        if not process_command(command):
            break
