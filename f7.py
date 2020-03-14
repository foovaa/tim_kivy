import kivy
kivy.require('1.11.1')

from kivy.app import App, Builder
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


Builder.load_file('f7_kivy.kv')

class MyPopup(FloatLayout):
    pass


class MyWidget(Widget):
    def popupButton(self):
        showPopup()



def showPopup():
    myPopup = MyPopup()

    popupWindow = Popup(title='Popup', content=myPopup, size_hint=(None, None), size=(400, 400))
    popupWindow.open()

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()

