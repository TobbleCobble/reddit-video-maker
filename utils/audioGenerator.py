import pyttsx3


engine = pyttsx3.init()

voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

def soundify(post):

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    for i in range(len(post)):
        if i == 0:
            engine.save_to_file(post[i].title, "temp/temp"+str(i)+".mp3")
            engine.runAndWait()
        else:
            engine.save_to_file(post[i].body, "temp/temp"+str(i)+".mp3")
            engine.runAndWait()
'''   
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()
'''