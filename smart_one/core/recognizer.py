import speech_recognition as sr


class Recognizer:
    LANG = "en-us"

    def __init__(self):
        self.engine = sr.Recognizer()
        self.mic = sr.Microphone()
        self.engine.pause_threshold = 1

    def listen(self) -> str:
        with self.mic as source:
            print("Listening...")
            audio = self.engine.listen(source)

        query: str = ""
        try:
            print("Recognizing...")
            query = self.engine.recognize_google(audio, language=self.LANG)
            print(query)
        except sr.RequestError:
            print("Request error!")
        except Exception as e:
            print(e)

        return query
