# OCR(사진 속 문자 판독기) : 구글 AI Tesseract OCR 이용

import pytesseract 
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

a = Image.open('영수증.jpg')
result =pytesseract.image_to_string(a, lang='kor')

print(result)