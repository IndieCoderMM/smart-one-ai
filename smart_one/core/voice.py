from smart_one.utils.settings import SPEECH_RATE, GENDER
import pyttsx3


class Voice:

    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.gender = 0 if GENDER == "male" else 2
        self.engine.setProperty("rate", SPEECH_RATE)
        self.engine.setProperty("volumen", 1.0)
        available_voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", available_voices[self.gender].id)

    def speak(self, message: str):
        self.engine.say(message)
        self.engine.runAndWait()