# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from screen import *
from ruffier import*


class HeartCheck(App):
    #title
    #icon 
    def build(self):
        sm = ScreenManager()
        rf = Ruffier()
        sm.add_widget(StartScr( ruffier = rf,next_screen='test1',direction='up', name = "start"))
        sm.add_widget(Test1Src(ruffier = rf,next_screen='test2',direction='left',name = 'test1'))
        sm.add_widget(Test2Src(next_screen='test3',direction='down',name = 'test2'))
        sm.add_widget(Test3Src(ruffier = rf,next_screen='result',direction='right',name = 'test3'))
        sm.add_widget(ResultSrc(ruffier = rf, name = 'result'))
        return sm
HeartCheck().run()