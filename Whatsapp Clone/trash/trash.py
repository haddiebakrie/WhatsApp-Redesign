def chat_builder(self, profile, screen):
        usermsg, friendmsg, last = profile['msg'].values()
        if len(usermsg) >= len(friendmsg):
            j = len(usermsg) 
        else: 
            j = len(friendmsg)
        i = 0
        for i in range(j):
            try:
                if type(usermsg[i]) == list:
                    for msg in usermsg[i]:
                        self.chatmsg = Message()
                        self.chatmsg.text, self.chatmsg.timestamp, self.chatmsg.state = msg.split(';')
                        self.chatmsg.sender = 'user'
                        self.chatmsg.rt = ChatScreen()
                        screen.ids['messages'].add_widget(self.chatmsg)
                else:
                    self.chatmsg = Message()
                    self.chatmsg.text, self.chatmsg.timestamp, self.chatmsg.state = usermsg[i].split(';')
                    self.chatmsg.sender = 'user'
                    self.chatmsg.rt = ChatScreen()
                    screen.ids['messages'].add_widget(self.chatmsg)
                if type(friendmsg[i]) == list:
                    for msg in friendmsg[i]:
                        self.chatmsg = Message()
                        self.chatmsg.text, self.chatmsg.timestamp, self.chatmsg.state = msg.split(';')
                        self.chatmsg.sender = 'friend'
                        self.chatmsg.rt = ChatScreen()
                        screen.ids['messages'].add_widget(self.chatmsg)
                else:
                    self.chatmsg = Message()
                    self.chatmsg.text, self.chatmsg.timestamp, self.chatmsg.state = friendmsg[i].split(';')
                    self.chatmsg.sender = 'friend'
                    self.chatmsg.rt = ChatScreen()
                    screen.ids['messages'].add_widget(self.chatmsg)
                i += 1
            except IndexError:
                pass


<Message>:
    sender: 'user'
    orientation: 'vertical'
    text: ''
    size: self.texture_size
    size_hint_x: None
    size_hint_y: None
    text_size: root.width, None
    multiline: True
    font_size: 14
    theme_text_color:'Custom'
    text_color: [1, 1, 1, 1]
    bold: True
    pos_hint: {'left': 1} if self.sender == 'friend' else {'right': 1}
    radius: [0, 10, 10, 10] if self.sender == 'friend' else [10, 0, 10, 10]
    canvas.before: 
        Color:
            rgba: app.theme_cls.accent_color if self.sender == 'friend' else [.5, .5, .5, 1]
        RoundedRectangle:
            radius: root.radius
            pos: self.pos[0] - 5, self.pos[1] - 5
            size: self.size[0] + 15, self.size[1] + 15