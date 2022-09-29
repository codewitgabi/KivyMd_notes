from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton


KV = """

MDScreen:
	MDRectangleFlatButton:
		text: "DISPLAY SNACKBAR"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: app.show_snackbar()
"""

class SnackBarApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
	def show_snackbar(self):
		self.snack_bar = Snackbar(
			text= "[color=#ec654fff]Hello world!![/color]",
			#size_hint_x= .5,
			#snackbar_x= "10dp",
			snackbar_y= "10dp",
			buttons= [
				MDFlatButton(
					text= "Cancel",
					opposite_colors= True,
					on_release= self.close_snackbar
				),
				MDFlatButton(
					text= "Retry",
					opposite_colors= True
				)
			],
			bg_color= (0, 0, 1, 1)
		)
		
		self.snack_bar.open()
		
		
	def close_snackbar(self, widget):
		self.snack_bar.dismiss
	
		
SnackBarApp().run()