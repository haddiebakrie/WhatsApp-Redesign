from kivymd.uix.screen import MDScreen
from components.screentab import ScreenTab
from components.chatitem import ChatItem
from components.statusitem import StatusItem
from screens.chatscreen import ChatScreen
from screens.groupscreen import GroupScreen
from screens.statusscreen import StatusScreen
from kivy.clock import Clock
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'homescreen.kv'))

class HomeScreen(MDScreen):
	
	def on_enter(self, *args):
		Clock.schedule_once(self.load,1)

	def load(self, interval):
		
		self.ids.chats.load_chats()
		self.ids.groups.load_groups()
		self.ids.status.load_status()
		
