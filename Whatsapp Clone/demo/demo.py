chats = {

    "anita": ["hey;2:20 PM;read;you", "hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "staying alive;2:20 PM;delivered;you"],
    "jooyce": ["what's the deal with that guy from earlier;2:20 PM;read;you", "seriously i dont know;2:20 PM;read;friend", "we re not good enough to help move? Lol.;2:20 PM;read;you", "Lol guess we re nt;2:20 PM;read;friend", 
        "you coming to bariat's;2:20 PM;read;you","yeah what time?;2:50 PM;read;friend", "hope its not late ;2:58 PM;read;friend"],
    "weeknd": ["hey;2:20 PM;read;you","hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "he really made a fool out of me;2:20 PM;delivered;you"],
    "jordan": ["hey;2:20 PM;read;you","hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "you keep crying to me;2:20 PM;delivered;you"],
    "breezy": ["hey;2:20 PM;read;you","hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "staying alive;2:20 PM;delivered;you"],
    "wizkid": ["hey;2:20 PM;read;you","hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "hopefully something comes up;2:20 PM;delivered;you"],
    "davido": ["hey;2:20 PM;read;you","hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "i am down here;2:20 PM;delivered;you"],
    "zendaya": ["hey;2:20 PM;read;you","hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "what tf were you thinking ;2:20 PM;delivered;you"],
    "rihanna": ["hey;2:20 PM;read;you","hi whats up;2:20 PM;read;friend", "how are you doing?;2:20 PM;read;you","doing great you?;2:20 PM;waiting;friend", 
        "i won bro;2:20 PM;delivered;you"],
}

anita = {
    "name": "Anita",
    "image": "assets/images/12.png",
    "active": True,
    "msg": chats["anita"],
    }

jooyce = {
    "name": "Jooyce",
    "image": "assets/images/16.jpg",
    "active": False,
    "msg": chats["jooyce"],
    }

weeknd = {
    "name": "Weeknd",
    "image": "assets/images/weeknd.jpg",
    "active": True,
    "msg": chats["weeknd"],
    }

jordan = {
    "name": "Jordan",
    "image": "assets/images/jordan.jpg",
    "active": False,
    "msg": chats["jordan"],
    }

breezy = {
    "name": "Breezy",
    "image": "assets/images/breezy.jpg",
    "active": True,
    "msg": chats["breezy"],
    }

wizkid = {
    "name": "Wizkid",
    "image": "assets/images/wizkid.jpg",
    "active": False,
    "msg": chats["wizkid"],
    }

davido = {
    "name": "Davido",
    "image": "assets/images/davido.jpg",
    "active": False,
    "msg": chats["davido"],
    }

zendaya = {
    "name": "Zendaya",
    "image": "assets/images/14.jpg",
    "active": False,
    "msg": chats["zendaya"],
    }

rihanna = {
    "name": "Rihanna",
    "image": "assets/images/rihanna.png",
    "active": True,
    "msg": chats["rihanna"],
    }

profiles = [anita, jooyce, weeknd, jordan, breezy, wizkid, davido, zendaya, rihanna]

print(profiles[0]["msg"])
# print(anita.items())
# chats.items