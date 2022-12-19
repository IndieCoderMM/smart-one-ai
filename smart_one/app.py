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

        if event == mavis.gui.SEND:
            query = values[mavis.gui.QUERY]
            mavis.gui.update(mavis.gui.QUERY, "")

        if event == mavis.gui.CHANGE_CMD:
            mavis.change_cmd_mode()
            if mavis.mode == CmdMode.VOICE:
                mavis.speak("I'm listening sir.")
                query = mavis.listen()
                mavis.gui.update(mavis.gui.STATUS, "Recognizing")
                mavis.change_cmd_mode()

        if event == mavis.gui.SAVE:
            mavis.save_conversation()

        if event == mavis.gui.CLEAR:
            mavis.clear_conversation()

        if query:
            respond = mavis.get_ai_respond(query)

        if respond:
            mavis.gui.print(query, respond, mavis.name)
            mavis.speak(respond)
        respond = ""
        query = ""

    mavis.terminate_program()