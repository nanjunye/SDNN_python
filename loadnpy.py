from PIL import Image


img = Image.open('img2.jpg')
img = img.resize([175, 175])
img.show()



