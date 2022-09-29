from kivymd.app import MDApp
from kivy.lang import Builder


KV = """
MDScreen:
	MDBottomNavigation:
		panel_color: "#eeeaea"
		selected_color_background: "#75bb7a4d"
		text_color_active: 0, 0, 1, 1
		
		MDBottomNavigationItem:
			name: "Screen 1"
			text: "Mail"
			icon: "gmail"
			badge_icon: "numeric-10"
			
			MDLabel:
				text: "Mail"
				halign: "center"
				
		MDBottomNavigationItem:
			name: "Screen 2"
			text: "Facebook"
			icon: "facebook"
			badge_icon: "numeric-5"
			
			MDLabel:
				text: "Facebook"
				halign: "center"
				
				
		MDBottomNavigationItem:
			name: "Screen 3"
			text: "LinkedIN"
			icon: "linkedin"
			badge_icon: "numeric-7"
			
			MDLabel:
				text: "LinkedIN"
				halign: "center"
		

"""

class BottomNavigationApp(MDApp):
	def build(self):
		self.theme_cls.material_style = "M3"
		return Builder.load_string(KV)
		
		
BottomNavigationApp().run()