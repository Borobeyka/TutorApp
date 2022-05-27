import hashlib
from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen

Builder.load_file("./objects/screens/ProfileScreen.kv")

class ProfileScreen(Screen):
    def __init__ (self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def save(self):
        fields = self.ids
        if len(fields.password.text) == 0:
            fields.notificator.text = "Необходимо заполнить все поля"
            return
        
        fields.notificator.text = ""
        hashlib.sha256(b"" + bytearray(fields.password.text, "utf8")).hexdigest()

        with self.app.con().cursor() as cursor:
            sql = """UPDATE tutors SET password=%s WHERE login=%s"""
            cursor.execute(sql, (hashlib.sha256(b"" + bytearray(fields.password.text, "utf8")).hexdigest(),
            self.app.store.get("data")["login"]))
        self.app.store.put("data", login=fields.login.text)
        fields.notificator.text = "Учетные данные обновлены"