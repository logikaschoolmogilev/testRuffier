from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from instructions import*

class StartScr(Screen):
    def __init__(self, next_screen, direction, ruffier, **kwargs):
        super().__init__(**kwargs)
        self.RUFFIER = ruffier
        self.NEXT_SCREEN = next_screen 
        self.DIRECTION = direction

        instr = Label(text =txt_instruction, halign = "center", pos_hint={"y":0.6})
        instr.bind(size = instr.setter("text_size"))
        
        lbl_name = Label(text = "Enter you name", pos_hint={"x":0.5})
        lbl_age = Label(text = "Enter you age")

        self.in_name = TextInput(hint_text='Write	here name',multiline=False)
        self.in_age = TextInput(hint_text='Write	here age',multiline=False)
        self.btn_ok = Button(text = "Next", size_hint = (0.2,0.1), pos_hint={"x":0.4, "y":0.05})
        self.btn_ok.on_press = self.next
        vert = FloatLayout()
        h1 = BoxLayout(orientation = "horizontal", size_hint=(0.8,0.05), pos_hint={"y":0.3})
        h2 = BoxLayout(orientation = "horizontal", size_hint=(0.8,0.05), pos_hint={"y":0.23})
        h1.add_widget(lbl_name)
        h1.add_widget(self.in_name)
        h2.add_widget(lbl_age)
        h2.add_widget(self.in_age)

        vert.add_widget(instr)
        vert.add_widget(h1)
        vert.add_widget(h2)
        vert.add_widget(self.btn_ok)

        self.add_widget(vert)

    def next(self):
        self.RUFFIER.NAME = self.in_name.text
        self.RUFFIER.AGE = int(self.in_age.text)
        if self.RUFFIER.NAME and self.RUFFIER.AGE:
            self.manager.current = self.NEXT_SCREEN
            self.manager.transition.direction = self.DIRECTION



class Test1Src(Screen):
    def __init__(self,next_screen, direction,ruffier, **kwargs):
        super().__init__(**kwargs)
        self.NEXT_SCREEN = next_screen 
        self.DIRECTION = direction
        self.RUFFIER = ruffier

        instr = Label(text =txt_test1, halign = "center", pos_hint={"y":0.6})
        instr.bind(size = instr.setter("text_size"))
        
        lbl_test1 = Label(text = "Enter you result", pos_hint={"x":0.5})
        
        self.in_test1 = TextInput(hint_text='Write	here you resuly',multiline=False)
        self.btn_ok = Button(text = "Next", size_hint = (0.2,0.1), pos_hint={"x":0.4, "y":0.05})
        self.btn_ok.on_press = self.next
        vert = FloatLayout()
        h1 = BoxLayout(orientation = "horizontal", size_hint=(0.8,0.05), pos_hint={"y":0.3})
        h1.add_widget(lbl_test1)
        h1.add_widget(self.in_test1)
    

        vert.add_widget(instr)
        vert.add_widget(h1)
        
        vert.add_widget(self.btn_ok)

        self.add_widget(vert)

    def next(self):
        self.RUFFIER.P1 = int(self.in_test1.text)
        if self.RUFFIER.P1:
            self.manager.current = self.NEXT_SCREEN
            self.manager.transition.direction = self.DIRECTION

class Test2Src(Screen):
    def __init__(self,next_screen, direction, **kwargs):
        super().__init__(**kwargs)
        self.NEXT_SCREEN = next_screen 
        self.DIRECTION = direction
        
        instr = Label(text =txt_test2, halign = "center", pos_hint={"y":0.6})
        instr.bind(size = instr.setter("text_size"))
        
        self.btn_ok = Button(text = "Next", size_hint = (0.2,0.1), pos_hint={"x":0.4, "y":0.05})
        self.btn_ok.on_press = self.next
        vert = FloatLayout()
        vert.add_widget(instr)
     
        
        vert.add_widget(self.btn_ok)

        self.add_widget(vert)

    def next(self):
        
        
            self.manager.current = self.NEXT_SCREEN
            self.manager.transition.direction = self.DIRECTION

class Test3Src(Screen):
    def __init__(self,next_screen, direction, ruffier, **kwargs):
        super().__init__(**kwargs)
        self.RUFFIER = ruffier
        self.NEXT_SCREEN = next_screen 
        self.DIRECTION = direction
      

        instr = Label(text =txt_test3, halign = "center", pos_hint={"y":0.6})
        instr.bind(size = instr.setter("text_size"))
        
        lbl_res = Label(text = "Enter you result", pos_hint={"x":0.5})
        lbl_res_rest = Label(text = "Enter you result after rest")

        self.in_test2 = TextInput(hint_text='Write here result',multiline=False)
        self.in_test3 = TextInput(hint_text='Write here result after rest',multiline=False)
        self.btn_ok = Button(text = "Next", size_hint = (0.2,0.1), pos_hint={"x":0.4, "y":0.05})
        self.btn_ok.on_press = self.next
        vert = FloatLayout()
        h1 = BoxLayout(orientation = "horizontal", size_hint=(0.8,0.05), pos_hint={"y":0.3})
        h2 = BoxLayout(orientation = "horizontal", size_hint=(0.8,0.05), pos_hint={"y":0.23})
        h1.add_widget(lbl_res)
        h1.add_widget(self.in_test2)
        h2.add_widget(lbl_res_rest)
        h2.add_widget(self.in_test3)

        vert.add_widget(instr)
        vert.add_widget(h1)
        vert.add_widget(h2)
        vert.add_widget(self.btn_ok)

        self.add_widget(vert)

    def next(self):
        self.RUFFIER.P2 = int(self.in_test2.text)
        self.RUFFIER.P3 = int(self.in_test3.text)
        if self.RUFFIER.P2 and self.RUFFIER.P3:
            self.manager.current = self.NEXT_SCREEN
            self.manager.transition.direction = self.DIRECTION

class ResultSrc(Screen):
    def __init__(self,ruffier, **kwargs):
        super().__init__(**kwargs)
        self.RUFFIER = ruffier
        self.result = Label(text ="result", halign = "center", pos_hint={"y":0.6})
        self.result.bind(size = self.result.setter("text_size"))
        
        vert = FloatLayout()
        
        vert.add_widget(self.result)

        self.add_widget(vert)
        self.on_enter = self.before

    def before(self):
        self.RUFFIER.test2()
        self.result.text = self.RUFFIER.TXT
