import kivy 
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1

        self.insideGridLayout = GridLayout()
        self.insideGridLayout.cols = 2

        self.firstNameLabel = Label(text='text 1')
        self.insideGridLayout.add_widget(self.firstNameLabel)
        self.nameTextInput = TextInput(multiline=False)
        self.insideGridLayout.add_widget(self.nameTextInput)

        self.lastNameLabel = Label(text='text 1')
        self.insideGridLayout.add_widget(self.lastNameLabel)
        self.lastNameTextInput = TextInput(multiline=False)
        self.insideGridLayout.add_widget(self.lastNameTextInput)
        
        self.emailLabel = Label(text='text 1')
        self.insideGridLayout.add_widget(self.emailLabel)
        self.emailTextInput = TextInput(multiline=False)
        self.insideGridLayout.add_widget(self.emailTextInput)
        
        self.add_widget(self.insideGridLayout)

        self.submit = Button(text='submit', font_size=20)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)


    def pressed(self, instance):
        firstName = self.nameTextInput.text
        lastName = self.lastNameTextInput.text
        email = self.emailTextInput.text

        print('Name: ', firstName, 'Last name: ', lastName, 'Email: ', email)
        
        self.nameTextInput.text = ''
        self.lastNameTextInput.text = ''
        self.emailTextInput.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()



if __name__ == '__main__':
    MyApp().run()


