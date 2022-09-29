from kivymd.app import MDApp
from kivy.lang import Builder


class ScrollViewApp(MDApp):
	def build(self):		
		return Builder.load_file("scroll.kv")
		
		
ScrollViewApp().run()