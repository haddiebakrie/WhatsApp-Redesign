from components.messagelabel import MessageLabel
from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty, BooleanProperty
from kivymd.uix.button import MDIconButton
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.app import App
import os


Builder.load_file(os.path.join(os.path.dirname(__file__), 'messagescreen.kv'))


class MessageScreen(MDScreen):
	focus_state = BooleanProperty()
	

	messages = ListProperty()
	time = StringProperty()
	username = StringProperty('')
	source = StringProperty('')
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.camera_btn = MDIconButton(icon='camera')
		Clock.schedule_once(self.custom_init, 1)

	def custom_init(self, *args):
		self.app = App.get_running_app()
		self.rv = self.ids.message_rv
		self.screen_manager = self.app.root.screen_manager
		values = [{'message_id': 1, 'text': 'Bernice', 'side': 'right', 'bg_color': '#223344', 'text_size': [None, None]}, {'message_id': 2, 'text': 'do you really think so?', 'side': 'left', 'bg_color': '#332211', 'text_size': [None, None]}]
		self.app.messages.extend(values)
	def add_message(self, text, side, color):
		# create a message for the recycleview
		self.messages.append({
			'message_id': len(self.messages),
			'text': text,
			'side': side,
			'bg_color': color,
			'text_size': [None, None],
		})
		self.app.messages.append({
			'message_id': len(self.messages),
			'text': text,
			'side': side,
			'bg_color': color,
			'text_size': [None, None],
		})
		self.rv.data = self.app.messages

    

	@staticmethod
	def focus_textinput(textinput):
		textinput.focus = False

	def send_message(self, textinput):
		print('sending message')
		text = textinput.text
		textinput.text = ''
		self.add_message(text, 'right', '#223344')
		self.focus_textinput(textinput)
		Clock.schedule_once(lambda *args: self.answer(text), 1)
		self.scroll_bottom()

	def answer(self, text, *args):
		print('answered message')
		self.add_message('do you really think so?', 'left', '#332211')

	def scroll_bottom(self):
		rv = self.ids.message_rv
		box = self.ids.message_box
		if rv.height < box.height:
			Animation.cancel_all(rv, 'scroll_y')
			Animation(scroll_y=0, t='out_quad', d=.5).start(rv)
	def load_resource(self, source='', username='Joe Doe', time='online'):
		self.source = source
		self.username = username
		self.time = time
	def back_btn(self):
		''' return to the previous screen'''
		self.screen_manager.current = 'home'
	def focus_callback(self, *args):
		self.focus_state = True
		if self.focus_state:
			print('focussing')
			self.ids.language_btn.pos_hint = {'center_x':0.86, 'center_y':0.5}
			self.ids.attachment_btn.pos_hint = {'center_x':0.96, 'center_y':0.5}
			self.ids.send_microphone_btn.icon = 'send'
			self.ids.input_layout.remove_widget(self.camera_btn)
			self.focus_state = False
	def on_focus_state(self, instance, value):
		if value:
			self.unfocus_callback()


	def unfocus_callback(self, *args):
		print('unfocusing')
		self.ids.language_btn.pos_hint = {'center_x':0.7, 'center_y':0.5}
		self.ids.attachment_btn.pos_hint = {'center_x':0.8, 'center_y':0.5}
		if self.camera_btn in  self.ids.input_layout.children[:]:
			pass
		else: 
			
			self.ids.input_layout.add_widget(self.camera_btn)
			self.camera_btn.pos_hint = {'center_x':0.9, 'center_y':0.5}
		