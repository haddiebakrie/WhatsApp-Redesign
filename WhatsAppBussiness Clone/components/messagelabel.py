from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, ListProperty
from kivy.app import App
from kivy.animation import Animation

from kivy.lang import Builder
from kivy.metrics import dp
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'messagelabel.kv'))

class MessageLabel(MDFloatLayout):
	messages = ListProperty()
	
	def update_message_size(self, message_id, texture_size, max_width):
		# when the label is updated, we want to make sure the displayed size is
		# proper
		app = App.get_running_app()
		self.messages = app.messages 
		print(message_id)
		if max_width == 0:
			return

		one_line = dp(50)  # a bit of  hack, YMMV

		# if the texture is too big, limit its size
		if texture_size[0] >= max_width * 2 / 3:
			self.messages[message_id] = {
				**self.messages[message_id],
				'text_size': (max_width * 2 / 3, None),
			}

		# if it was limited, but is now too small to be limited, raise the limit
		elif texture_size[0] < max_width * 2 / 3 and \
			texture_size[1] > one_line:
			self.messages[message_id] = {
			**self.messages[message_id],
			'text_size': (max_width * 2 / 3, None),
			'_size': texture_size,
			}

		# just set the size
		else:
			self.messages[message_id] = {
				**self.messages[message_id],
				'_size': texture_size,
			}