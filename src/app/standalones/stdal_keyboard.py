'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

import sys
print(sys.path)
sys.path.append("/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/src/")
print(sys.path)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.graphics import Color
from kivy.properties import StringProperty, ObjectProperty
import json
from kivy.core.text import LabelBase


class SignKey(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_key_pressed')
        self.write = ""

    def on_press(self):
        super().on_press()
        self.dispatch('on_write_stuff', self.write)

    def on_write_stuff(self, message):
        # This method will be called when the event is dispatched
        pass

class CurrentSignInput(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fsw = ""
    
    

class Suggetion(Button):
    pass

class NoteColumn(Widget):
    pass


class VKeyboardStandAlone(App):
    path_capture = StringProperty("")

    def build(self):
        keyboard_path = "app/assets/keyboards/limited_keys_keyboard.json"
        with open(keyboard_path,"r") as f:
            template = json.load(f)["keyboard"]

        layout = BoxLayout(orientation='vertical')
        text_layout = BoxLayout(y=0.2)
        reco_layout = BoxLayout(y=0.2)
        keyboard_layout = BoxLayout(y=0.6)
        for row in template:
            for key_params in row:
                pass

        layout.add_widget(painter)
        sub_layout = BoxLayout(size_hint=(1,0.2))
        btn_clear = Button(text="clear")
        btn_clear.bind(on_press=lambda x:painter.clear())
        btn_save = Button(text="save")
        btn_save.bind(on_press=lambda x:painter.export_image(path = self.path_capture))
        sub_layout.add_widget(btn_clear)
        sub_layout.add_widget(btn_save)
        layout.add_widget(sub_layout)
        return layout
    
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="No message yet")

        key_button = KeyButton()
        key_button.bind(on_write_stuff=self.write_stuff_handler)

        layout.add_widget(self.label)
        layout.add_widget(key_button)

        return layout

    def write_stuff_handler(self, instance, message):
        self.label.text = message

if __name__ == "__main__":
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '450')
    LabelBase.register(name='SWFill', 
                   fn_regular='app/assets/fonts/SuttonSignWritingFill.ttf')
    app = VKeyboardStandAlone()
    app.run()