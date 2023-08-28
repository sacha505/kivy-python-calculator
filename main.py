import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder

Config.set('graphics', 'resizable', 1)

Window.size = (400, 600)  # I want the window to be calculator-shaped


# Creating Layout class
class grid(GridLayout):

    # = calls function
    def calculate(self, calculation):
        self.display.text = str(eval(calculation))


# Creating App class
class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (202, 237, 255)
        return grid()


# creating object and running it
calcApp = CalculatorApp()
calcApp.run()
