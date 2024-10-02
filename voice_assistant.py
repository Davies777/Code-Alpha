
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import os

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose a different voice (0 for male, 1 for female)
engine.setProperty('rate', 150)  # Set speech speed

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input from the user."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Network error.")
        return "None"
    return query.lower()

def greet_user():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def execute_task(query):
    """Execute the task based on the voice command."""
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "time" in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {str_time}")

    elif "open code" in query:
        code_path = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif "send email" in query:
        # Add email sending functionality here
        speak("Sorry, I cannot send emails right now.")

    else:
        speak("I don't know how to do that yet, but I'm learning!")

# Main function
def main():
    greet_user()
    speak("How can I assist you today?")
    
    while True:
        query = listen()

        if query == "none":
            continue
        
        if "exit" in query or "stop" in query:
            speak("Goodbye!")
            break
        
        # Execute tasks based on the query
        execute_task(query)

# Run the assistant
if __name__ == "__main__":
    main()
