import sys
import warnings
from PyQt5.QtWidgets import * #automatethem.com
import win32gui
import win32con
import threading
warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from pywinauto import backend
from pywinauto import Desktop, Application
import time

def __show_property(self, index=None):
    data = index.data()
    self.table_model \
        = MyTableModel(self.tree_model.props_dict.get(data), self)
    self.table_view.wordWrap()
    self.table_view.setModel(self.table_model)
    self.table_view.setColumnWidth(1, 320)

    handle = None 
    process_id = None 
    for name, value in self.tree_model.props_dict.get(data):
        if name == "handle":
            try:
                handle = int(value)
            except:
                pass
        elif name == "process_id":
            try:
                process_id = int(value)
            except:
                pass

    if handle and process_id:
        app = Application(backend='uia').connect(process=int(process_id)) #프로세스 pid로 연결하는 방법
        #app = Application(backend='uia').connect(title_re="Notepad\+\+") #정규식으로 프로그램 title을 검색해서 연결하는 방법
        window = app.window(handle=handle)
        #window.wrapper_object().set_focus()
        t = threading.Thread(target=self.blink, args=[handle])
        t.start()
            
def blink(self, handle):
        #https://groups.google.com/g/python_inside_maya/c/qZOWB6_8E3g
        for i in range(2):
            #change_background_color(hwnd, color1)
            win32gui.ShowWindow(handle, win32con.SW_HIDE)
            time.sleep(0.5)
            #change_background_color(hwnd, color2)
            #time.sleep(duration)
            win32gui.ShowWindow(handle, win32con.SW_SHOW)
            if i != 2 -1:
                time.sleep(0.5)
