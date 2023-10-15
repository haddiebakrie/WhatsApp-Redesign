from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'chatitem.kv'))

class RightContainer(IRightBodyTouch, MDBoxLayout):
		pass

class LeftContainer(ILeftBodyTouch, MDBoxLayout):
	pass

class ChatItem(TwoLineAvatarIconListItem):
	source = StringProperty()
	username = StringProperty()
	message = StringProperty()
	time = StringProperty()
	date = StringProperty()
	check_icon = StringProperty('numeric-1-circle')