
import kivy
kivy.require('2.3.0')
import datetime as dt

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder
from kivy.config import Config
from utils.data_models import Sign





class SignEditor(BoxLayout):
    sign = ObjectProperty(None)

    def clear(self):
        self.ids["painter"].clear()

    def export(self):
        self.ids["painter"].export_image()

class Root(BoxLayout):
    pass


class SLRecoApp(App):
    def build(self):
        root_widget = Root()
        return root_widget

if __name__ == '__main__':
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '740')
    LabelBase.register(name='NotoSWFont', 
                   fn_regular='NotoSansSignWriting-Regular.ttf')
    Builder.load_file("sign_level.kv")

    app = SLRecoApp()

    app.run()