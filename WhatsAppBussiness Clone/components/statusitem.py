from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.app import App
import os


Builder.load_file(os.path.join(os.path.dirname(__file__), 'statusitem.kv'))

class StatusItem(TwoLineAvatarIconListItem):
	source = StringProperty('')
	username = StringProperty('')
	date = StringProperty('')


	def on_release(self, *args):
		app = App.get_running_app()
		screen_manager = app.root.screen_manager
		screen_manager.current = 'status'
		status_screen = screen_manager.get_screen('status')
		status_screen.load_resource(source=self.source, status_source=self.source, username=self.username, time=self.date)



		#print(screen_manager.current)