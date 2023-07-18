# for screenshot
from PIL import Image
import win32clipboard as clip
import win32con
from io import BytesIO


class Screenshot:
    @staticmethod
    def CopyImageToClipBoard(imagePath):
        im = Image.open(imagePath) 
        output = BytesIO()
        im.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()
        clip.OpenClipboard()
        clip.EmptyClipboard()
        clip.SetClipboardData(win32con.CF_DIB, data)
        clip.CloseClipboard()
