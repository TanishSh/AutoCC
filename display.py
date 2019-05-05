import pygame as pg
import os, time, queue, win32con, win32gui, pywintypes, win32api
import speech_recognition as sr
import json

q = queue.Queue()
x = 400
y = 350
color = [255, 255, 255]
black = [0, 0, 0]

def recognize_speech():

    test = sr.AudioFile("file.wav")
    r = sr.Recognizer()
    with test as source:
        audio = r.record(source)
        # r.recognize_google_cloud(audio, open_json())
    return r.recognize_google_cloud(audio, open_json())

def open_json():
    with open('AutoCC-9917161c773d.json') as json_file:
        data = json.load(json_file)
        str_data = json.dumps(data)
        #print(data)
        return str_data


def queue():
    # innie = recognize_speech()
    # q.put(innie)
    return

def dequeue(screen):
    innie = recognize_speech()
    q.put(innie)
    if(q.empty()):
        #print("Empty queue")
        pg.display.flip()
    else:

        update_text(q.get(), screen)


def update_text(input, screen):
    # pick a font you have and set its size
    myfont = pg.font.SysFont("Times New Roman", 18)
    # apply it to text on a label
    label = myfont.render(input, 1, color)
    # put the label object on the screen at point x=100, y=100
    #print("Writing: " + str(input))
    screen.blit(label, (50, 20))
    # show the whole thing
    pg.display.flip()
    time.sleep(4)
    screen.fill(black)
    #print("Filled in black")


def init():
    print("beginning init")
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    pg.init()
    # use a (r, g, b) tuple for color

    # create the basic window/screen and a title/caption
    # default is a black background, no window border
    screen = pg.display.set_mode((640, 100), pg.NOFRAME)
    print("started screen")
    pg.display.set_caption("Display")

    hWnd = pg.display.get_wm_info()['window']
    win32gui.SetWindowPos(hWnd, -1, x, y, 0, 0, 0x0001)
    print("set window coords")
    """
    update_text("Test1")
    update_text("Test2")
    update_text("Test3")
    """
    """
    queue("Test1")
    #print("Queueing test1")
    queue("Test2")
    queue("Test3")
    """

    #dequeue()
    # event loop
    print("kicking off the infinite loop")
    while True:
        for event in pg.event.get():
            # exit conditions --> windows titlebar x click
            if event.type == pg.QUIT:
                raise SystemExit
        dequeue(screen)
        # print("Repeat")

