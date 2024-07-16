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
from app.widgets.drawing_pad import Painter
from kivy.config import Config
from kivy.graphics import Color
from kivy.properties import StringProperty


class DrawingPadStandAlone(App):
    path_capture = StringProperty("")

    def build(self):
        layout = BoxLayout(orientation='vertical')
        painter = Painter(size_hint=(1.,0.8), pen_color = Color(1,0,0))
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

if __name__ == "__main__":
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '450')
    PATH_CAPTURE = "/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/captures/"
    app = DrawingPadStandAlone(path_capture = PATH_CAPTURE)
    app.run()
