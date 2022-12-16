from core.gui import Gui
from core.openai_helper import get_ai_respond
from datetime import datetime
from enum import Enum

import speech_recognition as sr
import pyttsx3

MAX_TOKEN = 2000


class Status(Enum):
    ONLINE = 0
    OFFLINE = 1


class Command(Enum):
    VOICE = 0
    TEXT = 1


class AI:

    def __init__(self, name, data):
        self.gui = None
        self.voice = None
        self.chat_engine = None
        self.conversations = []
        self.name = name
        self.data_file = data
        self.status = Status.ONLINE
        self.command = Command.VOICE
        self.data_size = 0
        self.prompt = self.load_memory()

    def listen_voice_command(self) -> str:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        query = ""
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-us")
            print(query)
            if "sleep" in query:
                if datetime.now().hour >= 21:
                    self.speak("Good night Sir")
                else:
                    self.speak("Have a nice day Sir")
                query = "exit"
            elif "hello" in query:
                self.speak("How may I help you?")
        except sr.RequestError:
            self.speak("I'm connecting to the server.")
        except Exception as e:
            self.speak("Sir, I don't understand that.")
            print(e)
        return query

    def get_ai_respond(self, query: str) -> str:
        prompt = f"\nYou: {query}\n{self.name}: "
        self.prompt += prompt
        try:
            respond = get_openai_complete(self.prompt).lstrip()
            self.prompt += respond
        except Exception as e:
            print(e)
            respond = "Please wait sir, I'm connecting to the server..."
        return respond

    def load_memory(self) -> str:
        prompt = ""
        with open(self.data_file) as memory:
            for line in memory:
                self.data_size += len(line.split())
                if self.data_size > MAX_TOKEN:
                    break
                prompt += line
        return prompt

    def init_gui(self, theme: str = "Python", minimal: bool = True):
        self.gui = Gui(self.name, theme, minimal)

    def init_voice_engine(self, rate: int, vid: int):
        self.voice = pyttsx3.init("sapi5")
        self.voice.setProperty("rate", rate)
        self.voice.setProperty("volume", 1.0)
        voices = self.voice.getProperty("voices")
        self.voice.setProperty("voice", voices[vid].id)

    def greeting(self):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            self.speak("Good Morning sir")
        elif 12 <= hour < 16:
            self.speak("Good Afternoon sir")
        else:
            self.speak("Good Evening sir")
        self.speak("I'm online. How can I help you?")

    def speak(self, text: str):
        self.voice.say(text)
        self.voice.runAndWait()

    def get_chat_respond(self, prompt: str) -> str:
        respond = self.chat_engine.get_response(prompt)
        return respond

    def save_memory(self):
        with open(self.data_file, "w") as file:
            file.write(self.prompt)

    def ask_permission(self, question: str, title: str):
        self.speak(question)
        return self.gui.get_confirm(title)

    def confirm_save(self):
        ans = self.ask_permission("Do you want me to save this conversation?",
                                  "Confirm Save?")
        if ans:
            self.save_memory()
            self.speak("Saving the file...")
        else:
            self.speak("Deleting history...")

    def terminate_program(self):
        if len(self.prompt.split()) > self.data_size:
            self.confirm_save()
        self.speak("I'm closing the program.")
        self.gui.close()

    def take_text_command(self) -> str:
        event, values = self.gui.read(timeout=100)
        if self.gui.check_exit(event):
            return "exit"
        if event == self.gui.SEND:
            self.gui[self.gui.REQUEST_KEY].update("")
            query = values[self.gui.REQUEST_KEY]
            return query
        return ""

    def print_on_screen(self, text: str):
        self.gui.print_output(text)

    def get_chat_history(self):
        conversations = []
        with open(self.data_file) as memory:
            for line in memory:
                if ":" not in line or len(line) < 10:
                    continue
                conversations.append(line.lstrip())
        return conversations

    def go_offline_mode(self):
        self.status = Status.OFFLINE
        self.chat_engine = ChatBot(self.name)
