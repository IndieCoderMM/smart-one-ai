from smart_one.core.engine import AI, Status, Command
import keyboard

mavis = AI("Mavis", "database/mavis_data.txt")


def run():
    mavis.init_gui('DarkPurple4')
    mavis.init_voice_engine(190, 2)
    mavis.greeting()
    response = None
    while True:
        if mavis.command == Command.TEXT:
            query = mavis.take_text_command()
            if query == "":
                continue
            if query == "exit":
                break
            response = mavis.get_ai_respond(query)
            mavis.speak(response)

        if keyboard.is_pressed("space"):
            if mavis.status == Status.OFFLINE:
                continue
            query = mavis.listen_voice_command()
            if query == "exit":
                break
            if query == "":
                continue

            response = mavis.get_ai_respond(query)
            mavis.speak(response)

        if keyboard.is_pressed("p"):
            if response:
                mavis.speak("I'm printing on the screen...")
                mavis.print_on_screen(response)

        if keyboard.is_pressed("c"):
            if mavis.ask_permission(
                    "Sir, do you want to change command method?",
                    "Change Command Mode?"):
                mavis.command = Command.TEXT if mavis.command == Command.VOICE else Command.VOICE
                mavis.speak(
                    f"Ok Sir, you can use {'voice' if mavis.command==Command.VOICE else 'text'} command now'"
                )

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


if __name__ == "__main__":
    run()