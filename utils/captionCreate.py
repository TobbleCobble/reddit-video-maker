from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import random
import os
import textwrap
import json

## create images based on text -> image needs to look like a post on 
## reddit/generic social media post
## different image for title

try:
    with open('assets/design.json', 'r') as file:
        design_data = json.load(file)
except:
    print("[ERROR]: Cannot find file assets/design.json")


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec condimentum est ac massa lobortis, eget vulputate lectus iaculis. Curabitur pellentesque tincidunt dui, ac interdum enim efficitur in. Sed bibendum neque non magna dignissim, vitae laoreet lacus malesuada. Cras at elementum nulla. Maecenas dapibus leo arcu, vitae aliquam mauris volutpat eu. Quisque tempus elementum rutrum. Nullam hendrerit luctus augue, eget mollis lectus sagittis sit amet. Nunc facilisis varius nulla, sed efficitur diam euismod ullamcorper."
username = "Lorem ipsum"

def titleImage(text, username, subreddit):
    font = ImageFont.truetype(design_data["font"], 24)
    userFont = ImageFont.truetype(design_data["font"], 20)

    para = textwrap.wrap(text, width=45)

    para.insert(0, "      ")
    para.insert(0, "      ")
    para.insert(0, "      ")

    text = '\n'.join(para)

    icon = []
    size = (60, 60)

    image = Image.new('RGB',(500,text.count("\n")*28+20), color=tuple(design_data["background-colour"]))
    img = Image.new('RGBA', image.size)

    
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.rounded_rectangle((0, 0, 500,text.count("\n")*28+20), design_data["radius"], fill=tuple(design_data["background-colour"])[0])
    img.paste(image, (0,0), mask)

    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=tuple(design_data["background-colour"])[0])

    for icons in os.listdir("assets/subreddit_icon"):
        if ".png" in icons:

            im = Image.open("assets/subreddit_icon/"+subreddit[2:]+".png")
            im = im.convert('RGBA')
            im = im.resize((60,60))
            
            icon.append(im)

    pfp = icon[0]

    d = ImageDraw.Draw(img)

    d.text((10,10), text,fill=tuple(design_data["colour"]), align="left", font=font)
    d.text((70,10), subreddit,fill=tuple(design_data["colour"]), align="left", font=font)
    d.text((80,35), username,fill=tuple(design_data["colour"]), align="left", font=userFont)

    img.paste(pfp,(5,5),mask)
    img.save("temp/"+username+"/0_title.png")


def commentImage(username, text, num, sectionid, asker):
    font = ImageFont.truetype(design_data["font"], 20)
    userFont = ImageFont.truetype(design_data["font"], 15)

    para = textwrap.wrap(text, width=52)

    if sectionid == 0:
        para.insert(0, " ")
        para.insert(1, " ")

    text = '\n'.join(para)

    image = Image.new('RGB',(500,text.count("\n")*21+30), color=tuple(design_data["background-colour"]))
    img = Image.new('RGBA', image.size)
    d = ImageDraw.Draw(img)

    pfps = []
    
    size = (40, 40)

    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, 500,text.count("\n")*21+30), design_data["radius"], fill=tuple(design_data["background-colour"])[0])
    img.paste(image, (0,0), mask)

    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=tuple(design_data["background-colour"])[0])


    for pfp in os.listdir("assets/pfp"):
        if "pfp" in pfp:

            im = Image.open('assets/pfp/'+pfp)
            im = im.convert('RGBA')
            im = im.resize((40,40))
            
            pfps.append(im)

    pfp = pfps[random.randrange(0,5)]
    
    if sectionid == 0:
        d.text((10,10), text,fill=tuple(design_data["colour"]), align="left", font=font)
    
        d.text((50,15), username,fill=tuple(design_data["colour"]), align="left", font=userFont)

        img.paste(pfp, (5,5), mask)
    
    else:
        d.text((10,10), text,fill=tuple(design_data["colour"]), align="left", font=font)

    img.save("temp/"+asker+"/"+str(num)+"_"+username+"_"+str(sectionid)+'.png')

def textImage(username, text, num, sectionid):
    font = ImageFont.truetype(design_data["font"], 20)
    
    para = textwrap.wrap(text, width=52)
    text = '\n'.join(para)

    image = Image.new('RGB',(500,text.count("\n")*21+30), color=tuple(design_data["background-colour"]))
    img = Image.new('RGBA', image.size)

    
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.rounded_rectangle((0, 0, 500,text.count("\n")*21+30), design_data["radius"], fill=tuple(design_data["background-colour"])[0])
    img.paste(image, (0,0), mask)
    
    d = ImageDraw.Draw(img)
    d.text((10,10), text,fill=tuple(design_data["colour"]), align="left", font=font)

    sectionid = str(sectionid)

    if len(sectionid) < 2:
        sectionid = "0" + sectionid

    img.save("temp/"+str(username)+"/"+str(num)+"_"+str(username)+"_"+str(sectionid)+'.png')

if __name__ == "__main__":
    commentImage(username, text, 0, 0, "steve")
    titleImage("what's 9 + 10?? is it 21 or have i been lied to", "steve", "r/askreddit")
    textImage("steve", text, 0, 0)