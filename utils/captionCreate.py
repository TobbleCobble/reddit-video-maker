from PIL import Image, ImageDraw, ImageFont

## create images based on text -> image needs to look like a post on 
## reddit/generic social media post
## different image for title

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec condimentum est ac massa lobortis, eget vulputate lectus iaculis. Curabitur pellentesque tincidunt dui, ac interdum enim efficitur in. Sed bibendum neque non magna dignissim, vitae laoreet lacus malesuada. Cras at elementum nulla. Maecenas dapibus leo arcu, vitae aliquam mauris volutpat eu. Quisque tempus elementum rutrum. Nullam hendrerit luctus augue, eget mollis lectus sagittis sit amet. Nunc facilisis varius nulla, sed efficitur diam euismod ullamcorper."
username = "Lorem ipsum"

def titleImage(text):
    lines = []
    length = 0
    nextSpace = 0
    font = ImageFont.truetype("fonts/helvetica.ttf", 24)

    for i in range(len(text)):
        if i != 0:
            if i % 45 == 0:
                if text[i] == " ":
                    lines.append(text[length:i])
                    length = i
                else:
                    for j in range(len(text[:i])):
                        if text[j] == " ":
                            nextSpace = j
                    lines.append(text[length:nextSpace])
                    length = nextSpace
    
    lines.append(text[length:len(text)])

    text = ""
    for line in lines:
        if line[0] == " ":
            line = line[1:]
    
        text+= line + "\n"


    img = Image.new('RGB',(500,len(lines)*28+10),color=(30,30,30))
    d = ImageDraw.Draw(img)

    d.text((10,10), text,fill=(250,250,250), align="left", font=font)
    img.save("temp/0_title.png")


def commentImage(username, text, num):
    lines = []
    length = 0
    nextSpace = 0
    font = ImageFont.truetype("fonts/helvetica.ttf", 20)

    for i in range(len(text)):
        if i != 0:
            if i % 45 == 0:
                if text[i] == " ":
                    lines.append(text[length:i])
                    length = i
                else:
                    for j in range(len(text[:i])):
                        if text[j] == " ":
                            nextSpace = j
                    lines.append(text[length:nextSpace])
                    length = nextSpace
    
    lines.append(text[length:len(text)])   

    lines.insert(0, "      "+username)
    lines.insert(1, " ")

    text = ""
    for line in lines:
        if line[0] == " ":
            line = line[1:]
    
        text+= line + "\n"


    img = Image.new('RGB',(500,len(lines)*26+10),color=(30,30,30))
    d = ImageDraw.Draw(img)

    d.text((10,10), text,fill=(250,250,250), align="left", font=font)
    img.save("temp/"+str(num)+"_"+username+'.png')


if __name__ == "__main__":
    commentImage(username, text, 0)
    titleImage("what's 9 + 10??")