from instructions import*
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction)
        lbl_name = Label( text = "Enter name")
        self.in_name = TextInput(text_hint = "Name", multiline = False)
        lbl_age = Label( text = "Enter name")
        self.in_age = TextInput(text_hint = "Age", multiline = False)

