from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivy.lang import Builder


Builder.load_string("""
<CarouselWidget>:
	MDCarousel:
		id: carousel
		size: root.size
		on_slide_complete:
			print(self.index)
			print(len(self.slides))
			print(dir(self))
		
		BoxLayout:
			orientation: "vertical"
			Button:
				text: "Button 1"
				font_size: "25sp"
				
			MDLabel:
				size_hint: 1, .1
				text: str(carousel.index + 1) + "/" + str(len(carousel.slides))
				font_size: dp(22)
				halign: "center"
				
		MDBoxLayout:
			orientation: "vertical"
			Button:
				text: "Button 2"
				font_size: "25sp"
				pos_hint: {"top": 1}
				
			MDLabel:
				size_hint: 1, .1
				text: str(carousel.index + 1) + "/" + str(len(carousel.slides))
				font_size: dp(22)
				halign: "center"

""")

class CarouselWidget(MDWidget):
	pass
	

class CarouselApp(MDApp):
	def build(self):
		screen =  CarouselWidget()
		
		return screen
		
		
CarouselApp().run()