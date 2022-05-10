from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = """
<MyLayout>

    BoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        GridLayout:
            cols:3
            rows:3
            

            Spinner:
                id: spinner_id
                text: "Menu"
                values: ["Catalogue","Buy","Payment Methods", "Contact"]
                on_text: root.spinner_clicked(spinner_id.text)

        

            Label:
                id: Label1
                text: "My Panel"

            Button:
                text:"Buy"

    
        WindowManager:
            FirstWindow:
            SecondWindow:  
    
<FirstWindow>:
    name: "first"
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            text: "First Screen"
            font_size: 32

        Button:
            text: "Next Screen"
            font_size: 32
            on_release: 
                root.manager.current= "second"

<SecondWindow>:
    name: "second"
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        Label:
            text: "Second Screen"
            font_size: 32

        Button:
            text: "Go Back"
            font_size: 32
            on_release: 
                root.manager.current= "first"
"""
Builder.load_string(kv)

class MyLayout(Widget):
    def spinner_clicked(self,value):
        self.ids.Label1.text= f'You selected: {value}' 



#Definine our different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass 


class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run() 