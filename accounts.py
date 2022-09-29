from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
import sqlite3
from kivymd.toast import toast
import re


class AccountScreen(MDScreen):
	def submit_form_data(self):
		username = self.ids.username.text
		email = self.ids.email.text
		password = self.ids.password.text
		confirm_password = self.ids.confirm_password.text
		
		with sqlite3.connect("kivy_account.db") as conn:
			cursor = conn.cursor()
			
			email_regex = re.compile(r"^\w+@\w+\.?\w{3}\.?\w{3}$")
			
			if password == confirm_password:
				if len(password) >= 8:
					if len(email_regex.findall(email)) == 1:
						db_emails = conn.execute("""SELECT email FROM user""")
						for db_email in db_emails:
							if db_email[0] == email:
								self.ids.email.error = True
								self.ids.email.helper_text = "Email Already in use!!!"
								return
			
						conn.execute("""INSERT INTO user VALUES (?, ?, ?)""", (username, email, password))	
						conn.commit()
						
						self.ids.username.text = ""
						self.ids.email.text = ""
						self.ids.password.text = ""
						self.ids.confirm_password.text = ""
						self.ids.password.error = False
						self.ids.password.helper_text = ""
						self.ids.email.error = False
						self.ids.email.helper_text = ""
						
						toast(f"Account for {username} created successfully!!!", True, 80, 20, 0)
						
					else:
						self.ids.email.error = True
						self.ids.email.helper_text = "Invalid email address!!"
				else:
					self.ids.password.error = True
					self.ids.password.helper_text = "Password must contain minimum of 8 characters"
			else:
				self.ids.password.error = True
				self.ids.password.helper_text = "Passwords do not match"


class AccountApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Green"
		
		return AccountScreen()
		
		
	def on_start(self):
		with sqlite3.connect("kivy_account.db") as conn:
			cursor = conn.cursor()
			
			cursor.execute("""CREATE TABLE if not exists user (
				username text,
				email text,
				password text
			)""")
			
			conn.commit()
	
	
	def switch_mode(self, switch):
		self.theme_cls.theme_style = "Dark" if switch.active else "Light"
		
		
if __name__ == "__main__":
	AccountApp().run()