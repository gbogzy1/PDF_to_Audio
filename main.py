from PyPDF2 import PdfReader
from gtts import gTTS
import os
from PyPDF2 import PdfReader


pdf = 'htbcasestudy.pdf'


def pdftoaudio(pdf):
    reader = PdfReader(pdf)
    print(len(reader.pages))

    num_pages = len(reader.pages)
    if num_pages > 0:
        for page in range(num_pages):
            clean_text = reader.pages[page].extract_text().strip().replace('\n', ' ')
            print(clean_text)
    else:
        print("Please check your pdf file and run again ")
    language = 'en'


    obj = gTTS(text=clean_text, lang=language, slow=False)

    obj.save('testpdftoaudio.mp3')


pdftoaudio(pdf)