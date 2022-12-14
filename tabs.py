from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts


KV = """

#<Tab>:
#	MDIconButton:
#		id: icon
#		icon: root.icon
#		icon_size: "48sp"
#		pos_hint: {"center_x": .5, "center_y": .5}


#<Tab>:
#	MDLabel:
#		id: label
#		text: root.title
#		halign: "center"


<Tab>:
	MDIconButton:
		id: icon
		icon: app.icons[3]
		icon_size: "48sp"
		pos_hint: {"center_x": .5, "center_y": .5}


BoxLayout:
	orientation: "vertical"
	
	MDTopAppBar:
		title: "Demo"
		
	MDTabs:
		id: tabs
		tab_indicator_height: "3dp"
		tab_indicator_type: "line"
		allow_stretch: True
		#fixed_tab_panel_width: "200dp"
		tab_bar_height: "50dp"
		elevation: 10
		indicator_color: 0, 0, 1, .6
		lock_swiping: True
		text_color_active: 1, 1, 1, 1
		text_color_normal: 1,1,1,1
		on_tab_switch: app.on_tab_switch(*args)
		on_ref_press: app.on_ref_press(*args)
"""


class Tab(MDFloatLayout, MDTabsBase):
	content_text = StringProperty("")
	

class TabApp(MDApp):
	icons = list(md_icons.keys())[15:30]
	index = 0
	
	def build(self):
		self.theme_cls.primary_palette = "Teal"
		self.theme_cls.theme_style = "Dark"
		return Builder.load_string(KV)
		
	def on_start(self):

		"""
		Use this for tab with icon. Also uncomment the first tab class in the KV string.
		"""
		#for icon in self.icons:
		#	self.root.ids.tabs.add_widget(
		#		Tab(icon= icon)
		#	)
			
		"""
		Use this for tab with text. Also uncomment the second tab class in the KV string.
		"""
		
		#for icon in self.icons:
		#	self.root.ids.tabs.add_widget(
		#		Tab(title= icon)
		#	)
		
		"""
		Use this for tab with text and icon. Also uncomment the first/second tab class in the KV string.
		"""
		
		#for icon in self.icons:
		#	self.root.ids.tabs.add_widget(
		#		Tab(icon= icon, title= icon)
		#	)
		
		"""
		Use this for tab with text and icon that will remove tab on click. Also uncomment the third tab class in the KV string.
		"""
		
		for name_tab in self.icons:
			self.root.ids.tabs.add_widget(Tab(title=f"[ref={name_tab}]{md_icons['close']}[/ref]{name_tab}"))
	
	def on_tab_switch(
		self,
		instance_tabs,
		instance_tab,
		instance_tab_label, 
		tab_text
	):
		"""
		Use this for tab with icon. Also uncomment the first tab class in the KV string.
		"""
		#count_icon = instance_tab.icon
		#print(f"Welcom to {count_icon} tab!!!")
		
		"""
		Use this for tab with text. Also uncomment the second tab class in the KV string.
		"""
		
		#instance_tab.ids.label.text = tab_text
		
		pass
		
	def on_ref_press(
		self,
		instance_tabs,
		instance_tab_label,
		instance_tab,
		instance_tab_bar,
		instance_carousel
	):
		for instance_tab in instance_carousel.slides:
			if instance_tab.title == instance_tab_label.text:
				instance_tabs.remove_widget(instance_tab_label)
				break
 
					
		
TabApp().run()