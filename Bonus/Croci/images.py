'''
Funzioni di utilita' per leggere e salvare una immagine nella nostra codifica.
Utilities to load/save a PNG file to our encoding.
'''
import png
import io
import IPython.display as ipd 

def load(filename):
    """ Loads a PNG-8 image from the "filename" file.
        Returns a matrix (list of lists) of pixels.
        Every pixel is a triple (r, g, b) with the intensity of the three
        screen colours, expressed as a number ranging between 0 and 255
        (included), where:
            - r stands for red;
            - g stands for green;
            - b stands for blue.
    """
    with open(filename, mode='rb') as f:
        reader = png.Reader(file=f)
        try:
            w, h, png_img, _ = reader.asRGB8()
        except:
            raise ValueError("WARNING: The image has a transparency channel.")
        w *= 3
        return [ [ (line[i],line[i+1],line[i+2]) for i in range(0, w, 3) ]
                 for line in png_img ]


def save(img, filename):
    """ Saves the "img" image in the "fname" file using the PNG-8 encoding.
        img is a matrix (list of lists) of pixels.
        Every pixel is a triple (r, g, b) with the intensity of the three
        screen colours, expressed as a number ranging between 0 and 255
        (included), where:
            - r stands for red;
            - g stands for green;
            - b stands for blue.
    """
    png_img = png.from_array(img, 'RGB')
    png_img.save(filename)


class Image:
    """ Represents an image as a list of (R, G, B) triples, each denoting a
        pixel. Its _repr_png_() method enables IPython consoles, QTConsoles and
        notebooks to display the image.
    """
    def __init__(self, img):
        self.pixels = img

    def _repr_png_(self):
        '''Creates a binary representation of the image in a PNG format'''
        img = png.from_array(self.pixels, 'RGB')
        b = io.BytesIO()
        img.save(b)
        return b.getvalue()

def visd(img, caption=''):
    """ Displays an image in an IPython console, optionally followed by a
        caption.
    """
    ipd.display(Image(img))
    if caption:
        print(caption)
