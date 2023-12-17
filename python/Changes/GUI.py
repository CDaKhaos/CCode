# -*- coding: GBK -*-

import tkinter as tk
from ui_frame import ui_frame
from data import YAO, EightDiagrams, ChangesDiagrams
from GUI_ONE import ui_one

class ui_Changes(ui_frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Changes!')

        self.lst_ChangesD = list(ChangesDiagrams)

        # abstractmethod
        self._YANG_YAO = 'black'
        self._HEI = 5
        self._resize()

        self.w = (self._X_START * 2) + (self._LEN * 15)
        self.h = (self._Y_START * 2) + (self._Y_GAP * 15) + self._WIN_TITLE_HEI 
        self.center_window(self.w, self.h)
        self.cv = tk.Canvas(self.master, bg = 'white', width=self.w, height=self.h)
        self._draw()
        self.cv.pack()

        # 绑定鼠标单击事件处理程序
        self.cv.bind('<Button-1>', self.click)


    def _draw(self):
        set_col = 8
        row = len(ChangesDiagrams) / set_col

        for i, value in enumerate(self.lst_ChangesD, 0):
            x = self._X_START + (self._LEN * 2) * (i % set_col)
            y = self._Y_START + (self._Y_GAP * 2) * int(i / set_col)

            self.__draw_ChangesDiagrams(value, i, x, y)
        
        #y = (self.h - HEI) / 8
        #x = self.w / 8
        #for i in range(1, 8):
        #    self.cv.create_line(0, y*i, self.w, y*i, fill = 'black')
        #    self.cv.create_line(x*i, 0, x*i, self.h, fill = 'black')
            
    def __draw_ChangesDiagrams(self, changesD, index, x, y):
        y = self._draw_EightDiagrams(changesD.value[0], x, y)
        y = self._draw_EightDiagrams(changesD.value[1], x, y)

        self.cv.create_text(x+(self._LEN/2), y+self._HEI+self._HEI, 
            text = ("%d.%s" % (index+1, changesD.value[2])),
            font = self._FONT,
            fill='black',
            anchor = tk.CENTER,
            justify = tk.CENTER)
        return y

    
    # 添加鼠标单击事件处理程序
    def click(self, event):
        # 在散点图中添加新点
        x, y = event.x, event.y
        
        yy = (self.h - self._HEI) / 8
        xx = self.w / 8

        row = x / xx
        col = y / yy

        index = int(row) + int(col)*8

        print(self.lst_ChangesD[index])
        
        self.ui_one = tk.Toplevel(self.master)
        one = ui_one(self.ui_one, self.lst_ChangesD[index])


if __name__ == '__main__':
    root = tk.Tk()
    app = ui_Changes(master=root)
    app.mainloop()