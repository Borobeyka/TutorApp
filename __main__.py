# ROOT
import json
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config

# UIX

# Widgets
Builder.load_file("./objects/widgets/root.kv")
from objects.ScreenManagement import *
from objects.screens.ScheduleScreen import *
from objects.screens.ProfileScreen import *

from objects.widgets.MainWidget import *

Config.set("graphics", "width", "600")
Config.set("graphics", "height", "900")
Config.write()

class MainApp(MDApp):
    def __init__ (self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        with open("config.json", encoding="utf-8") as file:
            self.settings = json.loads(file.read())
    
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    MainApp().run()