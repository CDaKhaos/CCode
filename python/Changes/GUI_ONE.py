# -*- coding: GBK -*-

import tkinter as tk
from ui_frame import ui_frame
from data import YAO, EightDiagrams, ChangesDiagrams

class ui_one(ui_frame):
    def __init__(self, master, ChangesOne):
        super().__init__(master)
        self.master = master
        self.One = ChangesOne

        self.master.attributes("-topmost", True)
        self.master.title(ChangesOne.value[2])

        # abstractmethod
        self._YANG_YAO = 'red'
        self._HEI = 25
        self._resize()
        
        w = 700
        h = 400
        self.center_window(w, h)
        self.cv = tk.Canvas(self.master, bg = 'white', width=w, height=h)
        self._draw()
        self.cv.pack()

    def center_window(self, width, height):
        #获取屏幕尺寸
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()

        #计算窗口居中显示的参数
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        #设置窗口居中显示
        self.master.geometry(size)

    def _draw(self):
        x = self._X_START
        y = self._Y_START
        y = self._draw_EightDiagrams(self.One.value[0], x, y)
        y = self._draw_EightDiagrams(self.One.value[1], x, y)
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = ui_one(master=root, ChangesOne=ChangesDiagrams.QIAN)
    app.mainloop()