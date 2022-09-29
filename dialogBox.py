from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem, OneLineAvatarListItem
from kivy.uix.boxlayout import BoxLayout


KV = """
<Item>:
	on_release:
		print(self.text)
		
	IconLeftWidget:
		icon: root.source
		
		
<ItemConfirm>:
	on_release: root.set_icon(check)
	
	CheckboxLeftWidget:
		id: check
		group: "check"
		

<Content>:
	orientation: "vertical"
	spacing: "10dp"
	size_hint_y: None
	height: "120dp"
	
	MDTextField:
		hint_text: "Name"
		
	MDTextField:
		hint_text: "City"


MDScreen:
	MDRectangleFlatButton:
		text: "Open Dialog Box: Example 1"
		pos_hint: {"center_x": .5, "center_y": .6}
		on_release: app.show_dialog_box()
		
	MDRectangleFlatButton:
		text: "Open Dialog Box: Example 2"
		pos_hint: {"center_x": .5, "center_y": .5}
		on_release: app.show_dialog_box2()
		
	MDRectangleFlatButton:
		text: "Open Dialog Box: Example 3"
		pos_hint: {"center_x": .5, "center_y": .4}
		on_release: app.show_dialog_box3()
		
	MDRectangleFlatButton:
		text: "Open Dialog Box: Example 4"
		pos_hint: {"center_x": .5, "center_y": .3}
		on_release: app.show_dialog_box4()

"""

class Item(OneLineIconListItem):
	divider= None
	source= StringProperty()


class ItemConfirm(OneLineAvatarListItem):
	divider= None
	
	def set_icon(self, obj):
		obj.active = True
		check_list = obj.get_widgets(obj.group)
		for check in check_list:
			if check != obj:
				check.active = False
			else:
				print(obj)
				

class Content(BoxLayout):
	pass
	

class DialogBoxApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
		
	def show_dialog_box(self):
		self.dialog = MDDialog(
			title= "Greet Text",
			text= "Hello world!!!",
			auto_dismiss= False,
			buttons= [
				MDFlatButton(
					text= "CLOSE",
					theme_text_color= "Custom",
					text_color= self.theme_cls.primary_color,
					on_release= self.close_dialog
				),
				MDFlatButton(
					text= "CANCEL",
					theme_text_color= "Custom",
					text_color= self.theme_cls.primary_color
				),
			]
		)
		self.dialog.open()
		
	def close_dialog(self, obj):
		self.dialog.dismiss()
		
	def show_dialog_box2(self):
		self.dialog2 = MDDialog(
			title= "Select Backup Account",
			text= "Select an account to use as backup",
			type= "simple",
			items= [
				Item(text= "User1@gmail.com", source= "account"),
				Item(text= "User2@gmail.com", source= "account"),
			]
		)
		self.dialog2.open()
	
	def show_dialog_box3(self):
		self.dialog3 = MDDialog(
			title= "Select Ringtone",
			type= "confirmation",
			items = [
				ItemConfirm(text= "Phobos"),
				ItemConfirm(text= "Luna"),
				ItemConfirm(text= "Right"),
				ItemConfirm(text= "Solo"),
				ItemConfirm(text= "Diamond"),
				ItemConfirm(text= "Bouster"),
				ItemConfirm(text= "Crook"),
				ItemConfirm(text= "Destiny"),
			],
			buttons= [
				MDFlatButton(
					text= "CLOSE",
					theme_text_color= "Custom",
					text_color= self.theme_cls.primary_color,
				),
				MDFlatButton(
					text= "CANCEL",
					theme_text_color= "Custom",
					text_color= self.theme_cls.primary_color
				),
			]
		)
		self.dialog3.open()
		
	def show_dialog_box4(self):
		self.dialog4 = MDDialog(
			title= "Select Ringtone",
			type= "custom",
			content_cls= Content(),
			buttons= [
				MDFlatButton(
					text= "CLOSE",
					theme_text_color= "Custom",
					text_color= self.theme_cls.primary_color,
				),
				MDFlatButton(
					text= "CANCEL",
					theme_text_color= "Custom",
					text_color= self.theme_cls.primary_color
				),
			]
		)
		self.dialog4.open()
		
DialogBoxApp().run()