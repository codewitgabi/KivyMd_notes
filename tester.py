from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty


class TesterScreen(MDScreen):
	text = StringProperty("Hello")
	

class TesterApp(MDApp):
	text = StringProperty("Hello\nLine")
	def build(self):
		return TesterScreen()
		
			
TesterApp().run()