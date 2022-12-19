from smart_one.core.gui import Gui
from smart_one.core.voice import Voice
from smart_one.core.recognizer import Recognizer
from smart_one.core.memory import load_memory, save_memory
from smart_one.utils.openai_helper import get_openai_respond
from smart_one.utils.settings import NAME, SPEECH_RATE, GENDER
from smart_one.utils.constants import CmdMode


class AI:

    def __init__(self):
        self.name = NAME

        self.gui = Gui("Smart One A.I.")
        self.voice = Voice()
        self.recognizer = Recognizer()
        self.prompt = load_memory()
        self.mode = CmdMode.TEXT

    def get_ai_respond(self, query: str) -> str:
        prompt = f"\nYou: {query}\n{self.name}: "
        self.prompt += prompt
        try:
            respond = get_openai_respond(self.prompt).lstrip()
            self.prompt += respond
        except Exception as e:
            respond = "Sir, "
        return respond

    def greeting(self):
        self.speak(f"Hello sir, I'm {self.name}")
        # self.speak("You can ask me anything and I will try my best to answer.")
        # self.speak(
        #     "If you want to use voice command, press SPACE BAR on your keyboard."
        # )

    def terminate_program(self):
        self.speak("See you sir")
        self.gui.close()

    def speak(self, message: str):
        self.voice.speak(message)

    def listen(self) -> str:
        return self.recognizer.listen()

    def change_cmd_mode(self):
        self.mode = CmdMode.VOICE if self.mode == CmdMode.TEXT else CmdMode.TEXT
        mode = "Voice Input" if self.mode == CmdMode.VOICE else "Text Input"
        status = "Listening" if self.mode == CmdMode.VOICE else "Standby"
        self.gui.update(self.gui.MODE, mode)
        self.gui.update(self.gui.STATUS, status)

    def save_conversation(self):
        if len(self.prompt) > 1500:
            self.speak(
                "Sir, I can't save the conversation. My memory is full.")
            return False
        save_memory(self.prompt)
        self.speak("Alright sir, I added this conversation to my memory.")

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
