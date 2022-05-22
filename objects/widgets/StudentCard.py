from kivy.lang import Builder
from kivymd.uix.card import MDCard

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from objects.widgets.StudentCardContent import *

Builder.load_file("./objects/widgets/StudentCard.kv")

class StudentCard(MDCard):
    def __init__ (self, **kwargs):
        super(StudentCard, self).__init__(**kwargs)
    
    def on_touch(self, instance):
        dialog = MDDialog(
            title="Сведения об уроке",
            type="custom",
            radius=[20],
            content_cls=StudentCardContent(self),
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                ),
                MDFlatButton(
                    text="Сохранить изменения",
                )
            ]
        )
        dialog.open()