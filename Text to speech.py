from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = "en"
sp = gTTS(text= """Flow control is a high-level way of programming a computer to make decisions."
                These decisions can be simple or complicated, executed once or multiple times.
                The syntax for the different flow control mechanisms varies, but what they all share is that they
determine an execution pathway for the program. Python has relatively few forms of
flow control. They are conditionals, exceptions, and loops.""", lang=language, slow=False)
sp.save(audio)
playsound(audio)