from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
import random
import os

## create images based on text -> image needs to look like a post on 
## reddit/generic social media post
## different image for title

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec condimentum est ac massa lobortis, eget vulputate lectus iaculis. Curabitur pellentesque tincidunt dui, ac interdum enim efficitur in. Sed bibendum neque non magna dignissim, vitae laoreet lacus malesuada. Cras at elementum nulla. Maecenas dapibus leo arcu, vitae aliquam mauris volutpat eu. Quisque tempus elementum rutrum. Nullam hendrerit luctus augue, eget mollis lectus sagittis sit amet. Nunc facilisis varius nulla, sed efficitur diam euismod ullamcorper."
username = "Lorem ipsum"

def titleImage(text, username, subreddit):
    lines = []
    length = 0
    nextSpace = 0
    font = ImageFont.truetype("fonts/helvetica.ttf", 24)
    userFont = ImageFont.truetype("fonts/helvetica.ttf", 20)

    lines = textwrap.wrap(text, width=45)

    lines.insert(0, "      ")
    lines.insert(0, "      ")
    lines.insert(0, "      ")

    text = '\n'.join(lines)

    icon = []
    size = (60, 60)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=255)

    for icons in os.listdir("subreddit_icon"):
        if ".png" in icons:

            im = Image.open('subreddit_icon/'+subreddit[2:]+".png")
            im = im.convert('RGBA')
            im = im.resize((60,60))
            
            icon.append(im)

    pfp = icon[0]


    img = Image.new('RGB',(500,len(lines)*28+10),color=(30,30,30))
    d = ImageDraw.Draw(img)

    d.text((10,10), text,fill=(250,250,250), align="left", font=font)
    d.text((70,10), subreddit,fill=(250,250,250), align="left", font=font)
    d.text((80,35), username,fill=(200,200,200), align="left", font=userFont)

    img.paste(pfp,(5,5),mask)
    img.save(username+"/0_title.png")


def commentImage(username, text, num, sectionid, asker):
    font = ImageFont.truetype("fonts/helvetica.ttf", 20)
    userFont = ImageFont.truetype("fonts/helvetica.ttf", 15)
    
    para = textwrap.wrap(text, width=52)

    text = '\n'.join(para)

    print(text)

    img = Image.new('RGB',(500,(text.count("\n")+1)*21+10),color=(30,30,30))
    d = ImageDraw.Draw(img)

    
    


    d.text((10,10), text,fill=(250,250,250), align="left", font=font)

    sectionid = str(sectionid)

    if len(sectionid) < 2:
        sectionid = "0" + sectionid

    img.save(str(asker)+"/"+str(num)+"_"+str(username)+"_"+str(sectionid)+'.png')


if __name__ == "__main__":
    commentImage(username, text, 0, 0, "john")
    titleImage("what's 9 + 10??", "john", "r/amitheasshole")