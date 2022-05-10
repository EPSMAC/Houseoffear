from PIL import Image
def Picture():
    #read the image
    im = Image.open("myqr.png")

    #show image
    im.show()