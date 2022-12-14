from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


KV = """
<MD3Card>:
	padding: 16
	size_hint: None, None
	size: "200dp", "100dp"
	
	MDRelativeLayout:
		size_hint: None, None
		size: root.size
		
		MDIconButton:
			icon: "dots-vertical"
			pos: root.width - (self.width + root.padding[0] + dp(4)), root.height - (self.height + root.padding[0] + dp(4))
			on_release: app.root.ids.banner.show()
			
		MDLabel:
			id: label
			text: root.text
			adaptive_size: True
			color: .2, .2, .2, .8
			
			
MDScreen:
	MDBoxLayout:
		id: box
		orientation: "vertical"
		adaptive_size: True
		spacing: "56dp"
		pos_hint: {"center_x": .5, "center_y": .5}
		
		
	MDBanner:
		type: "two-line-icon"
		id: banner
		text: ["This is my banner widget", "Second line for banner widget"]
		over_widget: box 
		vertical_pad: 0
		right_action: ["CANCEL", lambda x: print(x)]
		left_action: ["CLOSE", lambda x: banner.hide()]
		opening_time: 0.1
		
			
"""

class MD3Card(MDCard, RoundedRectangularElevationBehavior):
	text = StringProperty()
	

class CardApp(MDApp):
	def build(self):
		self.theme_cls.material_style = "M3"
		return Builder.load_string(KV)
		
		
	def on_start(self):
		styles = {
			"elevated": "#f6eeee",
			"filled": "#f4dedc",
			"outlined": "#f8f5f4"
		} 
		
		for style in styles:
			self.root.ids.box.add_widget(
				MD3Card(
					style= style,
					text= style.capitalize(),
					line_color= (0.2, 0.2, 0.2, 0.8),
					md_bg_color= styles[style]
				)
			)
		
		
CardApp().run()