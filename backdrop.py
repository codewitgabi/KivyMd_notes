from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
 


Builder.load_string("""
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget

<ItemBackdropFrontLayer@TwoLineAvatarListItem>
	icon: "android"
	IconLeftWidget:
		icon: root.icon


<MyBackdropFrontLayer@ItemBackdropFrontLayer>
	backdrop: None
	text: "50% dec"
	secondary_text: " by 50 %"
	icon: "transfer-down"
	on_press: root.backdrop.open(-Window.height / 2)
	pos_hint: {"top": 1}
	_no_ripple_effect: True
	
<MyBackdropBackLayer@Image>
	size_hint: .8, .8
	source: "data/logo/kivy-icon-512.png"
	pos_hint: {"center_x": .5, "center_y": .6} 
	
	
<BackDropWidget>:
	MDBackdrop:
		id: backdrop
		left_action_items: [['menu', lambda x: self.open()]]
		title: "Demo"
		#radius_left: "25dp"
#		radius_right: "0dp"
		radius: 0
		right_action_items: [["heart", lambda x: print(x)], ["share", lambda x: print(x)]]
		header_text: "Menu:"

		
	MDBackdropBackLayer:
		MyBackdropBackLayer:
			id: backlayer
			
		MDBackdropFrontLayer:
			MyBackdropFrontLayer:
				backdrop: backdrop 

""")


class BackDropWidget(MDScreen):
	pass
	
	
class BackDropApp(MDApp):
	def build(self):
		return BackDropWidget()
	
	
BackDropApp().run()