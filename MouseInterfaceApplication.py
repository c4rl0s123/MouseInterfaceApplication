import win32api, win32con
from ctypes import windll, Structure, c_long, byref
from datetime import datetime, timedelta
import time
import random

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return (pt)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep((150 + random.randint(4, 96))/1000)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep((120 + random.randint(4, 96))/1000)

def looper():
    start_time = datetime.now()
    try:
        while datetime.now() <= start_time + timedelta(305 + random.randint(2, 43)):
            pt = queryMousePosition()
            click(pt.x, pt.y)
            time.sleep((806 + random.randint(124, 401))/1000)
    except KeyboardInterrupt:
        pass

time.sleep(5)
looper()