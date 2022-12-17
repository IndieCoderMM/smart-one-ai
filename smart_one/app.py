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
        event, values = mavis.gui.read()
        if mavis.gui.check_exit(event):
            break
        if event == "-CHANGE-MODE-":
            mode = "Text" if mavis.gui["-MODE-"].get() == "Voice" else "Voice"
            mavis.gui["-MODE-"].update(mode)
        if event == "-SHOW-CMD-":
            mavis.gui.print_output("exit; save; sleep;")
        if event == "ENTER":
            query = values["-REQUEST-"]
            mavis.gui["-REQUEST-"].update("")
            respond = mavis.get_ai_respond(query)
            mavis.gui["-OUTPUT-"].update("")
            print(respond)
            mavis.speak(respond)

    mavis.terminate_program()