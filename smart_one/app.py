from smart_one.core.ai import AI
from smart_one.utils.constants import CmdMode

mavis = AI()


def run():
    respond: str = ""
    query: str = ""
    mavis.greeting()
    while True:
        event, values = mavis.gui.read()
        if mavis.gui.check_exit(event):
            break

        if event == "ENTER":
            query = values["-REQUEST-"]

        if query:
            respond = mavis.get_ai_respond(query)
            query = ""

        if respond:
            mavis.gui["-OUTPUT-"].update(respond)
            mavis.speak(respond)
            respond = ""

    mavis.terminate_program()