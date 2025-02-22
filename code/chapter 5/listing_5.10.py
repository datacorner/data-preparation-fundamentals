import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

"""
    Installing Tesseract on windows
        1) Download the Tesseract OCR installer for Windows from its official repositor
            * Tesseract GitHub Releases (https://github.com/tesseract-ocr/tesseract)
            * Or directly from UB Mannheim's Tesseract for Windows (https://github.com/UB-Mannheim/tesseract/wiki) 
        2) Run the installer and complete the installation process. During installation, note the directory where Tesseract is 
           installed (e.g., C:\Program Files\Tesseract-OCR).
        3) Add Tesseract to the PATH
        Ex. C:\Program Files\Tesseract-OCR
    Installing Tesseract on Linux:
        Run on the CLI: sudo apt install tesseract-ocr
        
    Install the Python Tesseract Library pip: via pip install pytesseract
"""

if __name__ == "__main__":
    img = Image.open("../data/images/test-image.png")

    plt.imshow(img)
    plt.axis('off')
    plt.show()

    text = pytesseract.image_to_string(img)
    print("Extracted text:")
    print(text) 
