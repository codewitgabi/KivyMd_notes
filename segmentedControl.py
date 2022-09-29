from kivymd.app import MDApp
from kivy.lang import Builder


KV = """
MDScreen:
	padding: [20, 0]
	MDSegmentedControl:
		pos_hint: {"center_x": .5, "top": 1}
		md_bg_color: "#334294ee"
		segment_panel_height: self.height
		separator_color: [1,1,1,1]
		segment_color: [1,1,1,1]
		radius: 0
		elevation: 10
		on_active: print(dir(self))
		
		MDSegmentedControlItem:
			text: "Female"
			
		MDSegmentedControlItem:
			text: "Male"
			
		MDSegmentedControlItem:
			text: "All"
				
"""

class SegmentedApp(MDApp):
	def build(self):
		return Builder.load_string(KV) 
		
		
SegmentedApp().run()