from gtts import gTTS

import os

mytext = 'write here'

language = 'es'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("audio.mp3")

os.system("mpg321 audio.mp3")