from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.uix.screenmanager import Screen

Builder.load_file("./objects/screens/StudentsScreen.kv")

class StudentsScreen(Screen):
    def __init__ (self, **kwargs):
        super(StudentsScreen, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()
    
    def update(self):


        with self.app.con().cursor() as cursor:
            sql = """SELECT * FROM students WHERE tutor_id = (SELECT id FROM tutors WHERE login=%s)"""
            cursor.execute(sql, (self.app.store.get("data")["login"],))
            rows = cursor.fetchall()
            print(rows)

            for row in rows:
                student = Button(size_hint_y=None, height=80, font_size=18, background_color=self.app.settings["color"]["lemon"])
                student.bind(on_press=self.show_student)
                student.text = row["name"]
                self.ids.students.add_widget(student)
        self.ids.students.add_widget(Widget())
    
    def show_student(self, instance):
        print(instance)