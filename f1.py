import kivy
kivy.require('1.11.1')

from kivy.app import App, Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_file('f1_kivy.kv')


class MySimpleGridLayout(GridLayout):
    pass


class MyApp(App):
    def build(self):
        return MySimpleGridLayout()


if __name__ == '__main__':
    MyApp().run()




