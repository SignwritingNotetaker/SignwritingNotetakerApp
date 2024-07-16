'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from data_models import Sign, Pose, Note

class SignLabel(Label):
    sign = ObjectProperty(None)

    def quick_save(self):
        self.export_to_png("base/{}.png".format(self.sign.swu))


    
class SignLineTextInput(TextInput):
    pass

    
class PoseWidget(Widget):
    pose = ObjectProperty(None)

    def export_to_png(self, filename, *args, **kwargs):
        return super().export_to_png(filename, *args, **kwargs)
    
if __name__ == "__main__":
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.core.text import LabelBase
    LabelBase.register(name='noto', 
                   fn_regular='fonts/NotoSansSignWriting-Regular.ttf')
    LabelBase.register(name='fill', 
                   fn_regular='fonts/SuttonSignWritingFill.ttf')
    LabelBase.register(name='line', 
                   fn_regular='fonts/SuttonSignWritingLine.ttf')
    LabelBase.register(name='null', 
                   fn_regular='fonts/SuttonSignWritingNull.ttf')
    LabelBase.register(name='oned', 
                   fn_regular='fonts/SuttonSignWritingOneD.ttf')
    
    TEXT = "\n".join(["abc123!?@\U0001D800,\U0001D801,\U0001D802,\U0001D803,\U0001D804",
    ",".join([chr(i) for i in range(ord("\U0001D80C"), ord("\U0001D81c")+1)]),
    ",".join([chr(i) for i in range(ord("\U0001D9EF"), ord("\U0001D9FF")+1)]),
    ",".join([chr(i) for i in range(ord("\U00040001"), ord("\U00040011")+1)]),
    ",".join([chr(i) for i in range(ord("\U0004F418"), ord("\U0004F428")+1)])
    ])
    ALL_SWU_S = "\n".join([
        "".join(chr(i+16*800) for i in range(j, j+16*40,8))
        for j in range(ord("\U00040001"), ord("\U0004F428")+1,16*40)
    ])

    class TestApp(App):
        def build(self):
            box = BoxLayout(orientation="horizontal")
            button = Button(text="save")
            # text = "\U00040001"
            # text = "\U00042C41"
            text = "\U0001D800\U0001D903\U0001d905\U0001d9ff\U0001D9EC\U0001DA8A\U0001DA7A"
            for t in text:
                oned = SignLabel(sign = Sign(swu=t),font_name = "noto", font_size=200)
                oned.text = t
                box.add_widget(oned)
            # button.bind(on_pressed = oned.quick_save)
            # noto = Label(font_name = "noto")
            # noto.text = TEXT
            # box.add_widget(noto)
            # fill = Label(font_name = "fill")
            # fill.text = TEXT
            # box.add_widget(fill)
            # line = Label(font_name = "line")
            # line.text = TEXT
            # box.add_widget(line)
            # null = Label(font_name = "null")
            # null.text = TEXT
            # box.add_widget(null)
            
            # label = SignLabel()
            # label.sign = Sign("S15a3f")
            # print(label.sign, label.sign.uni)
            # label.text = label.sign.uni
            # box.add_widget(label)
            return box
    app = TestApp()
    app.run()

