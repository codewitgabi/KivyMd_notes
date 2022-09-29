from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.label import MDLabel, MDIcon
from kivy.lang import Builder
from kivymd.font_definitions import theme_font_styles


Builder.load_string("""
<LabelIconWidget>:
	MDBoxLayout:
		id: box
		orientation: "vertical"
		size: root.size
		padding: [30, 10]
		
		MDIcon:
			icon: "gmail"
			pos_hint: {"center_x": .5, "y": 0}
			badge_icon: "numeric-10"
			badge_icon_color: [1, 1, 1, 1]
			badge_bg_color: [0, 0, 1, 1]
			badge_font_size: 20
""")


class LabelIconWidget(MDWidget):
	pass
	

class LabelIconApp(MDApp):
	def build(self):
		screen =  LabelIconWidget()
		
		for theme in [
			"Primary",
			"Secondary",
			"Hint",
			"Error",
			"ContrastParentBackground"
		]:
			screen.ids.box.add_widget(
				MDLabel(
					text= theme,
					halign= "center", 
					theme_text_color= theme,
					font_style= "H5"
				)
			)
		for style in theme_font_styles[:-1]:
			screen.ids.box.add_widget(
				MDLabel(
					text= style,
					halign= "center",
					font_style= style
				)
			)

		return screen
		
		
LabelIconApp().run()