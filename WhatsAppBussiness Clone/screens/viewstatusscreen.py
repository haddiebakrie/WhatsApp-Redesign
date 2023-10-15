from kivymd.uix.screen import MDScreen
from kivy.animation import Animation 
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.list import IRightBodyTouch, ILeftBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.app import App
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'viewstatusscreen.kv'))

class RightContainer(IRightBodyTouch, MDBoxLayout):
		pass
'''
class LeftContainer(ILeftBodyTouch, MDBoxLayout):
	pass

'''
class ViewStatusScreen(MDScreen):
	source = StringProperty()
	status_source = StringProperty()
	username = StringProperty()
	time = StringProperty('00:00')
	progressbar = ObjectProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		Clock.schedule_once(self.custom_init, 1)

	def custom_init(self, *args):
		app = App.get_running_app()
		self.screen_manager = app.root.screen_manager


	def load_resource(self, source='', status_source='', username='', time='00:00'):
		''' load information to the status '''
		self.source = source
		self.status_source = status_source
		self.username = username
		self.time = time

		Clock.schedule_once(self.animate_pregress_bar)

	def animate_pregress_bar(self, args):
		''' animate the progress of the status '''
		self.anim = Animation(duration=5, value=100)
		self.anim.bind(on_complete=self.complete)
		self.anim.start(self.progressbar)

	def complete(self, *args):
		
		self.progressbar.value = 0
		self.screen_manager.current = self.screen_manager.previous()
	
	def back_btn(self):
		''' return to the previous screen'''
		if self.anim:
			self.anim.stop(self.progressbar)
		else:
			self.screen_manager.current = self.screen_manager.previous()






