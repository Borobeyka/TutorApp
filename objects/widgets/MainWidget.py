from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

from objects.screens.ScheduleScreen import *
from objects.screens.ProfileScreen import *
from objects.screens.StudentsScreen import *
from objects.screens.SettingsScreen import *

Builder.load_file("./objects/widgets/MainWidget.kv")

class MainWidget(BoxLayout):
    def __init__ (self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def change_screen(self, instance):
        if self.app.is_logged:
            self.ids.manager.current = instance.name
            self.ids.tool_bar.title = instance.text
