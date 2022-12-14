from kivymd.app import MDApp
from kivy.lang import Builder


KV = """

MDScreen:
	GridLayout:
		cols: 2
		spacing: 10
		padding: [10, 10]
		
		MDSmartTile:
			radius: 24
			box_radius: [24, 24, 0, 0]
			box_color: 1,1,1,.2
			size_hint: .5, .5
			#size: "150dp", "150dp"
			pos_hint: {"center_x": .5, "center_y": .5}
			source: "/storage/emulated/0/BizzBlog/img/Screenshot_20220908-234110~2.png"
			box_position: "header"
			#overlap: False
			
			MDIconButton:
				icon: "heart-outline"
				theme_icon_color: "Custom"
				icon_color: 1, 0, 0, 1
				pos_hint: {"center_y": .5}
				on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"		
			
			MDLabel:
				text: "Julia and Julie"
				bold: True
				color: 1, 1, 1, 1 
				
		MDSmartTile:
			radius: 24
			box_radius: [0,0,24, 24]
			box_color: 1,1,1,.2
			size_hint: .5, .5
			#size: "150dp", "150dp"
			pos_hint: {"center_x": .5, "center_y": .5}
			source: "/storage/emulated/0/BizzBlog/img/Screenshot_20220908-234110~2.png"
			
			MDIconButton:
				icon: "heart-outline"
				theme_icon_color: "Custom"
				icon_color: 1, 0, 0, 1
				pos_hint: {"center_y": .5}			
			
			MDLabel:
				text: "Julia and Julie"
				bold: True
				color: 1, 1, 1, 1 
				
		MDSmartTile:
			radius: 24
			box_radius: [24, 24, 0, 0]
			box_color: 1,1,1,.2
			size_hint: .5, .5
			#size: "150dp", "150dp"
			pos_hint: {"center_x": .5, "center_y": .5}
			source: "/storage/emulated/0/BizzBlog/img/Screenshot_20220908-234110~2.png"
			box_position: "header"
			#overlap: False
			
			MDIconButton:
				icon: "heart-outline"
				theme_icon_color: "Custom"
				icon_color: 1, 0, 0, 1
				pos_hint: {"center_y": .5}
				on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"		
			
			MDLabel:
				text: "Julia and Julie"
				bold: True
				color: 1, 1, 1, 1 
				
		MDSmartTile:
			radius: 24
			box_radius: [0,0,24, 24]
			box_color: 1,1,1,.2
			size_hint: .5, .5
			#size: "150dp", "150dp"
			pos_hint: {"center_x": .5, "center_y": .5}
			source: "/storage/emulated/0/BizzBlog/img/Screenshot_20220908-234110~2.png"
			
			MDIconButton:
				icon: "heart-outline"
				theme_icon_color: "Custom"
				icon_color: 1, 0, 0, 1
				pos_hint: {"center_y": .5}			
			
			MDLabel:
				text: "Julia and Julie"
				bold: True
				color: 1, 1, 1, 1 
"""

class ImageListApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
		
ImageListApp().run()