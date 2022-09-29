from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast


KV = """
MDScreen:
	MDRectangleFlatButton:
		id: box
		text: "POP TOAST"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: app.pop_toast()
"""

	
class ToastApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
	def pop_toast(self):
		toast("Hello world!!", True, 80, 20, 0)
	
		
ToastApp().run()