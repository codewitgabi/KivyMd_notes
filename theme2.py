from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.factory import Factory
from kivymd.color_definitions import colors
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout


KV = """
<Root@MDBoxLayout>:
	orientation: "vertical"
	
	MDTabs:
		id: android_tabs
		on_tab_switch: app.on_tab_switch(*args)
		size_hint_y: None
		height: dp(48)
		tab_indicator_anim: False
		
		
	RecycleView:
		id: rv
		key_view_class: "view_class"
		key_size: "height"
		
		RecycleBoxLayout:
			default_size: None, dp(48)
			default_size_hint: 1, None
			size_hint_y: None
			height: self.minimum_height
			orientation: "vertical"
			
			
<ItemColor>:
	size_hint_y: None
	height: dp(42)
		
	MDLabel:
		text: root.text
		halign: "center"
		
<Tab>:
	
"""


class Tab(MDBoxLayout, MDTabsBase):
	pass
	

class ItemColor(MDBoxLayout):
	text = StringProperty()
	colors = ListProperty()
	

class IconsApp(MDApp):
	title = "Color Definitions"
	def build(self):
		Builder.load_string(KV)
		self.screen = Factory.Root()
		
		for name_tab in colors.keys():
			tab = Tab(text= name_tab)
			self.screen.ids.android_tabs.add_widget(tab)
			
		return self.screen
		
	def on_tab_switch(self,  instance_tabs, instance_tab, instance_tabs_label, tab_text):
		self.screen.ids.rv.data = []
		
		if not tab_text:
			tab_text = "Red"
		for value_color in colors[tab_text]:
			self.screen.ids.rv.data.append(
				{
					"view_class": "ItemColor",
					"text": value_color,
					"md_bd_color": colors[tab_text][value_color]
				}
			)
			
	def on_start(self):
		self.on_tab_switch(
			None,
			None,
			None,
			self.screen.ids.android_tabs.ids.layout.children[-1].text
		)
		
				
IconsApp().run()