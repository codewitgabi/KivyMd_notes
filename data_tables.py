from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout


class DataTableApp(MDApp):
	def build(self):
		layout = AnchorLayout()
		self.data_table = MDDataTable(
			use_pagination= True,
			check= True,
			background_color_header= "#65275d",
			column_data = [
				("No.", dp(20)),
				("Name", dp(20)),
				("Age", dp(10)),
				("Major", dp(20)),
			],
			row_data = [
				("1", "Codewitgabi", "12", "Python"),
				("2", "Samuel", "23", "HTML"),
				("3", "Jøsh", "14", "HTML"),
				("4", "Codewitgabi", "12", "Python"),
				("5", "Samuel", "23", "HTML"),
				("6", "Jøsh", "14", "HTML"),
				("7", "Codewitgabi", "12", "Python"),
				("8", "Samuel", "23", "HTML"),
				("9", "Jøsh", "14", "HTML"),
				("10", "Codewitgabi", "12", "Python"),
				("11", "Samuel", "23", "HTML"),
				("12", "Jøsh", "14", "HTML"),
			],
			sorted_on= "Schedule",
			sorted_order = "DSC",
			elevation= 2,
			rows_num = 10
		)
		
		layout.add_widget(self.data_table)
		
		return layout
		
		
DataTableApp().run()