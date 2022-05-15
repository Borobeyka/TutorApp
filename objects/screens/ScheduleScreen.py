import datetime
from dateutil.relativedelta import relativedelta
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen

from objects.widgets.StudentCard import *

Builder.load_file("./objects/screens/ScheduleScreen.kv")

class ScheduleScreen(Screen):
    def __init__ (self, **kwargs):
        super(ScheduleScreen, self).__init__(**kwargs)
        self.current_date = datetime.datetime.now()
    
    def load(self):
        self.update_content()
        
    def update_content(self):
        self.ids["header_month"].text = self.current_date.strftime("%B, %Y")
        self.ids["header_day"].text = self.current_date.strftime("%d, %A")

        print(self.ids["students_list"].add_widget(StudentCard()))

        
    def update_month(self, month):
        self.current_date = self.current_date + relativedelta(months=month)
        self.update_content()
    
    def update_day(self, day):
        self.current_date = self.current_date + relativedelta(days=day)
        self.update_content()