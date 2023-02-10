#importing all libraries required
from winotify import Notification,audio
from random import choice


#this code only works on windows operating aystem


# func that notifies the user
def notify(title="title",message="message",icon="python.png"):
	win = Notification(app_id="PYWINDOWSNOTIFYER",
		title=title,
		msg=message,
		duration="long",
		icon=icon,

		)
	win.set_audio(choice([audio.Mail,audio.SMS,audio.LoopingCall]),loop=False)
	win.add_actions(label="about creater",launch="https://github.com/Yuheshpandian")
	win.show()

title="INSTANCE Message"
message=choice(["HI EVERYONE HOW ARE YOU.HOPE YOU ARE FINE.","HEY PYTHON FANS HOPE YOU'RE DOING GOOD","HI CODING FANS","HEY WINDOW USERS","HELLO EVERYONE!","HOW IS THIS"])

# to modify the notification uncomment the next multiline comment
"""
title=input("enter the title of the notification")
message=input("enter what message you want to see")
"""

#to change the icon just give an path of the icon after message parameter
#notify(title,message,path)


notify(title,message)