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
    MODE = "-MODE-"
    OUTPUT = "-OUTPUT-"
    NET = "-NET-"
    CHANGE_CMD = "-CHANGE-CMD-"
    CLEAR = "-CLEAR-"
    SEND = "-SEND-"
    SAVE = "-SAVE-"

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
            sg.Text("Standby",
                    key=self.STATUS,
                    size=(10, 1),
                    text_color=LIGHTGREEN)
        ],
                         [
                             sg.Text("Network: "),
                             sg.Text("Online",
                                     key=self.NET,
                                     size=(10, 1),
                                     text_color=LIGHTGREEN)
                         ],
                         [
                             sg.Text("CMD Mode: "),
                             sg.Text("Text",
                                     key=self.MODE,
                                     size=(10, 1),
                                     text_color=LIGHTGREEN)
                         ]])
        return col

    def get_layout(self):
        col = self.get_dashboard()
        layout = [[
            sg.Multiline(size=(40, 10),
                         font="Consolas 15",
                         autoscroll=True,
                         auto_size_text=True,
                         pad=(2, 1),
                         key=self.OUTPUT,
                         disabled=True,
                         background_color=INDIGO,
                         text_color=WHITE), col
        ],
                  [
                      sg.Input(expand_x=True,
                               key=self.QUERY,
                               focus=True,
                               font="Consolas 14"),
                      sg.Button(
                          "Send",
                          key=self.SEND,
                          expand_x=True,
                          bind_return_key=True,
                          visible=False,
                      ),
                  ],
                  [
                      sg.Button("Clear", key=self.CLEAR, expand_x=True),
                      sg.Button("Save", key=self.SAVE, expand_x=True),
                      sg.Button("Save", key="-PRINT-", expand_x=True),
                      sg.Button("Voice Cmd",
                                key=self.CHANGE_CMD,
                                expand_x=True),
                      sg.Button("Close", expand_x=True)
                  ]]
        return layout

    @staticmethod
    def check_exit(event):
        return event == sg.WIN_CLOSED or event == "Close"

    @staticmethod
    def show_popup(message):
        sg.PopupOK(
            message,
            keep_on_top=True,
            no_titlebar=True,
        )

    @staticmethod
    def get_confirm(prompt):
        return (sg.PopupOKCancel(
            prompt,
            no_titlebar=True,
            line_width=20,
            font="Consolas 20",
            keep_on_top=True,
        ) == "OK")

    def update(self, key, text):
        self[key].update(text)
        self.refresh()

    def print(self, query, respond, ai_name):
        conversation = self[self.OUTPUT].get()
        conversation += f"\n$You: {query}\n${ai_name}: {respond}"
        self.update(self.OUTPUT, conversation)
