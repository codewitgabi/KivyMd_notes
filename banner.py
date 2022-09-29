from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


Builder.load_string("""
<BannerWidget>:
	MDBanner:
		type: "three-line-icon"
		id: banner
		text: ["This is my banner widget", "Second line for banner widget", "Here is the third line"]
		over_widget: screen
		vertical_pad: toolbar.height
		right_action: ["CANCEL", lambda x: print(x)]
		left_action: ["CLOSE", lambda x: banner.hide()]
		icon: "language-python"
		opening_time: 0.1
		
	MDTopAppBar:
		id: toolbar
		title: "Demo"
		pos_hint: {"top": 1}
		elevation: 10
		
	MDBoxLayout:
		id: screen
		orientation: "vertical"
		size_hint_y: None
		height: Window.height - toolbar.height
		
		OneLineListItem:
			text: "Click to display banner"
			on_release: banner.show()
			
			Widget:

""")

class BannerWidget(MDScreen):
	pass
	
	
class BannerApp(MDApp):
	def build(self):
		return BannerWidget()
	
	
BannerApp().run()