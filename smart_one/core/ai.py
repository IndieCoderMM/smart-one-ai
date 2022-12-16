from smart_one.core.gui import Gui
from smart_one.core.voice import Voice
from smart_one.core.recognizer import Recognizer
from smart_one.core.memory import load_memory
from smart_one.utils.openai_helper import get_openai_respond
from smart_one.utils.constants import Status, Command
from smart_one.utils.settings import MEMORY_PATH, NAME, SPEECH_RATE, GENDER

from datetime import datetime


class AI:

    def __init__(self):
        self.name = NAME
        self.status = Status.ONLINE
        self.command = Command.VOICE

        self.gui = Gui(self.name, "Python", True)
        self.voice = Voice()
        self.recognizer = Recognizer()
        self.prompt = load_memory(MEMORY_PATH)

    def get_ai_respond(self, query: str) -> str:
        prompt = f"\nYou: {query}\n{self.name}: "
        self.prompt += prompt
        try:
            respond = get_openai_respond(self.prompt).lstrip()
            self.prompt += respond
        except Exception as e:
            print(e)
            respond = "Please wait sir, I'm connecting to the server..."
        return respond

    def greeting(self):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            self.speak("Good Morning sir")
        elif 12 <= hour < 16:
            self.speak("Good Afternoon sir")
        else:
            self.speak("Good Evening sir")
        self.speak("I'm online. How can I help you?")

    def terminate_program(self):
        self.speak("I'm closing the program.")
        self.gui.close()

    def speak(self, message: str):
        self.voice.speak(message)

    def listen(self) -> str:
        self.recognizer.listen()

    def print_output(self, text: str):
        self.gui.print_output(text)

    # def save_memory(self):
    #     with open(self.data_file, "w") as file:
    #         file.write(self.prompt)

    # def ask_permission(self, question: str, title: str):
    #     self.speak(question)
    #     return self.gui.get_confirm(title)

    # def confirm_save(self):
    #     ans = self.ask_permission("Do you want me to save this conversation?",
    #                               "Confirm Save?")
    #     if ans:
    #         self.save_memory()
    #         self.speak("Saving the file...")
    #     else:
    #         self.speak("Deleting history...")

    # def take_text_command(self) -> str:
    #     event, values = self.gui.read(timeout=100)
    #     if self.gui.check_exit(event):
    #         return "exit"
    #     if event == self.gui.SEND:
    #         self.gui[self.gui.REQUEST_KEY].update("")
    #         query = values[self.gui.REQUEST_KEY]
    #         return query
    #     return ""
