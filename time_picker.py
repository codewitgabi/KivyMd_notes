from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDTimePicker
from kivy.utils import get_color_from_hex


KV = """
MDScreen:	
	MDTopAppBar:
		title: "Demo"
		elevation: 10
		pos_hint: {"top": 1}
		
	MDRaisedButton:
		text: "Open Color Picker"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: app.open_time_picker()

"""

class ColorPickerApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
	def open_time_picker(self):
		from datetime import datetime
		import time
		
		hour = time.strftime("%I")
		min = time.strftime("%M")
		sec = time.strftime("%S")
		am_pm = time.strftime("%p").lower()
		
		cur_time = datetime.strptime(f"{hour}:{min}:{sec}", "%H:%M:%S").time()
		tp = MDTimePicker(
			primary_color= get_color_from_hex("#72225b"),
			accent_color=get_color_from_hex("#5d1a4a"),
			selector_color= get_color_from_hex("#e93f39"),
			text_color= get_color_from_hex("#ffffff"),
			text_current_color= get_color_from_hex("#00ff00"),
			am_pm = am_pm,
		)
		tp.set_time(cur_time)
		tp.bind(time= self.get_time)
		tp.open()
		
	def get_time(self, instance, value):
		print(value)
		
		
ColorPickerApp().run()