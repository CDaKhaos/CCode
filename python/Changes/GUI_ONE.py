# -*- coding: GBK -*-

import tkinter as tk
from ui_frame import ui_frame
from data import YAO, EightDiagrams, ChangesDiagrams
import data_GUA

class ui_one(ui_frame):
    def __init__(self, master, ChangesGUA):
        super().__init__(master)
        self.master = master
        self.GUA = ChangesGUA

        self.master.attributes("-topmost", True)
        self.master.title(ChangesGUA.value[2])

        # abstractmethod
        self._YANG_YAO = 'red'
        self._HEI = 20
        self._FONT = ('仿宋', self._HEI-3)
        self._resize()
        
        self.w = 900
        self.h = 400
        self.center_window(self.w, self.h)
        self.cv = tk.Canvas(self.master, bg = 'white', width=self.w, height=self.h)
        self._draw()
        self.cv.pack()

    def _draw(self):
        x = self._X_START
        y = self._Y_START + self._HEI

        # 卦辞
        self.cv.create_text(self.w / 2, y, 
            text = (data_GUA.Changes_Txt[self.GUA][0]),
            font = self._FONT,
            fill='black'
            )

        Y_S = y + self._HEI + self._HEI
        y = Y_S
        y = self._draw_EightDiagrams(self.GUA.value[0], x, y, data_GUA.Changes_Txt[self.GUA][1:4])
        y = self._draw_EightDiagrams(self.GUA.value[1], x, y, data_GUA.Changes_Txt[self.GUA][4:7])

        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = ui_one(master=root, ChangesGUA=ChangesDiagrams.ZHUN)
    app.mainloop()