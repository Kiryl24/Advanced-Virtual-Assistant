#install ffmpeg
#install pip auto-py-to-exe
#install py_audio just in case, and setuptools
import speech_recognition as sr
from gtts import gTTS
import winsound
import pyautogui
import webbrowser
from pydub import AudioSegment
import datetime
import random
import re
import pyjokes

def tell_joke():
    joke = pyjokes.get_joke()
    respond(joke)

def extract_numbers(command):
    numbers = re.findall(r'\d+', command)
    return [int(num) for num in numbers]
def perform_calculation(command):
    numbers = extract_numbers(command)
    if "+" in command:
        result = sum(numbers)
    elif "-" in command:
        result = numbers[0] - sum(numbers[1:])
    elif "*" in command:
        result = 1
        for num in numbers:
            result *= num
    elif "/" in command:
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    else:
        respond("Sorry, I can only perform addition, subtraction, multiplication, and division.")
        return
    respond(f"The result is {result}.")
def choose_response(responses):
    return random.choice(responses)


def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None


def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)


def search_on_google(query):
    webbrowser.open("https://www.google.com/search?q=" + query)


def main():
    listeningToTask = False
    while True:
        command = listen_for_command()
        print("Command recognized:", command)

        triggerKeyword = "ava"
        if command and triggerKeyword in command.lower():
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond(f"Adding {command} to your task list. You have {len(tasks)} currently in your list.")
            elif "add a task" in command:
                listeningToTask = True
                respond("Sure, what is the task?")
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "take a screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("Screenshot has been taken.")
            elif "capture screen" in command:
                pyautogui.screenshot("screenshot.png")
                respond("Screenshot has been taken.")
            elif "open browser" in command:
                respond("Opening browser.")
                webbrowser.open("http://www.google.com")
            elif "open internet" in command:
                respond("Opening browser.")
                webbrowser.open("http://www.google.com")
            elif "open youtube" in command.lower():
                respond("Opening YouTube")
                webbrowser.open("https://www.youtube.com/")
            elif "hello" in command:
                respond("Hello, how can I help you?")
            elif "who is your creator" in command:
                respond("His name is Jackob, rest is classified")
            elif "terminate" in command:
                respond("Goodbye!")
                break
            elif "time" in command.lower():
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M")
                respond(f"The current time is {current_time}.")
            elif "what are you" in command.lower():
                respond("I am Advanced Virtual Assistant, I'm here to help you and ease your computer usage.")
            elif "give me more information about your creator" in command.lower():
                respond("Sorry, these are classified informations.")
            elif "what Ava stands for" in command.lower():
                respond("Advanced Virtual Assistant.")
            elif "what is Ava" in command.lower():
                respond("Advanced Virtual Assistant.")
            elif "search for" in command.lower() and "on google" in command.lower():
                query = command.lower().replace("ava search for", "").replace("on google", "")
                search_on_google(query.strip())
            elif "calculate" in command.lower():
                perform_calculation(command)
            elif "roll" in command.lower():
                number = random.randint(1, 5)
                respond(str(number))
            elif "joke" in command.lower():
                respond(tell_joke())
            else:
                print("I'm sorry, I do not understand")

if __name__ == "__main__":
    tasks = []
    respond("AVA is initializing")
    respond("AVA is ready")
    respond("Hello User")
    main()