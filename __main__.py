# ROOT
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

# UIX
from kivy.uix.label import Label

# Widgets
Builder.load_file("./objects/widgets/root.kv")
from objects.widgets.MainWidget import *

Config.set("graphics", "width", "600")
Config.set("graphics", "height", "900")

class MainApp(App):
    config = None

    def __init__ (self):
        super(MainApp, self).__init__()
        with open("config.json", encoding="utf-8") as file:
            self.settings = json.loads(file.read())
    
    def build(self):
        mw = MainWidget()
        return mw

if __name__ == "__main__":
    MainApp().run()