# ROOT
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

import json
import pymysql
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from kivy.storage.jsonstore import JsonStore

# UIX
from objects.ScreenManagement import *

# Widgets
Builder.load_file("./objects/widgets/root.kv")
from objects.widgets.MainWidget import *


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        with open("config.json", encoding="utf-8") as file:
            self.settings = json.loads(file.read())
        self.store = JsonStore("data.json")
        Config.set("graphics", "width", self.settings["app"]["width"])
        Config.set("graphics", "height", self.settings["app"]["height"])
        Config.write()
        self.is_logged = self.is_logged()

    def is_logged(self):
        if self.store.exists("data"):
            with self.con().cursor() as cursor:
                sql = "SELECT login FROM tutors WHERE login = %s"
                count = cursor.execute(sql, (self.store.get("data")["login"],))
                if count != 0:
                    return True
        return False

    def con(self):
        con = pymysql.connect(
            host=self.settings["app"]["db"]["hostname"],
            user=self.settings["app"]["db"]["username"],
            password=self.settings["app"]["db"]["password"],
            database=self.settings["app"]["db"]["database"],
            charset="utf8", autocommit=True,
            cursorclass=pymysql.cursors.DictCursor)
        return con

    def build(self):
        mw = MainWidget()
        if self.is_logged == True:
            mw.ids.manager.get_screen("schedule").update()
            mw.ids.manager.get_screen("students").update()
        else:
            mw.ids.manager.current = "profile"
        return mw


if __name__ == "__main__":
    MainApp().run()
