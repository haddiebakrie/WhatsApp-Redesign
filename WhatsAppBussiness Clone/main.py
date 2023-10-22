from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from screens.homescreen import HomeScreen
from screens.viewstatusscreen import ViewStatusScreen
from screens.messagescreen import MessageScreen
from screens.settingscreen import SettingScreen

Window.size = (400, 688)
#Window.top = 0.5
#Window.left = 980

Window.custom_titlebar = False
class WhatsApp(MDFloatLayout):
	screen_manager = ObjectProperty()
	

class MainApp(MDApp):
	messages = ListProperty()
	def build(self):
		self.init_menu()
		self.theme_cls.primary_palette = 'Teal'
		self.theme_cls.theme_style = 'Dark'
		return WhatsApp()
	def init_menu(self):
		menu_items=[
				 { "text":f"Advertise",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='Advertise':self.menu_callback(x)}, 
				 {"text":f"Bussiness Tools",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='Bussiness Tools':self.menu_callback(x)},
				 {"text":f"New Group",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='New Group':self.menu_callback(x)},

				 {"text":f"New BroadCast",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='New BroadCast':self.menu_callback(x)},

				 {"text":f"Labels",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='Labels':self.menu_callback(x)},
				 {"text":f"Linked Devices",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='Linked Devices':self.menu_callback(x)},
				 {"text":f"Starred Message",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='Starred Message':self.menu_callback(x)},
				 {"text":f"Settings",
				 	"viewclass":"OneLineListItem",
				 	"divider":None,
				 	"on_release":lambda x='Settings':self.settings_callback(x)},
				 ]
		self.menu = MDDropdownMenu(items=menu_items,
 									width_mult=4)
	def callback(self, instance):
		''' display settings options '''
		self.menu.caller = instance
		self.menu.open()
	def settings_callback(self, value):
		self.menu.dismiss()
		self.root.screen_manager.current = 'setting'

	def menu_callback(self, instance):
		print(instance)
		self.menu.dismiss()
		
	def change_tabs(self, args):
		tab_instance = args[1]
		tab_name = args[3]
		if tab_name == 'Chats':
			tab_instance.children[0].load_chats()
		if tab_name == 'Groups':
			tab_instance.children[0].load_groups()
			#tab_instance.load_groups()
		if tab_name == 'Status':
			tab_instance.children[0].load_status()
			#tab_instance.load_groups()

if __name__ =='__main__':
	MainApp().run()
