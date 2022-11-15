import pyautogui
import pytesseract


def main():
    while True:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        im1 = pyautogui.screenshot("SC.png", region=(1798, 940, 60, 20))
        text = pytesseract.image_to_string(im1)
        #print(text)
        parsed = text[0:-4]
        #print(parsed)
        if parsed:
            try:
                int(parsed)
                print("MILS: {}, distance: {:.0f}".format(parsed, mil_to_dist(parsed)))
            except ValueError as e:
                pass
    return


def mil_to_dist(mils):
    return (int(mils) - 1000) / -0.235


main()
