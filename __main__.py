# ROOT
import json
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config

# UIX
from objects.ScreenManagement import *

# Widgets
Builder.load_file("./objects/widgets/root.kv")
from objects.widgets.MainWidget import *

class MainApp(MDApp):
    def __init__ (self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        with open("config.json", encoding="utf-8") as file:
            self.settings = json.loads(file.read())
        Config.set("graphics", "width", self.settings["app"]["width"])
        Config.set("graphics", "height", self.settings["app"]["height"])
        Config.write()

    def build(self):
        return MainWidget()

if __name__ == "__main__":
    MainApp().run()