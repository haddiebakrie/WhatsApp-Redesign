from kivymd.uix.list import TwoLineAvatarIconListItem, TwoLineIconListItem
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file_-), 'settingscreen.kv'))

class TwoLineListItem(TwoLineAvatarIconListItem):
	source = StringProperty()
	username = StringProperty()
	about = StringProperty()
	pass
class TwoLineIconItem(TwoLineIconListItem):
	icon = StringProperty()
	action = StringProperty()
	description = StringProperty()

class SettingScreen(MDScreen):
	pass
