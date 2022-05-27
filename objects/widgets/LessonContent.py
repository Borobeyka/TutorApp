from datetime import datetime
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.picker import MDTimePicker

Builder.load_file("./objects/widgets/LessonContent.kv")

class LessonContent(BoxLayout):
    def __init__ (self, **kwargs):
        super(LessonContent, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.student = {}
        items = []
        with self.app.con().cursor() as cursor:
            sql = """SELECT id, name FROM students WHERE tutor_id =(SELECT id FROM tutors WHERE login = %s)"""
            cursor.execute(sql, (self.app.store.get("data")["login"]))
            rows = cursor.fetchall()
            for row in rows:
                items.append({
                    "viewclass": "OneLineListItem",
                    "text": row["name"],
                    "on_release": lambda x=row["name"], id=row["id"]: self.set_students_list_item(x, id),
                })
        self.students_list = MDDropdownMenu(
            caller=self.ids.students_list,
            items=items,
            position="bottom",
            width_mult=8,
            max_height=dp(168)
        )

        items = []
        with self.app.con().cursor() as cursor:
            sql = """SELECT * FROM lesson_type"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                items.append({
                    "viewclass": "OneLineListItem",
                    "text": row["lesson_type"],
                    "on_release": lambda x=row["lesson_type"], id=row["id"]: self.set_lessons_list_item(x, id),
                })
        self.lessons_list = MDDropdownMenu(
            caller=self.ids.lessons_list,
            items=items,
            position="bottom",
            width_mult=8,
            max_height=dp(168)
        )

        items = []
        with self.app.con().cursor() as cursor:
            sql = """SELECT * FROM payment_type"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                items.append({
                    "viewclass": "OneLineListItem",
                    "text": row["payment_type"],
                    "on_release": lambda x=row["payment_type"], id=row["id"]: self.set_payment_list_item(x, id),
                })
        self.payment_list = MDDropdownMenu(
            caller=self.ids.payment_list,
            items=items,
            position="bottom",
            width_mult=8,
            max_height=dp(168)
        )
    
    def set_payment_list_item(self, item, id):
        self.ids.payment_list.text = self.student["payment_type"] = item
        self.student["payment_type_id"] = id
        self.payment_list.dismiss()

    def set_lessons_list_item(self, item, id):
        self.ids.lessons_list.text = self.student["lesson_type"] = item
        self.student["lesson_type_id"] = id
        self.lessons_list.dismiss()

    def set_students_list_item(self, item, id):
        self.ids.students_list.text = self.student["name"] = item
        self.student["student_id"] = id
        self.students_list.dismiss()

    def on_save(self, instance, time):
        self.ids.student_time.text = str(time.strftime("%H:%M"))
    
    def show_date_picker(self):
        timepicker = MDTimePicker()
        timepicker.set_time(datetime.now())
        timepicker.bind(on_save=self.on_save)
        timepicker.open()