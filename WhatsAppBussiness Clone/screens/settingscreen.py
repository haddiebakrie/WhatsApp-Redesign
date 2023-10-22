from kivymd.uix.list import TwoLineAvatarIconListItem, TwoLineIconListItem, ILeftBodyTouch
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'settingscreen.kv'))



class LeftContainer(ILeftBodyTouch, FitImage):
	pass
	
class TwoLineIconItem(TwoLineAvatarIconListItem):
	icon = StringProperty()
	action = StringProperty()
	description = StringProperty()

class SettingScreen(MDScreen):
	def chevron_back(self):
		app = MDApp.get_running_app()
		app.root.screen_manager.current = 'home'
