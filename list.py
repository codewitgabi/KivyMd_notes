from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, TwoLineListItem, ThreeLineListItem, MDList, OneLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget


KV = """
ScrollView:
	MDList:
		OneLineListItem:
			text: "One Line List Item"
			
		TwoLineListItem:
			text: "Two Line List Item Line 1"
			secondary_text: "Two Line List Item Line 2"
			
		ThreeLineListItem:
			text: "Three Line List Item Line 1"
			secondary_text: "Three Line List Item Line 2"
			tertiary_text: "Three Line List Item Line 3"
			
		OneLineAvatarListItem:
			text: "One Line List Item With Avatar"
			
			ImageLeftWidget:
				source: "/storage/emulated/0/Commerce/static/img/background.png"
				
		TwoLineAvatarListItem:
			text: "Two Line List Item With Avatar"
			secondary_text: "Two Line List Item Line 2"
			
			ImageLeftWidget:
				source: "/storage/emulated/0/Commerce/static/img/background.png"
				
		ThreeLineAvatarListItem:
			text: "One Line List Item With Avatar"
			secondary_text: "Three Line List Item Line 2"
			tertiary_text: "Three Line List Item Line 3"
			
			ImageLeftWidget:
				source: "/storage/emulated/0/Commerce/static/img/background.png"
				
		OneLineIconListItem:
			text: "One Line List Item With Icon" 
			
			IconLeftWidget:
				icon: "language-php"
				
		TwoLineIconListItem:
			text: "Two Line List Item With Icon"
			secondary_text: "Two Line List Item Line 2"
			
			IconLeftWidget:
				icon: "language-css3"
			
		ThreeLineIconListItem:
			text: "One Line List Item With Avatar"
			secondary_text: "Three Line List Item Line 2"
			tertiary_text: "Three Line List Item Line 3"
			
			IconLeftWidget:
				icon: "language-cpp"
		
			
		OneLineAvatarIconListItem:
			on_release: print("Clicked")
			text: "One Line List Item With Avatar and Icon"
			
			IconLeftWidget:
				icon: "github"
				
			IconRightWidget:
				icon: "language-javascript"
				
		TwoLineAvatarIconListItem:
			on_release: print("Clicked")
			text: "Two Line List Item With Avatar and Icon"
			secondary_text: "Two Line List Item Line 2"
			
			IconLeftWidget:
				icon: "language-python"
				
			IconRightWidget:
				icon: "library"
				
		ThreeLineAvatarIconListItem:
			on_release: print("Clicked")
			text: "One Line List Item With Avatar and Icon"
			secondary_text: "Three Line List Item Line 2"
			tertiary_text: "Three Line List Item Line 3"
			
			IconLeftWidget:
				icon: "license"
				
			IconRightWidget:
				icon: "lightbulb"	
		
		
"""

class ListApp(MDApp):
	def build(self):		
		return Builder.load_string(KV)
		
		
ListApp().run()