from kivy.lang import Builder
from kivymd.uix.card import MDCard

from objects.widgets.StudentCard import *

Builder.load_file("./objects/widgets/StudentCard.kv")

class StudentCard(MDCard):
    pass