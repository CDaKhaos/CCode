# -*- coding: GBK -*-

import tkinter as tk
from data import YAO, EightDiagrams
from abc import ABCMeta, abstractmethod


class ui_frame(tk.Frame):
    __metaclass__ = ABCMeta

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self._HEI = 5
        self._X_START = 20
        self._Y_START = 10
        self._WIN_TITLE_HEI = 30
        self._resize()
        self._YANG_YAO = 'balck'
    
    def _resize(self):
        self._LEN = self._HEI * 11
        self._YIN_GAP = self._LEN * 0.372 / 4   #����Ϊ�˺ÿ������˻ƽ�ָ����0.618
        self._Y_GAP = self._LEN - self._HEI - self._HEI
        self._FONT = ('����', self._HEI*2)

    def center_window(self, width, height):
        #��ȡ��Ļ�ߴ�
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()

        #���㴰�ھ�����ʾ�Ĳ���
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2 - self._WIN_TITLE_HEI)

        #���ô��ھ�����ʾ
        self.master.geometry(size)

    def _draw_EightDiagrams(self, eightD, x, y):
        for value in eightD.value:
            y = self._draw_yao(value, x, y)
        return y

    def _draw_yao(self, yao, x, y):
        ye = y + self._HEI
        if yao == YAO.YANG.value:
            self.cv.create_rectangle(x, y, x+self._LEN, ye, fill=self._YANG_YAO)
        else:
            mid = x + self._LEN / 2
            self.cv.create_rectangle(x, y, mid - self._YIN_GAP, ye, fill = 'black')
            self.cv.create_rectangle(mid + self._YIN_GAP, y, x+self._LEN, ye, fill = 'black')
        return ye+self._HEI

    @abstractmethod
    def _draw(self):
        pass