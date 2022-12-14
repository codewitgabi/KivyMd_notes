from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list.list import OneLineIconListItem, MDList
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior


KV = """
<ItemDrawer>:
	text: "Files"
	theme_text_color: "Custom"
	#on_release: self.parent.set_color_item(self)	
	IconLeftWidget:
		id: icon
		icon: "folder"
		theme_text_color: "Custom"
		icon_size: "30dp"
		#text_color: root.text_color


MDScreen:
	MDNavigationLayout:
		MDScreenManager:
			MDScreen:
				MDTopAppBar:
					title: "Demo"
					elevation: 10
					pos_hint: {"top": 1}
					#md_bg_color: "#e7e4c0"
#					specific_text_color: "4a4939"
					left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
					
				MDRaisedButton:
					text: "Test Widget Positioning"
					pos_hint: {"center_x": .5, "center_y": .5}
		
		MDNavigationDrawer:
			id: nav_drawer
			#md_bg_color: "#f7f4e7"
			type: "modal"
			anchor: "left"
			padding: 5, 16, 25, 16
			#close_on_click: False
			#enable_swiping: False
			size_hint_x: .7
			radius: 0
			#on_touch_down: print(dir(it))
			
			MDNavigationDrawerMenu:
				
				MDNavigationDrawerHeader:
					title: "Nav Header"
					text: "Header Text"
					spacing: "4dp"
					padding: (dp(12), dp(30), 0, dp(12))
					source: "/storage/emulated/0/Pictures/Screenshots/Screenshot_20220914-234925~2.png"
					text_halign: "right"
					title_halign: "right"
					title_font_size: "28sp"
					
				MDNavigationDrawerDivider:
					
				MDNavigationDrawerLabel:
					text: "Nav Label"
					
				MDNavigationDrawerDivider:
					
				MDNavigationDrawerItem:
					icon: "account"
					text: "gabrielmichael497@gmail.com"
					right_text: "99+"
					text_color: [1,1,1,1] if app.theme_cls.theme_style == "Dark" else [0,0,0,1]
					selected_color: [1,1,1,1] if app.theme_cls.theme_style == "Dark" else [0,0,0,1]
					
				MDNavigationDrawerItem:
					icon: "logout"
					text: "Logout"
					on_release: print("Logout Success!!!")
					text_color: [1,1,1,1] if app.theme_cls.theme_style == "Dark" else [0,0,0,1]
					selected_color: [1,1,1,1] if app.theme_cls.theme_style == "Dark" else [0,0,0,1]
					
				MDNavigationDrawerDivider:
					
				MDNavigationDrawerItem:
					text: "Switch Mode"
					on_release: app.switch_mode()
					text_color: [1,1,1,1] if app.theme_cls.theme_style == "Dark" else [0,0,0,1]
					selected_color: [1,1,1,1] if app.theme_cls.theme_style == "Dark" else [0,0,0,1]
					
				OneLineListItem:
					text: "Please ensure to rate this app amd report bugs!!!"
			
				#ContentNavigationDrawer:
#					orientation: "vertical"
#					padding: "8dp", "-50dp"
#					spacing: "8dp"
#					
#					AnchorLayout:
#						anchor_x: "left"
#						size_hint_y: None
#						height: avatar.height
#						
#						Image:
#							id: avatar
#							source: "/storage/emulated/0/Download/cert-CT-HTW9DMPH.png"
#							size_hint: None, None
#							size: ("56dp", "56dp")
#					
#					MDLabel:
#						text: "KivyMD Library"
#						font_style: "Button"
#						size_hint_y: None
#						height: self.texture_size[1]
#						
#					MDLabel:
#						text: "kivydevelopment@gmail.com"
#						font_style: "Caption"
#						size_hint_y: None
#						height: self.texture_size[1]
#						
#					ScrollView:
#						DrawerList:
#							id: md_list


"""

class DrawerList(ThemableBehavior, MDList):
	def set_color_item(self, obj):
		for item in self.children:
			if item.text_color == self.theme_cls.primary_color:

				item.text_color = self.theme_cls.text_color

				break

		obj.text_color = self.theme_cls.primary_color
 


class ItemDrawer(OneLineIconListItem):
	icon = StringProperty()
	

class ContentNavigationDrawer(BoxLayout):
	pass


class PracticeApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Teal"
		self.theme_cls.theme_style = "Dark"
		return Builder.load_string(KV)
		
	def switch_mode(self):
		self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
		
		
PracticeApp().run()