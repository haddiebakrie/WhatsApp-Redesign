import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.properties import BooleanProperty, DictProperty, OptionProperty, StringProperty
from kivy.lang.builder import Builder
from demo.demo import profiles


Builder.load_file('story.kv')
Builder.load_file('chat_list_item.kv')
Builder.load_file('chat_screen.kv')
Builder.load_file('text_field.kv')

__version__ = '1.0.0'

Window.size = (320, 600)

class WindowManager(ScreenManager):
    '''A window manager to manage switching between screens. '''

class MessageScreen(Screen):
    '''A screen that display the stories and all message histories. '''

class StoryWithImage(MDBoxLayout):
    '''A horizontal layout with the user dp and the user name'''
    text = StringProperty() # To store the user's name
    source = StringProperty() #The path to the user's picture

class ChatListItem(MDCard):
    '''A clickable chat item for the chat timeline'''
    mssg = StringProperty() # To store the user's mssg
    friend_avatar = StringProperty() #The path to the user's picture
    timestamp = StringProperty() #The time the message was sent
    profile = DictProperty() #A user from demo.profile
    isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting']) #Message read status
    friend_name = StringProperty()

class ChatScreen(Screen):
    '''A screen that display messages with a user.'''
    text = StringProperty() #User's name
    image = StringProperty() #User Profile Picture
    active = BooleanProperty() # To chech if user is active

class MainApp(MDApp):
    def build(self):
        '''Initialize the application
        and return the root widget.'''

        # Setting theme properties.
        self.theme_cls.theme_style = 'Dark' #Dark theme
        self.theme_cls.primary_palette = 'Teal' #Main color palette
        self.theme_cls.accent_palette = 'Teal' #Second color palette  with 4oo hue value
        self.theme_cls_accent_hue = '400'
        self.title = 'WhatsApp Redesign'

        #Storing the screens in a list.
        screens = [
            MessageScreen(name='message'),
            ChatScreen(name='chat-screen')
        ]

        #Adding all screen in screens to the window manager
        self.wm = WindowManager(transition=FadeTransition()) # Creating an instance of Window manager and setting the animation when switching between screens
        for screen in screens:
            self.wm.add_widget(screen)

        self.story_builder()
        self.chat_list_builder()

        #Return the window manager.
        return self.wm

    def story_builder(self):
        '''Create a story for each user and add it to the story layout.'''
        for profile in profiles:
            self.story = StoryWithImage()
            self.story.text = profile['name']
            self.story.source = profile['image']
            self.wm.screens[0].ids['story_layout'].add_widget(self.story)

    def chat_list_builder(self):
        '''Create a chat list item for each user and add it to message list.'''
        for profile in profiles:
            for message in profile['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = profile
                self.chatitem.friend_name = profile['name']
                self.chatitem.friend_avatar = profile['image']

                # Spliting the message content
                lastMessage, time, isRead, sender = message.split(';')
                self.chatitem.mssg = lastMessage
                self.chatitem.timestamp = time
                self.chatitem.isRead = isRead
            self.wm.screens[0].ids['chatTimeLine'].add_widget(self.chatitem)

    def change_screen(self, screen):
        self.wm.current = screen

    def create_chat(self, profile):
        '''Get all user message and create a chat screen.'''
        self.chat_screen = ChatScreen()
        self.chat_screen.text = profile['name']
        self.chat_screen.image = profile['image']
        self.chat_screen.active = profile['active']
        self.wm.switch_to(self.chat_screen)




if __name__ == "__main__":
    MainApp().run()