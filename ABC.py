from PIL import Image, ImageFont, ImageDraw
import os

pth='c:\\Users\\aleksey\\Desktop\\ABC\\'

for i in range (97,123,1):
    img=Image.new('RGB',(100,100),'white')

    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=80)

    idraw.text((23, 10), chr(i), font=font,fill='black')
    #img.show()
    img.save(pth+chr(i)+'.png')

img = Image.new('RGB',(100,100),'white')
img.save(pth+'1.png')

img = Image.new('RGB',(100,100),'black')
img.save(pth+'2.png')

print(os.listdir(pth))
