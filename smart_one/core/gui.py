import PySimpleGUI as sg


class Gui(sg.Window):
    SEND = "Send"
    PROMPT_KEY = "-PROMPT-"
    REQUEST_KEY = "-REQUEST-"
    OUTPUT_KEY = "-OUTPUT-"
    AI_GIF = "./database/assets/ai-assistant.gif"

    def __init__(self, title, theme, minimal):
        sg.theme(theme)
        self.layout = self.get_minimal_layout(
        ) if minimal else self.get_layout()
        super().__init__(title,
                         self.layout,
                         return_keyboard_events=True,
                         keep_on_top=True)

    def get_minimal_layout(self):
        layout = [
            # [sg.Image(source=self.AI_GIF, key="-GIF-")],
            [
                sg.Input(
                    size=(40, 2),
                    key=self.REQUEST_KEY,
                    focus=True,
                    font="Consolas 18",
                    expand_x=True,
                ),
                sg.Button(
                    self.SEND,
                    size=(5, 1),
                    font="Helvetica 20",
                    button_color=(sg.YELLOWS[0], sg.BLUES[0]),
                    bind_return_key=True,
                    visible=False,
                ),
            ],
        ]
        return layout

    def get_layout(self):
        layout = [
            [
                sg.Multiline(size=(30, 10),
                             font="Helvetica 25",
                             echo_stdout_stderr=False,
                             reroute_stdout=False,
                             autoscroll=True,
                             auto_size_text=True,
                             key=self.OUTPUT_KEY)
            ],
            [
                sg.Input(
                    expand_x=True,
                    key=self.REQUEST_KEY,
                    focus=True,
                    font="Consolas 18",
                ),
                sg.Button(
                    self.SEND,
                    font="Helvetica 20",
                    size=(6, 1),
                    expand_x=True,
                    button_color=(sg.YELLOWS[0], sg.BLUES[0]),
                    bind_return_key=True,
                    visible=False,
                ),
            ],
        ]
        return layout

    @staticmethod
    def check_exit(event):
        return event == sg.WIN_CLOSED

    @staticmethod
    def print_output(message):
        sg.PopupOK(
            message,
            keep_on_top=True,
            no_titlebar=True,
            font=("Comic Sans Ms", 20),
            line_width=50,
        )

    @staticmethod
    def get_confirm(prompt):
        # choice,_ = sg.Window(title, [[sg.T(prompt)], [sg.Yes(s=10), sg.No(s=10)]],disable_close=True).read(close=True)
        return (sg.PopupOKCancel(
            prompt,
            no_titlebar=True,
            line_width=20,
            font="Consolas 20",
            keep_on_top=True,
        ) == "OK")