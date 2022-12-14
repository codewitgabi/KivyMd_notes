from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import NoTransition, SwapTransition, ScreenManager, Screen, SlideTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton, MDRoundFlatIconButton 


Builder.load_string("""
#:import toast kivymd.toast.toast

<LogoutScreen>:
	MDIconButton:
		icon: "logout"
		pos_hint: {"center_x": .5, "center_y": .5}
		icon_size: dp(48)
		theme_icon_color: "Custom"
		icon_color: [1, 0, 0, 1]
		on_release:
			root.manager.current = "home"
			root.manager.transition.direction = "right"
			toast("Home", True, 80, 20, 0)
	
<HomeScreen>:
	MDIconButton:
		icon: "home"
		pos_hint: {"center_x": .5, "center_y": .5}
		icon_size: dp(48)
		theme_icon_color: "Custom"
		icon_color: [1, 0, 0, 1]
		on_release:
			root.manager.current = "logout"
			root.manager.transition.direction = "left"
			toast("Logout", True, 80, 20, 0)
""")

class HomeScreen(Screen):
	pass

		
class LogoutScreen(Screen):
	pass	


class ExpansionPanelApp(MDApp):
	def build(self):
		sm = ScreenManager(
			transition= SwapTransition()
		)
		sm.add_widget(
			HomeScreen(name= "home")
		)
		sm.add_widget(
			LogoutScreen(name= "logout")
		)
		return sm
		
		
ExpansionPanelApp().run()