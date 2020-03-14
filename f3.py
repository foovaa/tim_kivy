import kivy
kivy.require('1.11.1')

from kivy.app import App, Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
import kivy.properties as kivyProp 

Builder.load_file('f3_kivy.kv')

class MyWidget(Widget):
    firstName = kivyProp.ObjectProperty(None)
    lastName = kivyProp.ObjectProperty(None)
    email= kivyProp.ObjectProperty(None)

    def submitButton(self):
        print('Name: ', self.firstName.text,
              'Last name: ', self.lastName.text,
              'Email: ', self.email.text)
        

class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
