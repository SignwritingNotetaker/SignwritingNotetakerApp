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
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
from kivy.storage.jsonstore import JsonStore
from kivy.event import EventDispatcher
from kivy.core.window import Window
from app.widgets.keyboard import SignKeyboard, Key


def update_rect(instance, value):
    instance.rect.pos = instance.pos
    instance.rect.size = instance.size

def add_background_color(widget, rgba):
        with widget.canvas.before:
            Color(*rgba) # green; colors range from 0-1 instead of 0-255
            widget.rect = Rectangle(size=widget.size,
                                pos=widget.pos)
        widget.bind(pos=update_rect, size=update_rect)


class NoteEventHandler(EventDispatcher):
    def __init__(self):
        self.id = None
        self.content = []
        self.cursor = 0
        self.register_event_type('on_content_change')
        self.register_event_type('on_cursor_move')
        self.register_event_type('on_add_signbox')
        self.register_event_type('on_del_signbox')

    def on_content_change(self, instance):
        pass

    def on_cursor_move(self, instance):
        pass
    
    def on_add_signbox(self, instance):
        pass

    def on_del_signbox(self, instance):
        pass
    
    def add_signbox(self, signbox):
        self.content.insert(self.cursor, signbox)
        self.cursor += 1
        self.dispatch('on_add_signbox')
        self.dispatch('on_content_change', self.content)
        self.dispatch('on_cursor_move', self.cursor)

    def del_signbox(self):
        if self.cursor > 0:
            self.content.pop(self.cursor)
            self.cursor -= 1
            self.dispatch('on_del_signbox')
            self.dispatch('on_content_change', self.content)
            self.dispatch('on_cursor_move', self.cursor)

    def cursor_next(self):
        if self.cursor < len(self.content) - 1:
            self.cursor += 1
        self.dispatch('on_cursor_move', self.cursor)
    
    def cursor_prev(self):
        if self.cursor > 0:
            self.cursor -= 1
        self.dispatch('on_cursor_move', self.cursor)


class SignboxBuilderEventHandler(EventDispatcher):
    def __init__(self):
        self.text = ""
        self.regexes = []
        self.register_event_type('on_content_change')
        self.register_event_type('on_add_sign')
        self.register_event_type('on_del_sign')
        self.register_event_type('on_del_empty')
        self.register_event_type('on_finish_signbox')

    def on_content_change(self, instance):
        pass

    def on_add_sign(self, instance):
        pass

    def on_del_sign(self, instance):
        pass

    def on_del_empty(self, instance):
        pass

    def on_finish_signbox(self, instance):
        pass

    def add_sign(self, sign, finish_signbox=False):
        print("add sign")
        self.regexes.append(sign.regex)
        self.dispatch('on_add_sign', self)
        self.dispatch('on_content_change', self)
        if finish_signbox:
            self.finish_signbox

    def finish_signbox(self):
        self.dispatch('on_finish_signbox', self)
        self.clear()

    def del_sign(self):
        if len(self.text) > 0:
            self.regexes.pop(-1)
            self.text = self.text[:-1]
            self.dispatch('on_del_sign', self)
            self.dispatch('on_content_change', self)
        else:
            self.register_event_type('on_del_empty')

    def clear(self):
        del self.regexes[:]
        self.text = ""


class IndexedGlossHandler():
    def __init__(self) -> None:
        self.gloss = None
    
    def load(self, indexed_gloss_path:str):
        self.gloss = JsonStore(indexed_gloss_path)

    def recommend(self, regex_keys:list, nb_reco:int = 5) -> list:
        res = []

        if len(res) > nb_reco:
            res = res[:nb_reco]
        return res





class VKeyboardStandAlone(App):
    path_capture = StringProperty("")

    def build(self):
        Window.size = (500,750)

        signbox_builder_handler = SignboxBuilderEventHandler()
        note_handler = NoteEventHandler()

        keyboard_path = "/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/src/app/assets/keyboards/limited_keys_keyboard.json"
        layout = BoxLayout(orientation="vertical")
        text_layout = BoxLayout(size_hint=(1, 0.4))
        add_background_color(text_layout, (0.7,0.7,0.7,1))

        reco_layout = BoxLayout(size_hint=(1, 0.2), orientation = "horizontal")
        add_background_color(reco_layout, (0.3,0.3,0.3,1))
        signbox_builder = Button(size_hint=(0.3, 1))
        signbox_builder.text = "a"
        add_background_color(signbox_builder, (0,0.5,0.5,1))
        # signbox_builder_handler.bind(on_content_change=partial(signbox_builder.__setattr__()))
        signbox_builder
        key = Key("b","b",1,"sign")
        signbox_builder_handler.add_sign(key)
        reco_layout.add_widget(signbox_builder)
            
        keyboard_layout = SignKeyboard(size_hint=(1, 0.4))
        add_background_color(keyboard_layout, (0.3,0.3,0.3,1))
        keyboard_layout.build(keyboard_path, signbox_builder_handler)

        layout.add_widget(text_layout)
        layout.add_widget(reco_layout)
        layout.add_widget(keyboard_layout)
        return layout

if __name__ == "__main__":
    LabelBase.register(name='SuttonSW', 
                   fn_regular='/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/src/app/assets/fonts/SuttonSignWritingOneD.ttf')
    app = VKeyboardStandAlone()
    app.run()