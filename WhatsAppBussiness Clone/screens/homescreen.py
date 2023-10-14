from kivymd.uix.floatlayout import MDFloatLayout
from components.screentab import ScreenTab
from components.chatitem import ChatItem
from components.statusitem import StatusItem
from screens.chatscreen import ChatScreen
from screens.groupscreen import GroupScreen
from screens.statusscreen import StatusScreen
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'homescreen.kv'))

class HomeScreen(MDFloatLayout):
	pass