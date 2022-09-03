import tkinter as tk
import time
import calc_eleven as calc
import calc_db as db
from settings import Settings


class ui_eleven_calc(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        settings = Settings()
        self.master = master
        self.master.title('Eleven Math!')
        self.pack()
        self.create_widgets()
        self.work = calc.c_calc(settings.counts, settings.max_result)
#        self.work.print()
        self.db = db.c_db()
        self.btn_callback_reset()
        self.tm_begin = time.time()
        self.b_right = True

    def create_widgets(self):
        """
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack()  #(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

        """
        self.lbl_index = tk.Label(self, text="", font=(
            'Arial', 12), width=40, height=2)
        self.lbl_index.pack()

        self.lbl_question = tk.Label(
            self, text="", bg='green', font=('Arial', 20), width=15, height=3)
        self.lbl_question.pack()

        self.entry_res = tk.Entry(self, font=('arial', 30), bd=3, width=15)
        self.entry_res.place(width=150, height=30)
        self.entry_res.pack()

        self.lbl_tip = tk.Label(
            self, text='Hello, Eleven!', bg='yellow', width=10, height=2)
        self.lbl_tip.pack()

        self.lb_res = tk.Listbox(self, width=40)
        self.lb_res.pack()

        # 在主窗口上添加一个frame控件
        self.frame_btn = tk.Frame()
        self.frame_btn.pack()

        self.btn_ok = tk.Button(
            self.frame_btn, text='Ok,Next', width=15, height=2)
        self.btn_ok["command"] = self.btn_callback_ok
        self.btn_ok.bind_all('<Return>', self.btn_event)
        self.btn_ok.pack(side=tk.LEFT)

        self.btn_reset = tk.Button(
            self.frame_btn, text='Reset', width=15, height=2)
        self.btn_reset["command"] = self.btn_callback_reset
        self.btn_reset.bind_all('<Shift_L>', self.btn_event_reset)
        self.btn_reset.pack(side=tk.RIGHT)

    def __update_lbl_index__(self):
        index = self.index_list+1
        count, fault = self.db.tb_count_today()
        str = "The %2d Question!, Total:%2d, Fault:%2d" % (index, count, fault)
        self.lbl_index.configure(text = str)

    def __update_lbl_question__(self, str_question):
        self.lbl_question.configure(text=str_question)

    def __update_lbl_tip__(self, n_right):
        if n_right == 1:
            self.lbl_tip.configure(text="right", bg="green")
        elif n_right == 0:
            self.lbl_tip.configure(text="wrong", bg="red")
        elif n_right == 2:
            self.lbl_tip.configure(text="Well Done", bg="yellow")

    def __update_lb_res__(self, str_res):
        tm_end = time.time()
        f_usage_time = tm_end - self.tm_begin

        self.lb_res.insert(tk.END, "%s,  %.02f" % (str_res, f_usage_time))
        if not self.b_right:
            self.lb_res.itemconfig(self.lb_res.size()-1, foreground='red')
        self.tm_begin = tm_end

        self.__insert_db__(f_usage_time)

    def __insert_db__(self, usage_time):
        # quesion, answer, result, usage_time
        str_question = self.lbl_question.cget("text")
        str_answer = self.entry_res.get()
        self.db.tb_insert(str_question, str_answer, self.b_right, usage_time)

    def btn_callback_ok(self):
        if self.__check_res__():    # right
            self.__update_lbl_tip__(1)
            self.__next_work__()
        else:                       # wrong
            self.entry_res.focus()
            self.entry_res.delete(0, 'end')
            self.__update_lbl_tip__(0)

        self.__update_lb_res__(self.str_res)

    def btn_event(self, event):
        if self.b_exit == True:
            self.master.destroy
        else:
            self.btn_callback_ok()

    def btn_callback_reset(self):
        self.work.create()
        self.index_list = -1
        self.__next_work__()
        self.lb_res.delete(0, tk.END)
        print('reset')

    def btn_event_reset(self, event):
        self.btn_callback_reset()
        # print('event')

    def __get_new_work__(self, index):
        list_nums = self.work.get_one_calc(index)
        if list_nums != None:
            str_question = list_nums[0]
            xRes = list_nums[1]
            return str_question
        else:
            return ""

    def __check_res__(self):
        n_res = int(self.entry_res.get())
        self.b_right = self.work.check_calc(self.index_list, n_res)
        # record the result for print the listbox
        self.str_res = str(self.index_list+1) + " : " + \
            self.lbl_question.cget("text") + self.entry_res.get()
        return self.b_right

    def __next_work__(self):
        # print(self.index_list)
        self.index_list += 1
        str_question = self.__get_new_work__(self.index_list)
        # print(str_question)
        if len(str_question) != 0:
            self.__update_lbl_index__()
            self.__update_lbl_question__(str_question)
            self.entry_res.delete(0, 'end')
            self.entry_res.focus()
            self.b_exit = False
        else:   # Game over!
            self.__update_lbl_tip__(2)
            self.btn_ok.configure(text='Exit', command=self.master.destroy)
            self.b_exit = True


root = tk.Tk()
app = ui_eleven_calc(master=root)
app.mainloop()
