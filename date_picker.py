from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDDatePicker
from kivy.utils import get_color_from_hex


KV = """
MDScreen:	
	MDTopAppBar:
		title: "Demo"
		elevation: 10
		pos_hint: {"top": 1}
		
	MDRaisedButton:
		text: "Show Date Picker"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: app.show_date_picker()

"""

class DatePickerApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
	def show_date_picker(self):
		dp = MDDatePicker(
			min_year= 2022,
			max_year= 2032,
			title= "Select Date",
			primary_color= get_color_from_hex("#72225b"),
			accent_color=get_color_from_hex("#5d1a4a"),
			selector_color= get_color_from_hex("#e93f39"),
			text_color= get_color_from_hex("#ffffff"),
			text_current_color= get_color_from_hex("#00ff00"),
			text_weekday_color= get_color_from_hex("#ffffff"),
			helper_text= "Please enter a valid date",
		)
		dp.bind(on_save= self.save_date, on_cancel= self.close_date_picker)
		dp.open()
		
	def save_date(self, instance, value, date_range):
		print(f"{instance} ==== value: {value} & range: {date_range}")
		
	def close_date_picker(self, instance, value):
		instance.dismiss
		
		
DatePickerApp().run()