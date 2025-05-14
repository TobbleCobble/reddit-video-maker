import pyttsx3
import random

engine = pyttsx3.init()

voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)


def soundifyAuthor(title, asker):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[random.randrange(0,2)].id)

    engine.save_to_file(title, "temp/"+asker+"/temp"+"0"+".mp3")
    engine.runAndWait()


def soundifyComment(comment, index, sectionid, asker):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.save_to_file(comment, "temp/"+asker+"/temp"+str(index)+"_"+str(sectionid)+".mp3")
    engine.runAndWait()

def soundifyPost(comment, index, sectionid, asker):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    ## make numbers appear 01, 02, ... 09, 10, 11 to maintain order in directory
    if len(str(sectionid)) < 2:
        sectionid = "0" + str(sectionid)

    engine.save_to_file(comment, "temp/"+asker+"/temp"+str(index)+"_"+str(sectionid)+".mp3")
    engine.runAndWait()