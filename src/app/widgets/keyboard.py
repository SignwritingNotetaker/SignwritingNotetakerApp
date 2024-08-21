from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import json

class Key(Button):
    def __init__(self, show_str:str, write_str:str, lenght_hint:float, key_type:str, regex:str=None, **kwargs):
        super().__init__(**kwargs)
        if show_str in "↵⌫":
            self.font_name = "DejaVuSans"
        else:
            if key_type == "sign":
                self.font_size = 42
            self.font_name = "SuttonSW"
        self.write = StringProperty(write_str)
        self.regex = StringProperty(regex)
        self.background_color = [0.2,0.2,0.2, 1]
        self.text = show_str
        self.key_type = key_type
        self.size_hint = [lenght_hint, 1]
        print("load key", show_str)


class SignKeyboard(BoxLayout):
    def build(self, keyboard_path:str, signbox_builder_handler):
        self.spacing = 3
        self.padding = 5
        with open(keyboard_path,"r") as f:
            template = json.load(f)["keyboard"]
        self.orientation='vertical'
        for row in template:
            row_box = BoxLayout()
            row_box.spacing = 3
            self.add_widget(row_box)
            for key_params in row:
                key = Key(*key_params)
                row_box.add_widget(key)
                key.bind(on_pressed=signbox_builder_handler.add_sign)

    
