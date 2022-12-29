from smart_one.utils.settings import NAME

import PySimpleGUI as sg

WHITE = "#ecf0f1"
LIGHTBLUE = "#0dcca1"
DARK = "#000000"
GREEN = "#65dc98"
TEAL = "#096a59"
INDIGO = "#7700a6"

theme_dict = {
    'BACKGROUND': DARK,
    'TEXT': LIGHTBLUE,
    'INPUT': TEAL,
    'TEXT_INPUT': WHITE,
    'SCROLL': LIGHTBLUE,
    'BUTTON': (LIGHTBLUE, DARK),
    'PROGRESS': (WHITE, DARK),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

sg.theme_add_new('custom', theme_dict)
sg.theme('custom')

sg.set_options(font=("Tw Cen MT", 18))


class Gui(sg.Window):
    STATUS = "-STATUS-"
    QUERY = "-QUERY-"
    MODE = "-MODE-"
    SCREEN = "-SCREEN-"
    NET = "-NET-"
    LISTEN = "-CHANGE-CMD-"
    CLEAR = "-CLEAR-"
    SEND = "-SEND-"
    SAVE = "-SAVE-"
    CLOSE = "-CLOSE-"
    PRINT = "-PRINT-"

    def __init__(self, title):
        self.layout = self.get_layout()
        super().__init__(title,
                         self.layout,
                         return_keyboard_events=True,
                         keep_on_top=True,
                         no_titlebar=True,
                         grab_anywhere=True)

    def get_layout(self):
        title_bar = []
        screen = self.get_screen()
        dashboard = self.get_dashboard()
        input_box = self.get_input_box()
        toolbar = self.cmd_buttons()
        layout = [title_bar, [screen, dashboard], input_box, toolbar]
        return layout

    def get_title_bar(self):
        return [sg.Text("S.M.A.R.T. 1", expand_x=True)]

    def get_dashboard(self):
        return sg.Column(
            [[sg.Image("smart_one/resources/circle.png", size=(200, 200))],
             [
                 sg.Text("Name:", size=(8, 1)),
                 sg.Text(NAME, size=(10, 1), text_color=GREEN)
             ],
             [
                 sg.Text("Status:", size=(8, 1)),
                 sg.Text("Standby",
                         key=self.STATUS,
                         size=(10, 1),
                         text_color=GREEN)
             ],
             [
                 sg.Text("Network:", size=(8, 1)),
                 sg.Text("Online",
                         key=self.NET,
                         size=(10, 1),
                         text_color=GREEN)
             ],
             [
                 sg.Text("Mode:", size=(8, 1)),
                 sg.Text("Text", key=self.MODE, size=(10, 1), text_color=GREEN)
             ]])

    def cmd_buttons(self):
        button_names = ["Clear", "Save", "Print", "Listen", "Close"]
        button_keys = [
            self.CLEAR, self.SAVE, self.PRINT, self.LISTEN, self.CLOSE
        ]
        return [
            sg.Button(name,
                      key=key,
                      expand_x=True,
                      image_source="smart_one/resources/button_hover.png",
                      image_size=(114, 38))
            for (name, key) in list(zip(button_names, button_keys))
        ]

    def get_screen(self):
        text = sg.Multiline("",
                            size=(40, 15),
                            pad=(2, 1),
                            key=self.SCREEN,
                            autoscroll=True,
                            disabled=True,
                            no_scrollbar=True,
                            background_color=GREEN,
                            text_color=DARK)
        frame = sg.Frame("S.M.A.R.T. 1", [[text]],
                         font="Impact 20",
                         title_color=LIGHTBLUE)
        return frame

    def get_input_box(self):
        return [
            sg.Input(expand_x=True,
                     key=self.QUERY,
                     focus=True,
                     border_width=3,
                     font=("Consolas", 15)),
            sg.Button(
                "Send",
                key=self.SEND,
                bind_return_key=True,
                visible=False,
            ),
        ]

    def check_exit(self, event):
        return event == sg.WIN_CLOSED or event == self.CLOSE

    @staticmethod
    def show_popup(message):
        sg.popup_ok(
            message,
            keep_on_top=True,
            no_titlebar=True,
        )

    @staticmethod
    def get_confirm(prompt):
        return (sg.popup_ok_cancel(
            prompt,
            no_titlebar=True,
            line_width=20,
            font="Consolas 20",
            keep_on_top=True,
        ) == "OK")

    @staticmethod
    def get_text(prompt):
        return sg.popup_get_text(prompt, no_titlebar=True, keep_on_top=True)

    def update_value(self, key, text):
        self[key].update(text)
        self.refresh()

    def print(self, query, respond, ai_name):
        conversation = self[self.SCREEN].get()
        conversation += f"\n$You: {query}\n${ai_name}: {respond}"
        self.update_value(self.SCREEN, conversation)

    def clear_screen(self):
        self.update_value(self.SCREEN, "")
