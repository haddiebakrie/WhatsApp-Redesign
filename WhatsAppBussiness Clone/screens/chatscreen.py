from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'chatscreen.kv'))

class ChatScreen(MDFloatLayout):
	chat_container = ObjectProperty()
	
	def load_chats(self):
		data = [{'source':'assests/images/17.jpg', 'username':'My Love', 'message':'Good Morning Love', 'date':'Today', 'time':'10:12 AM'}
		for i in range(500)]
		self.chat_container.data = data



