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
from kivy.core.window import Window
from app.widgets.signbox import SignBox
from kivy.storage.jsonstore import JsonStore


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


class RecoBar(BoxLayout):


    def clear(self):
        self.clear_widgets()

class StandaloneFormalSignWritingReco(App):
    def build(self):
        Window.size = (500,750)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.signbox = SignBox(size_hint=(1, 0.66))
        self.text_input = TextInput(hint_text= "Formal sign writing text", size_hint=(1, 0.24))
        copy_button = Button(text='To sign', size_hint=(1, 0.1))
        copy_button.bind(on_press=self.copy_text)

        # label_00 = Label(text="00", size_hint=(None, None), font_size=20, pos_hint={'left': 0, 'top': 1})
        # label_00.bind(size=label_00.setter('text_size')) 
        # label_11 = Label(text="11", size_hint=(None, None), font_size=20, pos_hint={'right': 1, 'bottom': 0})
        # self.signbox.add_widget(label_00)
        # self.signbox.add_widget(label_11)

        self.text_input.text = SHARK
        
        layout.add_widget(self.signbox)
        layout.add_widget(copy_button)
        layout.add_widget(self.text_input)
        
        return layout
    
    
    def copy_text(self, instance):
        self.signbox.clear()
        self.signbox.show(self.text_input.text)
        


if __name__ == "__main__":
    Z_FSW = "M518x517S10020482x487S2450a487x483"
    Z_FRU = "\U0001D800\U0001DA9C\U0001D945\U0001DAAA"
    SHARK = "M521x531S15a10509x469S29c27490x501S16257480x488S20a00488x472"
    DUBLIN = "AS10111S23a0bS37606M515x544S37606485x476S10111489x455S23a0b493x489"


    LabelBase.register(name='SuttonSW', 
                   fn_regular='/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/src/app/assets/fonts/SuttonSignWritingOneD.ttf')
    app = StandaloneFormalSignWritingShow()
    # app.init_text(SHARK)
    app.run()