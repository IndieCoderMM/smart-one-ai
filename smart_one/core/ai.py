from smart_one.core.gui import Gui
from smart_one.core.voice import Voice
from smart_one.core.recognizer import Recognizer
from smart_one.core.memory import load_memory, save_memory
from smart_one.utils.openai_helper import get_openai_respond
from smart_one.utils.settings import USER, NAME, SPEECH_RATE, GENDER


class AI:

    def __init__(self):
        self.name = NAME
        self.gui = Gui("Smart One A.I.")
        self.voice = Voice()
        self.recognizer = Recognizer()
        self.memory = load_memory()
        self.prompt = ""
        self.listening = False
        self.online = False

    def get_ai_respond(self, query: str) -> str:
        """Get respond from openAI

        Args:
            query (str): User input

        Returns:
            str: AI respond
        """
        prompt = f"\n{USER}: {query}\n{self.name}: "
        self.prompt += prompt
        try:
            respond = get_openai_respond(self.memory + self.prompt).lstrip()
            self.prompt += respond
        except Exception as e:
            respond = "Sir, I can't connect to the server right now."
        return respond

    def greeting(self):
        self.speak(f"Hello sir, I'm {self.name}")
        # self.speak("You can ask me anything and I will try my best to answer.")

    def terminate_program(self):
        self.gui.close()

    def speak(self, message: str):
        self.voice.speak(message)

    def listen(self) -> str:
        return self.recognizer.listen()

    def change_cmd_mode(self):
        self.listening = not self.listening
        mode = "Voice" if self.listening else "Text"
        status = "Listening" if self.listening else "Standby"
        self.gui.update_value(self.gui.MODE, mode)
        self.gui.update_value(self.gui.STATUS, status)

    def save_to_memory(self):
        if len(self.memory + self.prompt) > 1000:
            self.speak(
                "Sir, I can't save the conversation. My memory is full.")
            self.speak("But I can print the file for you.")
            return False
        save_memory(self.memory + self.prompt)
        self.speak("Alright sir, I added this conversation to my memory.")

    def print_conversation(self):
        with open("smart_one/data/saved_result.txt", "w") as file:
            file.write(self.prompt)
        self.speak("Ok sir, I saved this conversation to my data folder.")