from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.snackbar import Snackbar


Builder.load_string("""
<PracticeWidget>:
	MDBoxLayout:
		orientation: "vertical"
		
		MDTopAppBar:
			title: "PythonHub"
			opposite_colors: True
			left_action_items: [["menu", lambda x: app.callback()]]
			right_action_items: [["dots-vertical", lambda x: app.callback()],["clock", lambda x: app.callback(), "This is more options"]]
			elevation: 10
		
		Label:
			text: "Hello world"
			color: [0,0,0,1]
			font_size: dp(20)
			text_size: self.size
			valign: "top"
			padding: [20, 20]
		
		MDBottomAppBar:
			MDTopAppBar:
				title: "Botton Nav"
				type: "bottom"
				icon: "git"
				left_action_items: [["menu", lambda x: app.callback1(x), "This is a nav menu"]]
				mode: "end"
				icon_color: [0, 0, 1, 1]
				on_action_button: print("Action Button Pressed")
""")


class PracticeWidget(MDScreen):
	pass
	

class PracticeApp(MDApp):
	
	def build(self):
		self.theme_cls.primary_palette= "Green"
		return PracticeWidget()
		
	def callback(self):
		print("Nav Bar")
		
	def callback1(self, button):
		Snackbar(text= "Hello world").open()
		
PracticeApp().run()