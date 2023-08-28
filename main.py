import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

Builder.load_file('calculator.kv') #need to load kv file

Config.set('graphics', 'resizable', 1) #makes window resizable




