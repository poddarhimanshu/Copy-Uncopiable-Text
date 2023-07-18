# for OCR
import pytesseract
import json
import cv2 

with open('config.json') as config_file:
    config = json.load(config_file)
pytesseract.pytesseract.tesseract_cmd = config['pytesseractpath']

class TesseractOCR:
    @staticmethod
    def GetText(imagePath):
        image = cv2.imread(imagePath) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        text = pytesseract.image_to_string(image)
        return text