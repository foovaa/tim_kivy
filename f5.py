import kivy
kivy.require('1.11.1')

from kivy.app import App, Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

Builder.load_file('f5_kivy.kv')

class MyTouch(Widget):
    def __init__(self, **kwargs):
        super(MyTouch, self).__init__(**kwargs)


        with self.canvas:
            self.color = Color(0, 0, 1, 1, mode='rgba')
            self.whiteBoard = Rectangle(pos=(0, 0), size=(50, 50))


    def on_touch_down(self, touch):
        print('Down ', touch)
        self.whiteBoard.pos = touch.pos

    def on_touch_move(self, touch):
        print('Move ', touch)
        self.whiteBoard.pos = touch.pos

    def on_touch_up(self, touch):
        print('Up ', touch)
        self.whiteBoard.pos = touch.pos



class MyApp(App):
    def build(self):
        return MyTouch()


if __name__ == '__main__':
    MyApp().run()


