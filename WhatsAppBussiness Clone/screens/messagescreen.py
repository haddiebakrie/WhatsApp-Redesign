
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.app import App
import os


Builder.load_file(os.path.join(os.path.dirname(__file__), 'messagescreen.kv'))

class MessageScreen(MDScreen):
	pass