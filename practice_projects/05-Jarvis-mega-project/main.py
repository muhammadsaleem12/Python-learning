import os
from dotenv import load_dotenv
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from client import ask_ai


recognizer = sr.Recognizer()

load_dotenv()

newsapi = os.getenv("NEWS_API_KEY")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()




def processCommand(c):
    if "open google" in c.lower():
        print("Opening Google...")
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        print("Opening YouTube...")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        print("Opening LinkedIn...")
        webbrowser.open("https://linkedin.com")

    elif "open facebook" in c.lower():
        print("Opening Facebook...")
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        print("Opening Instagram...")
        webbrowser.open("https://instagram.com")

    elif "open gpt" in c.lower():
        print("Opening Chatgpt...")
        webbrowser.open("https://chatgpt.com")

    elif c.lower().startswith("play"):
        print("Playing music...")
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # NEWS Section

    elif "news" in c.lower():
        print("Getting the latest news...")

        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        )

        if r.status_code == 200:
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            print("Reading the latest headlines...")

            for article in articles:
                speak(article['title'])

    else:
        # Let AI handle the request
        print("Thinking...")
        response = ask_ai(c)

        print("Speaking...")
        speak(response)




if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        # Listen for the wake word "Jarvis"
        r = sr.Recognizer()

        print("recognizing....")

        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes Sir")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.WaitTimeoutError:
            print("I didn't hear anything.")

        except sr.UnknownValueError:
            print("I couldn't understand that.")

        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")