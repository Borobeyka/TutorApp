from datetime import datetime
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.picker import MDTimePicker

Builder.load_file("./objects/widgets/StudentCardContent.kv")

class StudentCardContent(BoxLayout):
    def __init__ (self, student, **kwargs):
        self.student = student
        super(StudentCardContent, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()
        items = []
        with self.app.con() as cursor:
            sql = """SELECT id, name FROM students WHERE tutor_id =(SELECT id FROM tutors WHERE login = %s)"""
            cursor.execute(sql, (self.app.store.get("data")["login"]))
            rows = cursor.fetchall()
            for row in rows:
                items.append({
                    "viewclass": "OneLineListItem",
                    "text": row["name"],
                    "on_release": lambda x=row["name"]: self.set_menu_item(x),
                })
        self.menu = MDDropdownMenu(
            caller=self.ids.students_list,
            items=items,
            position="bottom",
            width_mult=8,
            max_height=dp(168)
        )

    def set_menu_item(self, item):
        self.ids.students_list.text = item
        self.menu.dismiss()
    
    def on_save(self, instance, time):
        self.student.ids.time.text = self.ids.student_time.text = str(time.strftime("%H:%M"))
    
    def show_date_picker(self):
        timepicker = MDTimePicker()
        timepicker.set_time(datetime.strptime(self.student.ids.time.text, "%H:%M"))
        timepicker.bind(on_save=self.on_save)
        timepicker.open()