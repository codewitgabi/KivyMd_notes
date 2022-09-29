from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivy.lang import Builder
import re

KV = """
MDScreen:
	
	MDTextField:
		id: username
		pos_hint: {"center_x": .5, "center_y": .7}
		size_hint_x: .8
		hint_text: "Username"
		helper_text: "Enter your registered username"
		helper_text_mode: "on_focus"
		mode: "rectangle"
		#required: True
		#on_focus: app.validate_input(self)
		max_text_length: 16
		#multiline: True
		icon_left: "account"
		
	MDTextField:
		id: email
		pos_hint: {"center_x": .5, "center_y": .58}
		size_hint_x: .8
		hint_text: "Email"
		helper_text: "Enter a valid email address"
		helper_text_mode: "on_focus"
		mode: "rectangle"
		#required: True
		#on_focus: app.validate_input(self)
		max_text_length: 100
		icon_left: "gmail"
		
	MDTextField:
		id: password
		pos_hint: {"center_x": .5, "center_y": .46}
		size_hint_x: .8
		hint_text: "Password"
		helper_text: "Enter password"
		helper_text_mode: "on_focus"
		mode: "rectangle"
		password: True
		#required: True
		#on_focus: app.validate_input(self)
		max_text_length: 100
		icon_left: "key-variant"
			
	MDRectangleFlatButton:
		pos_hint: {"right": .9, "center_y": .34}
		text: "Signup"
		font_size: dp(19)
		on_release: app.validate_input(username,email, password)

"""


class pracApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
		
	def validate_input(self, username, email, password):
		comp = re.compile(r"^\w+@\w+\.\w{3}\.?[a-z]*$")
		
		if len(comp.findall(email.text)) == 0:
			email.helper_text = "Enter a valid email address"
			email.error = True
			
		if len(password.text) < 10:
			password.helper_text = "min length should be 10 characters"
			password.error = True
		
		
pracApp().run()