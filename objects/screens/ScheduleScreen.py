import datetime
from dateutil.relativedelta import relativedelta
from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen

from objects.widgets.StudentCard import *
from objects.widgets.LessonContent import *

Builder.load_file("./objects/screens/ScheduleScreen.kv")

class ScheduleScreen(Screen):
    def __init__ (self, **kwargs):
        super(ScheduleScreen, self).__init__(**kwargs)
        self.current_date = datetime.now()
        self.app = MDApp.get_running_app()
    
    def update(self):
        self.update_headers()
        self.update_content()
        
    def update_headers(self):
        self.ids.header_month.text = self.current_date.strftime("%B, %Y")
        self.ids.header_day.text = self.current_date.strftime("%d, %A")

    def update_content(self):
        self.ids.students_list.clear_widgets()
        with self.app.con().cursor() as cursor:
            sql = """SELECT DISTINCT l.*, s.*, lt.lesson_type, pt.payment_type FROM lessons AS l LEFT JOIN students AS s
            ON l.student_id = s.id LEFT JOIN lesson_type AS lt ON l.lesson_type_id = lt.id LEFT JOIN payment_type as pt
            ON l.payment_type_id = pt.id WHERE l.date = %s AND l.tutor_id =( SELECT id FROM tutors
            WHERE login = %s )"""
            date = self.current_date.date()
            cursor.execute(sql, (date, self.app.store.get("data")["login"]))
            rows = cursor.fetchall()
            if len(rows) == 0:
                return
            for index, row in enumerate(rows, start=1):
                student_card = StudentCard(row)
                student_card.ids.id.text = str(index)
                student_card.ids.time.text = str(row["time"])[:-3]
                student_card.ids.student_name.text = row["name"]
                student_card.ids.address.text = row["address"]+ " (" + row["lesson_type"] + ")"
                self.ids.students_list.add_widget(student_card)

    def update_month(self, month):
        self.current_date = self.current_date + relativedelta(months=month)
        self.update()
    
    def update_day(self, day):
        self.current_date = self.current_date + relativedelta(days=day)
        self.update()

    def add_lesson(self):
        self.dialog = MDDialog(
            title="Добавление урока",
            type="custom",
            radius=[20],
            content_cls=LessonContent(),
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
    
    def close(self, instance):
        self.dialog.dismiss()
    
    def save(self, instance):
        fields = self.dialog.content_cls.ids
        if (len(fields.students_list.text) == 0 or len(fields.student_time.text) == 0 or
            len(fields.lessons_list.text) == 0 or len(fields.payment_list.text) == 0):
            fields.notificator.text = "Необходимо заполнить все поля"
            return

        data = self.dialog.content_cls.student
        with self.app.con().cursor() as cursor:
            sql = """INSERT INTO lessons VALUES(NULL, (SELECT id FROM tutors WHERE login = %s), %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (self.app.store.get("data")["login"], self.current_date, fields.student_time.text,
                data.get("student_id"), data.get("lesson_type_id"), data.get("payment_type_id")))
        self.dialog.dismiss()
        self.update()