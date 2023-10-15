from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from screens.homescreen import HomeScreen
from screens.viewstatusscreen import ViewStatusScreen

Window.size = (400, 780)
Window.top = 0.5
Window.left = 980
class WhatsApp(MDFloatLayout):
	screen_manager = ObjectProperty()
	

class MainApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = 'Teal'
		self.theme_cls.material_style = 'M3'
		self.theme_cls.them_style = 'dark'
		return WhatsApp()
	def callback(self, instance):
		''' display settings options '''
		print(instance)
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
