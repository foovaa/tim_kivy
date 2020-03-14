import kivy
kivy.require('1.11.1')

from kivy.app import App, Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('f4_kivy.kv')

class MyFloatLayout(FloatLayout):
    pass



class MyApp(App):
    def build(self):
        return MyFloatLayout()



if __name__ == '__main__':
    MyApp().run()        






