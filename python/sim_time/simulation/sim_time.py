# 继承式调用
import threading
import time
if __package__ is None or __package__ == '':
    from sim_define import em_pro_ctrl
else:
    from .sim_define import em_pro_ctrl


class sim_event:
    on_event = []

    @staticmethod
    def raise_event(*args):
        for fun in sim_event.on_event:
            fun(*args)


class time_thread(threading.Thread):
    def __init__(self):
        super(time_thread, self).__init__()
        self.__exit_flag = False
        self.__run_flag = em_pro_ctrl.STOP
        self.start_time = time.time()
        self.now_time = 0
        self.fast = 1.0

    # 线程要运行的代码
    def run(self):
        step_time = 0
        count = 0
        while self.__exit_flag == False:
            # START
            if self.__run_flag == em_pro_ctrl.START:
                self.now_time = time.time()
                if (self.now_time - step_time) > 1.0 / self.fast:
                    step_time = self.now_time
                    count += 1
                    #print("working:%d!" % count)
                    # Event
                    sim_event.raise_event(count)

            else:
                # STOP
                if self.__run_flag == em_pro_ctrl.STOP:
                    self.start_time = step_time = time.time()
                    count = 0
            # PAUSE and default sleep
            time.sleep(0.01)

    def set_exit(self, flag=True):
        self.__exit_flag = flag

    def set_pro_ctrl(self, pro_ctrl=em_pro_ctrl.START):
        self.__run_flag = pro_ctrl


if __name__ == '__main__':
    t1 = time_thread()
    t1.start()
    print("0")

    time.sleep(2)
    t1.set_pro_ctrl(em_pro_ctrl.START)
    t1.fast = 2.0
    print("1")

    time.sleep(5)
    t1.set_pro_ctrl(em_pro_ctrl.PAUSE)
    print("2")

    time.sleep(2)
    t1.set_pro_ctrl(em_pro_ctrl.START)
    t1.fast = 5.0
    print("3")

    time.sleep(5)
    t1.set_exit()
    print("4")

    t1.join()
    print("Game Over")
