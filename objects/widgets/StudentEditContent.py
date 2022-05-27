from datetime import datetime
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.picker import MDTimePicker

Builder.load_file("./objects/widgets/StudentEditContent.kv")

class StudentEditContent(BoxLayout):
    def __init__ (self, student_id, **kwargs):
        self.student_id = student_id
        self.app = MDApp.get_running_app()

        with self.app.con().cursor() as cursor:
            sql = """SELECT * FROM students WHERE id=%s"""
            cursor.execute(sql, (self.student_id,))
            row = cursor.fetchone()
            self.student = row

        super(StudentEditContent, self).__init__(**kwargs)
        