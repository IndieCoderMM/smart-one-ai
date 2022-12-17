import PySimpleGUI as sg

GREEN = "#16A085"
LIGHTGREEN = "#27AE60"
LIGHTBLUE = "#3498DB"
DARK = "#2C3E50"
WHITE = "#ECF0F1"
BLUE = "#2980B9"
PURPLE = "#8E44AD"
YELLOW = "#F1C40f"
INDIGO = "#3F51B5"

theme_dict = {
    'BACKGROUND': DARK,
    'TEXT': YELLOW,
    'INPUT': YELLOW,
    'TEXT_INPUT': "BLACK",
    'SCROLL': BLUE,
    'BUTTON': (WHITE, GREEN),
    'PROGRESS': (WHITE, BLUE),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

sg.theme_add_new('custom', theme_dict)
sg.theme('custom')

sg.set_options(font="Tahoma 17")


class Gui(sg.Window):
    STATUS = "-STATUS-"
    QUERY = "-QUERY-"
    OUTPUT = "-OUTPUT-"
    NET = "-NET-"

    def __init__(self, title):

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
            sg.Text("Standby", key=self.STATUS, size=(10, 1))
        ], [
            sg.Text("Network: "),
            sg.Text("Online", key=self.NET, size=(10, 1))
        ], [
            sg.Text("CMD Mode: "),
            sg.Text("Voice", key="-MODE-", size=(10, 1))
        ]])
        return col

    def get_layout(self):
        col = self.get_dashboard()
        layout = [[
            sg.Multiline(size=(30, 10),
                         font="Helvetica 18",
                         autoscroll=True,
                         auto_size_text=True,
                         pad=(1, 1),
                         key=self.OUTPUT,
                         disabled=True,
                         background_color=INDIGO,
                         text_color=WHITE), col
        ],
                  [
                      sg.Input(expand_x=True, key=self.QUERY, focus=True),
                      sg.Button(
                          "ENTER",
                          font="Helvetica 14",
                          expand_x=True,
                          bind_return_key=True,
                          visible=True,
                      ),
                  ],
                  [
                      sg.Button("CMD", key="-SHOW-CMD-", expand_x=True),
                      sg.Button("Sound On", key="-SOUND-", expand_x=True),
                      sg.Button("Print", key="-PRINT-", expand_x=True),
                      sg.Button("Mic", key="-CHANGE-MODE-", expand_x=True),
                      sg.Button("Close", expand_x=True)
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

    def update(self, key, text):
        self[key].update(text)


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
