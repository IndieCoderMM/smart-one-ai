from smart_one.core.gui import Gui
from smart_one.core.voice import Voice
from smart_one.core.recognizer import Recognizer
from smart_one.core.memory import load_memory
from smart_one.utils.openai_helper import get_openai_respond
from smart_one.utils.settings import NAME, SPEECH_RATE, GENDER


class AI:

    def __init__(self):
        self.name = NAME

        self.gui = Gui("Smart One A.I.")
        self.voice = Voice()
        self.recognizer = Recognizer()
        self.prompt = load_memory()

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
