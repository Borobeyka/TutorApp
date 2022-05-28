from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

Builder.load_file("./objects/widgets/AddStudentContent.kv")

class AddStudentContent(BoxLayout):
    def __init__ (self, **kwargs):
        super(AddStudentContent, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()
    
        