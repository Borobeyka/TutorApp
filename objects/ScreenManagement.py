from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager

class ScreenManagement(ScreenManager):
    def __init__ (self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)