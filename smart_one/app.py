from smart_one.core.ai import AI

import socket

is_online = lambda: socket.gethostbyname(socket.gethostname()) != "127.0.0.1"

jarvis = AI()


def run():
    respond: str = ""
    query: str = ""
    jarvis.greeting()
    while True:
        event, values = jarvis.gui.read()
        if jarvis.gui.check_exit(event):
            break
        jarvis.online = is_online()
        jarvis.gui.update_value(jarvis.gui.NET,
                                "Online" if jarvis.online else "Offline")

        if event == jarvis.gui.SEND:
            query = values[jarvis.gui.QUERY]
            jarvis.gui.update_value(jarvis.gui.QUERY, "")

        if event == jarvis.gui.LISTEN:
            jarvis.change_cmd_mode()
            if jarvis.listening:
                jarvis.speak("I'm listening sir.")
                query = jarvis.listen()
                jarvis.gui.update_value(jarvis.gui.STATUS, "Recognizing")
                jarvis.change_cmd_mode()

        if event == jarvis.gui.SAVE:
            jarvis.save_conversation()

        if event == jarvis.gui.PRINT:
            jarvis.save_conversation()

        if event == jarvis.gui.CLEAR:
            jarvis.gui.clear_screen()

        if query:
            respond = jarvis.get_ai_respond(query)

        if respond:
            jarvis.gui.print(query, respond, jarvis.name)
            jarvis.speak(respond)
        respond = ""
        query = ""

    jarvis.terminate_program()