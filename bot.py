import time
import pyautogui
import pyscreenshot as ImageGrab

x1 = 550.0

def capture_screen():
    ''' Capture screen '''
    screen = ImageGrab.grab()
    return screen

def detect_enemy(screen):
    ''' Detect enemy based on color '''
    aux_color = screen.getpixel((int(x1), 246))
    for x in range(int(x1), int(x1+50)):
        for y in range(246, 276):
            color = screen.getpixel((x, y))
            if color != aux_color:
                return True
            else:
                color = aux_color

def jump():
    ''' Makes dinosaur jump '''
    global x1
    pyautogui.press('up')
    x1 += 0.5


print('Starting in 3 seconds...')
time.sleep(3)
pyautogui.press('up')

while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump() 
