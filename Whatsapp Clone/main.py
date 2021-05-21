import kivy
from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, OptionProperty, StringProperty
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.picker import MDThemePicker
from kivy.uix.scrollview import ScrollView
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.list import OneLineAvatarIconListItem
from demo.demo import profiles
import demo.group
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Builder.load_file('kvs/pages/group_screen.kv')
Builder.load_file('kvs/pages/call_screen.kv')
Builder.load_file('kvs/pages/chat_screen.kv')
Builder.load_file('kvs/widgets/story_layout.kv')
Builder.load_file('kvs/widgets/avatar.kv')
Builder.load_file('kvs/widgets/chat_list_item.kv')
Builder.load_file('kvs/widgets/group_list_item.kv')
Builder.load_file('kvs/widgets/call_list_item.kv')
Builder.load_file('kvs/widgets/bottom_navigator.kv')
Builder.load_file('kvs/widgets/text_field.kv')
Builder.load_file('kvs/widgets/chatbubble.kv')

Window.size = (320, 600)

class WindowManager(ScreenManager):
    '''A window manager to manage switching between sceens.'''

class MessageScreen(Screen):
    '''A screen that display the story fleets and all message histories.'''

class CallScreen(Screen):
    '''A screen that display the call histories.'''

class ChatScreen(Screen):
    '''A screen that display messages with a user.'''

    text = StringProperty()
    image = ObjectProperty()
    active = BooleanProperty(defaultvalue=False)

class StoryWithImage(MDBoxLayout):
    '''A horizontal layout with an image(profile picture)
        and a text(username) - The Story.'''

    text = StringProperty()
    source = StringProperty()

class ChatListItem(MDCard):
    '''A clickable chat item for the chat timeline.'''

    isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting'])
    friend_name = StringProperty()
    mssg = StringProperty()
    timestamp = StringProperty()
    friend_avatar = StringProperty()
    profile = DictProperty()

class GroupListItem(MDCard):
    '''A clickable chat item for the group chat timeline.'''

    isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting'])
    group_name = StringProperty()
    group_avatar = StringProperty()
    friend_mssg = StringProperty()
    timestamp = StringProperty()

class ChatBubble(MDBoxLayout):
    '''A chat bubble for the chat screen messages.'''

    profile = DictProperty()
    msg = StringProperty()
    time = StringProperty()
    sender = StringProperty()
    isRead = OptionProperty('waiting', options=['read', 'delivered', 'waiting'])

class GroupScreen(Screen):
    '''A screen that display messages history in groups .'''

class Message(MDLabel):
    '''A adaptive text for the chat bubble.'''

class MainApp(MDApp): 
    ''' The main App class using kivymd's properties.'''

    def build(self): 
        ''' Initializes the Application
        and returns the root widget'''
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.accent_hue = '400'
        self.title = "WhatsApp"
        self.wm = WindowManager(transition=FadeTransition())
        screens = [
            MessageScreen(name='message'), GroupScreen(name='group'), CallScreen(name='call'), 
            ChatScreen(name='chat')
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        self.story_builder()
        self.chatlist_builder()
        self.grouplist_builder()

        return self.wm

    def change_screen(self, screen):
        '''Change screen using the window manager.'''
        self.wm.current = screen

    def show_theme_picker(self):
        '''Display a dialog window to change app's color and theme.'''
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def create_chat(self, profile):
        '''Get all messages and create a chat screen'''
        self.chat_screen = ChatScreen()
        self.msg_builder(profile, self.chat_screen)
        self.chat_screen.text = profile['name']
        self.chat_screen.image = profile['image']
        self.chat_screen.active = profile['active']
        self.wm.switch_to(self.chat_screen)

    def story_builder(self):
        '''Create a Story for each user and
        adds it to the story layout'''
        for profile in demo.demo.profiles:
            self.story = StoryWithImage()
            self.story.text = profile['name']
            self.story.source = profile['image']
            self.wm.screens[0].ids['story_layout'].add_widget(self.story)

    def chatlist_builder(self):
        '''Create a Chat List Item for each user and
        adds it to the Message List'''
        for messages in profiles:
            for message in messages['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = messages
                self.chatitem.friend_name = messages['name']
                self.chatitem.friend_avatar = messages['image']

                lastmessage, time, isRead, sender = message.split(';')
                self.chatitem.mssg = lastmessage
                self.chatitem.timestamp = time
                self.chatitem.isRead = isRead
                self.chatitem.sender = sender
            self.wm.screens[0].ids['chatlist'].add_widget(self.chatitem)

    def msg_builder(self, profile, screen):
        '''Create a message bubble for creating chat.'''
        for prof in profile['msg']:
            for messages in prof.split("~"):
                if messages != "":
                    message, time, isRead, sender = messages.split(";")
                    self.chatmsg = ChatBubble()
                    self.chatmsg.msg = message
                    self.chatmsg.time = time
                    self.chatmsg.isRead = isRead
                    self.chatmsg.sender = sender
                    screen.ids['msglist'].add_widget(self.chatmsg)
                else:
                    print("No message")

                print(self.chatmsg.isRead)

    def grouplist_builder(self):
        '''Create a Chat List Item for each group and
        adds it to the Group List'''
        for group in demo.group.groups:
            self.groupitem = GroupListItem()
            self.groupitem.group = group
            self.groupitem.group_name = group['name']
            self.groupitem.group_avatar = group['image']
            self.groupitem.friend_mssg, self.groupitem.timestamp, self.groupitem.isRead = group['msg'].split(';')
            self.wm.screens[1].ids['grouplist'].add_widget(self.groupitem)   

if __name__ == "__main__":
    MainApp().run()