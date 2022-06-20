from PIL import Image

picpath = './gyros.jpg'

class Overlay:

    def __init__(self):
        print('Overlay object created.')

    def openImage(self, img):
        try:
            img = Image.open(img)
        except IOError:
            print('Error occured opening picture')
        return img

    def getImageSize(self, img):
        if isinstance(img, str):
            img = self.openImage(img)
        width, height = img.size
        print(f"Width: {width} px\nHeight: {height} px")



O = Overlay()
img = O.openImage(picpath)
O.getImageSize(picpath)

