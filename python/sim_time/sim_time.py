# 继承式调用
import threading
import time

class time_thread(threading.Thread):
    def __init__(self, name):
        super(MyThreading, self).__init__()
        self.name = name

    # 线程要运行的代码
    def run(self):
        print("我是线程%s" % self.name)
        time.sleep(2)

start_time = time.time()
t1 = MyThreading(1)
t2 = MyThreading(2)
end_time = time.time()
print("两个线程一共的运行时间为：", end_time-start_time)
print("主线程结束")

"""
运行结果：
我是线程1
我是线程2
两个线程一共的运行时间为： 0.0010724067687988281
主线程结束
线程2运行结束
线程1运行结束
"""
