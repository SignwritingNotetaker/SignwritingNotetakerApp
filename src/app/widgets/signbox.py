'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.core.window import Window
from app.utils.convert_text import fsw2coord
from app.utils.re_expr import RE_FSW_SPATIAL, RE_FSW_SYM
from kivy.graphics import Color
import re
from app.utils.convert_sign import sign_fsw_to_fru, sign_fsw_to_swu

DEFAULT_BOX_SIZE = 500
DEFAULT_FONT_SIZE = 26

class SignBox(RelativeLayout):
    def show(self, fsw_text:str, font_size:int=None, scale=False):
        x_ratio = self.size[0]/DEFAULT_BOX_SIZE
        y_ratio = self.size[1]/DEFAULT_BOX_SIZE
        font_size = min(x_ratio*DEFAULT_FONT_SIZE, y_ratio*DEFAULT_FONT_SIZE)
        for sign in re.findall(RE_FSW_SPATIAL, fsw_text):
            c = sign_fsw_to_swu(sign[:6])
            d_coords = fsw2coord(sign[6:])
            left = max(0.0, min(1.0, (d_coords[0]-250)/500))
            top = max(0.0, min(1.0, 1-(d_coords[1]-250)/500))
            label = Label(text=c, font_name = "SuttonSW", size_hint=(None, None), font_size=font_size, pos_hint={"right":1-left, "top":top})#, font_name="SuttonSW")
            label.bind(size=label.setter('text_size'))
            self.add_widget(label)

    def clear(self):
        self.clear_widgets()