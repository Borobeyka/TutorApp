from kivy.lang import Builder
from kivymd.uix.card import MDCard

from objects.widgets.StudentCard import *

Builder.load_file("./objects/widgets/StudentCard.kv")

class StudentCard(MDCard):
    def __init__ (self, **kwargs):
        super(StudentCard, self).__init__(**kwargs)
    
    def on_touch(self, instance):
        print(instance.ids.student_name.text)