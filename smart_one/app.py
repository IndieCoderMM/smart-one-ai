from smart_one.core.ai import AI
from smart_one.utils.constants import Status, Command
import keyboard

mavis = AI()


def run():
    mavis.greeting()
    response = None

    while True:
        if keyboard.is_pressed("x"):
            break

        if keyboard.is_pressed("space"):
            if mavis.status == Status.OFFLINE:
                continue
            query = mavis.listen()
            if query == "exit":
                break
            if query == "":
                continue

            response = mavis.get_ai_respond(query)
            mavis.speak(response)

        if keyboard.is_pressed("p"):
            if response:
                mavis.speak("I'm printing on the screen...")
                mavis.print_output(response)

        if keyboard.is_pressed("o"):
            if mavis.status == Status.OFFLINE:
                mavis.status = Status.ONLINE
                mavis.speak("I'm ONLINE.")
                continue
            if mavis.ask_permission(
                    "Sir,  Do you want me to work in offline mode?",
                    "Confirm?"):
                mavis.go_offline_mode()
                mavis.speak("I'm switching to OFFLINE mode.")

    mavis.terminate_program()