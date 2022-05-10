from kivy.lang import Builder

# from objects.screens.ScheduleScreen import *
# from objects.screens.ProfileScreen import *

from kivy.uix.screenmanager import ScreenManager

Builder.load_file("./objects/ScreenManagement.kv")

class ScreenManagement(ScreenManager):
    pass