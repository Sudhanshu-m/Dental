from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

class testApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass


class mainApp(MDApp):
    def build(self):
        return testApp()
    

if __name__ == "__main__":
    Window.size=(360,640)
    Builder.load_file("Dental.kv")
    mainApp().run()