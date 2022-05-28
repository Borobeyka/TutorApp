from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

from kivy.uix.screenmanager import Screen
from objects.widgets.StudentEditContent import *
from objects.widgets.AddStudentContent import *

Builder.load_file("./objects/screens/StudentsScreen.kv")

class StudentsScreen(Screen):
    def __init__ (self, **kwargs):
        super(StudentsScreen, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()
    
    def update(self):
        self.ids.students.clear_widgets()
        with self.app.con().cursor() as cursor:
            sql = """SELECT * FROM students WHERE tutor_id = (SELECT id FROM tutors WHERE login=%s)"""
            cursor.execute(sql, (self.app.store.get("data")["login"],))
            rows = cursor.fetchall()
            for row in rows:
                student = Button(size_hint_y=None, height=80, font_size=18, background_color=self.app.settings["color"]["lemon"])
                student.bind(on_press=self.show_student)
                student.text = row["name"]
                student.name = row["id"]
                self.ids.students.add_widget(student)
        self.ids.students.add_widget(Widget())

    def show_student(self, instance):
        self.dialog = MDDialog(
            title="Редактирование ученика",
            type="custom",
            radius=[20],
            content_cls=StudentEditContent(instance.name),
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    on_release=self.close
                ),
                MDFlatButton(
                    text="Сохранить изменения",
                    on_release=self.save
                )
            ]
        )
        self.dialog.open()
    
    def save(self, instance):
        fields = self.dialog.content_cls.ids
        print(fields)

        with self.app.con().cursor() as cursor:
            sql = """UPDATE students SET name=%s, phone=%s, address=%s WHERE id=%s"""
            cursor.execute(sql, (fields.name.text, fields.phone.text, fields.address.text, self.dialog.content_cls.student_id))
        self.update()
        self.dialog.dismiss()
    
    def close(self, instance):
        self.dialog.dismiss()

    def close_dialog(self, instance):
        self.as_dialog.dismiss()
    
    def add(self, instance):
        fields = self.as_dialog.content_cls.ids
        with self.app.con().cursor() as cursor:
            sql = """INSERT INTO students VALUES(NULL, %s, %s, %s, (SELECT id FROM tutors WHERE login=%s))"""
            cursor.execute(sql, (fields.name.text, fields.phone.text, fields.address.text, self.app.store.get("data")["login"]))
        self.update()
        self.as_dialog.dismiss()
    
    def add_student(self):
        self.as_dialog = MDDialog(
            title="Добавление ученика",
            type="custom",
            radius=[20],
            content_cls=AddStudentContent(),
            buttons=[
                MDFlatButton(
                    text="Закрыть",
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Добавить",
                    on_release=self.add
                )
            ]
        )
        self.as_dialog.open()