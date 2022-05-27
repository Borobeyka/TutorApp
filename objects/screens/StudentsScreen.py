
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen

Builder.load_file("./objects/screens/StudentsScreen.kv")

class StudentsScreen(Screen):
    def __init__ (self, **kwargs):
        super(StudentsScreen, self).__init__(**kwargs)