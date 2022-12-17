import PySimpleGUI as sg

SEND = "-ENTER-"
PROMPT_KEY = "-PROMPT-"
REQUEST_KEY = "-REQUEST-"
OUTPUT_KEY = "-OUTPUT-"


class Gui(sg.Window):

    def __init__(self, title):
        sg.theme("DarkBlue")
        self.layout = self.get_layout()
        super().__init__(title,
                         self.layout,
                         return_keyboard_events=True,
                         keep_on_top=True,
                         no_titlebar=True,
                         grab_anywhere=True)

    def get_dashboard(self):
        col = sg.Column([[
            sg.Text("Status: "),
            sg.Text("Standby", key="-STATUS-", size=(6, 1))
        ], [sg.Text("Network: "),
            sg.Text("Online", key="-NET-", size=(6, 1))],
                         [
                             sg.Text("CMD Mode: "),
                             sg.Text("Voice", key="-MODE-", size=(6, 1))
                         ]])
        return col

    def get_layout(self):
        col = self.get_dashboard()
        layout = [[
            sg.Multiline(size=(30, 10),
                         font="Helvetica 18",
                         echo_stdout_stderr=False,
                         reroute_stdout=True,
                         autoscroll=True,
                         auto_size_text=True,
                         key=OUTPUT_KEY), col
        ],
                  [
                      sg.Input(
                          expand_x=True,
                          key=REQUEST_KEY,
                          focus=True,
                          font="Consolas 18",
                      ),
                      sg.Button(
                          "ENTER",
                          font="Helvetica 14",
                          expand_x=True,
                          button_color="YELLOW on BLUE",
                          bind_return_key=True,
                          visible=True,
                      ),
                  ],
                  [
                      sg.Button("CMD", key="-SHOW-CMD-"),
                      sg.Button("Sound On", key="-SOUND-"),
                      sg.Button("Print", key="-PRINT-"),
                      sg.Button("Mic", key="-CHANGE-MODE-"),
                      sg.Button("Close",
                                button_color="YELLOW on RED",
                                size=(6, 1))
                  ]]
        return layout

    @staticmethod
    def check_exit(event):
        return event == sg.WIN_CLOSED or event == "Close"

    @staticmethod
    def print_output(message):
        sg.PopupOK(
            message,
            keep_on_top=True,
            no_titlebar=True,
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


if __name__ == "__main__":
    gui = Gui("Test Window")
    while True:
        event, values = gui.read()
        if gui.check_exit(event):
            break
        if event == "-CHANGE-MODE-":
            mode = "Text" if gui["-MODE-"].get() == "Voice" else "Voice"
            gui["-MODE-"].update(mode)
        if event == "-SHOW-CMD-":
            gui.print_output("exit; save; sleep;")
