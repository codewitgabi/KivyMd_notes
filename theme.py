import kivy
kivy.require("2.0.0")
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

"""
KivyMD's ThemeManager helps for configuring styling in our application. The look and feel can be tweaked using this.
"""

KV = """

MDBoxLayout:
	orientation: "vertical"
	
	MDBoxLayout:
		md_bg_color: app.theme_cls.bg_light
		
	MDBoxLayout:
		md_bg_color: app.theme_cls.bg_normal
		
	MDBoxLayout:
		md_bg_color: app.theme_cls.bg_dark
		
	MDBoxLayout:
		md_bg_color: app.theme_cls.bg_darkest
		
	MDSwitch:
		#widget_style: "ios" #android
		on_active: app.switch_mode()
		pos_hint: {"center_x": .5}
	
"""

class ThemeApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Cyan"
		self.theme_cls.primary_hue = "900"
		
		print(self.theme_cls.text_color)
		print(self.theme_cls.icon_color)
		print(self.theme_cls.error_color)
		
		""""
		Change Background Color
		self.theme_cls.theme_style = "Dark" # Light
		"""
		"""
		screen = MDScreen()
		screen.add_widget(
			MDRectangleFlatButton(
				text= "Theme App Button",
				pos_hint= {"center_x": .5, "center_y": .5}
			)
		)
		
		return screen
		"""
		
		return Builder.load_string(KV)
		
	def switch_mode(self):
		if self.theme_cls.theme_style == "Light":
			self.theme_cls.theme_style = "Dark"
		else:
			self.theme_cls.theme_style = "Light"
			
	
	def on_start(self):
		self.fps_monitor_start()
		
		

if __name__ == "__main__":
	ThemeApp().run()