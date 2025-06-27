import pytesseract, pyautogui, time, datetime
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract\tesseract' #substitute with your file path here

results_a = []
results_b = []

def filter_non_digits(string):
    result = ''
    for char in string:
        if char in '1234567890':
            result += char
    if result == "":
        result = "0"
    return result 

def search(term):
    pyautogui.click(x=1700, y=55)
    pyautogui.write(term)
    pyautogui.press('enter')
    time.sleep(2)
    screenshot = pyautogui.screenshot()
    box_coords = (1350, 100, 1550, 135)
    region = screenshot.crop(box_coords)
    pyautogui.click(x=1790, y=55)
    return filter_non_digits(pytesseract.image_to_string(region))

#start
word = "word"
name1 = "name1"
name1 = "name2"
filename = "cats.txt"
today = datetime.datetime.today()
numdays = int(input("Starting from how many days ago? ")) + 1
time.sleep(5)
dateList = []
for x in range (0, numdays):
    a_date = (str(today - datetime.timedelta(days = x))).split(" ")[0]
    results_a.append(search(word + " during:" + a_date + " from:" + name1))
    results_b.append(search(word + " during:" + a_date + " from:" + name2))

results_a = list(reversed(results_a))
results_b = list(reversed(results_b))

with open(filename, "w") as file:
    file.write("")

with open(filename, "a") as file:
    file.write(nome1 +", " + nome2 + "\n")
    for index in range (0, (len(results_a))):
        file.write(results_a[index] + ", " + results_b[index] +" \n")
