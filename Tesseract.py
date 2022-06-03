import re
import cv2 as cv
import pytesseract
from os import walk

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# img = cv.imread('0.png')

# print(ocr_core(img))

# f = []
# for (dirpath, dirnames, filenames) in walk("cropped_images"):
#     f.extend(filenames)
#     break
# print(f)

# for i in f:
#     img = cv.imread('cropped_images/'+i)
#     print(i + " : " + ocr_core(img))

def textRecognizer(img_path):
    img = cv.imread(img_path)
    text = ocr_core(img)
    return text.replace('''''','')
    