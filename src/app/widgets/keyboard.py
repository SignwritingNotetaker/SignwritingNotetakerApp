from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase

class SignKey(Button):
    sign = ObjectProperty(None)

    def get_sign(self, sign_text:str):
        self.parent.parent.parent.get_sign(sign_text)

class SignKeyboard(PageLayout):
    sign = ObjectProperty(None)

    def get_sign(self, sign_text):
        self.sign = sign_text

if __name__ == "__main__":

    from kivy.app import App
    from kivy.lang import Builder
    from kivy.config import Config

    class LocalTestApp(App):
        def build(self):
            keyboard = SignKeyboard()
            return keyboard
    
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '740')
    LabelBase.register(name='NotoSWFont', 
                   fn_regular='/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/src/app/assets/fonts/NotoSansSignWriting-Regular.ttf')
    Builder.load_file("keyboard.kv")

    app = LocalTestApp()

    app.run()
    
