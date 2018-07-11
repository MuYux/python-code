from PIL import Image,ImageDraw,ImageFont

img = Image.open('photo.jpg')

draw=ImageDraw.Draw(img)
myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
fillcolor = "#ff0000"
w,h=img.size
draw.text((w-45,0),'99',font=myfont,fill=fillcolor)
img.show()