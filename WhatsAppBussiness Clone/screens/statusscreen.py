from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'statusscreen.kv'))

class StatusScreen(MDFloatLayout):
	status_container = ObjectProperty()
	def load_status(self):
		data = [{'source':'assests/images/19.jpg', 'username':'bernice', 'date':'Today'}
		for i in range(10)]
		self.status_container.data = data