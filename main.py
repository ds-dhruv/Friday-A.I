import speech_recognition as sr
import os
import webbrowser
import win32com.client
import openai
from pyttsx3 import speak

from config import apikey
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Dhruv: {query}\n Friday: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def speaker(text):
    os.system(f'speak "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Friday"

if __name__ == '__main__':
    print('Welcome to Friday A.I')
    speak("Friday A.I meinn aapkaa swagat hain")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["facebook", "https://www.facebook.com"], ["instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"start {site[0]}".lower() in query.lower():
                speaker(f"Starting {site[0]} sir...")
                webbrowser.open(site[1])

        # todo: Add a feature to play a specific song
        songs = [["Thunder", "C:/Users/hp/Desktop/Music/Thunder.mp3"], ["Starboy", "C:/Users/hp/Desktop/Music/Starboy.mp3"],
                 ["cupid", "C:/Users/hp/Desktop/Music/cupid.mp3"], ["Blinding Lights", "C:/Users/hp/Desktop/Music/BlindingLights.mp3"],
                 ["Sickick", "C:/Users/hp/Desktop/Music/Sickick.mp3"]]
        for song in songs:
            if f"start {song[0]}".lower() in query.lower():
                musicPath = {song[0]}
                os.system(f"start {musicPath}")

        if "the time" in query:
            musicPath = "C:/Users/Vikas/Desktop/Music"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker(f"Sir time is {hour} bajke {min} minutes")

        elif "start camera".lower() in query.lower():
            path = "C:/Users/hp/Desktop/Camera"
            os.system(f"start {path}")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Friday Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





        # say(query)
