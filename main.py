import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalculatorGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'





class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()



if __name__ == "__main__":
    calculatorLayout = CalculatorApp()
    calculatorLayout.run()
    

