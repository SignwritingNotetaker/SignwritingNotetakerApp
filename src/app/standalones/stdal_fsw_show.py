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
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.config import Config
from utils.convert_text import RE_FSW_SPATIAL, RE_FSW_BOX_SPATIAL, RE_FSW_SYM, fsw2coord
import re
from utils.convert_sign import sign_fsw_to_fru, sign_fsw_to_swu

Z_FSW = "M518x517S10020482x487S2450a487x483"
Z_FRU = "\U0001D800\U0001DA9C\U0001D945\U0001DAAA"
SHARK = "M521x531S15a10509x469S29c27490x501S16257480x488S20a00488x472"
DUBLIN = "AS10111S23a0bS37606M515x544S37606485x476S10111489x455S23a0b493x489"

DEFAULT_FONT_SIZE = 26
DEFAULT_BOX_SIZE = 500

def show(fsw_text:str, font_size:int=None, box_size:int=None, crop=False):
    image = None
    if not font_size and not box_size:
        font_size = DEFAULT_FONT_SIZE
        box_size = DEFAULT_BOX_SIZE
    elif box_size:
        font_size = int(DEFAULT_FONT_SIZE*box_size/DEFAULT_BOX_SIZE)
    else:
        box_size = int(DEFAULT_BOX_SIZE*font_size/DEFAULT_FONT_SIZE)
    scale_ratio = box_size/DEFAULT_BOX_SIZE
    default_font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", DEFAULT_FONT_SIZE)
    font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", font_size)
    if crop:
        box = re.findall(RE_FSW_BOX_SPATIAL, fsw_text)
        if box:
            box = box[0]
            a,b = fsw2coord(box[1:])
            h = int(scale_ratio*(a-500)*2)
            l = int(scale_ratio*(b-500)*2)
            print(a,b,h,l)
            image = Image.new('RGB', (h, l), 'white')
        else:
            box = re.findall(RE_FSW_SYM, fsw_text)
            if box and len(box)==1:
                box = box[0]
                a,b = fsw2coord(box[1:])
                h = int(scale_ratio*(a-500)*2)
                l = int(scale_ratio*(b-500)*2)
                print(a,b,h,l)
                image = Image.new('RGB', (h, l), 'white')

    if not image:
        image = Image.new('RGB', (box_size, box_size), 'white')
    draw = ImageDraw.Draw(image)
    print(image.size)
    for sign in re.findall(RE_FSW_SPATIAL, fsw_text):
        c = sign_fsw_to_swu(sign[:6])
        d_coords = fsw2coord(sign[6:])
        d_left, d_top, d_right, d_bottom = default_font.getbbox(c)
        sign_l = d_right - d_left
        sign_h = d_bottom - d_top
        d_center_x = d_coords[0] - DEFAULT_BOX_SIZE + sign_l/2
        d_center_y = d_coords[1] - DEFAULT_BOX_SIZE + sign_h/2
        # Calculate position to draw the character (center it)
        left, top, right, bottom = font.getbbox(c)
        text_x = int(scale_ratio*d_center_x+left/2+image.size[0]/2)
        text_y = int(scale_ratio*d_center_y+top/2+image.size[1]/2)
        print(c,d_coords, d_center_x, d_center_y, text_x, text_y)
        
        # Draw the character on the image
        draw.text((text_x, text_y), c, font=font, fill='black')

    
    # Display the image
    image.show()

def draw_one_sign(fsw:str, font_size:int, box_size:int):
    image = Image.new('RGB', (box_size, box_size), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", font_size)
    text = sign_fsw_to_swu(fsw)
    left, top, right, bottom = font.getbbox(text)
    text_x = (box_size - right+left) // 2
    text_y = (box_size - bottom+top) // 2
    draw.text((text_x, text_y), text, font=font, fill='black')
    # image.show()
    image.save("base/{}.png".format(fsw))

class SignBox()

class StandaloneFormalSignWritingShow(App):
    def build(self):
        self.text_input = TextInput(size_hint=(1, 0.5))
        self.label = Label(text='', font_size=20, size_hint=(1, 0.5))
        copy_button = Button(text='Copy Text', size_hint=(1, 0.1))
        copy_button.bind(on_press=self.copy_text)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.text_input)
        layout.add_widget(copy_button)
        layout.add_widget(self.label)
        
        return layout
    
    def copy_text(self, instance):
        self.label.text = self.text_input.text

if __name__ == "__main__":
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '450')
    LabelBase.register(name='SuttonSW', 
                   fn_regular='SuttonSignWritingOneD.ttf')
    app = StandaloneFormalSignWritingShow()
    app.run()