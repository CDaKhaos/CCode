import threading
import time, os

class sim_time_thrd(threading.Thread)
    def __init__(self):
        super(sim_time_thrd, self).__init__()

    def run(self):
        print('123')

    def play(self):
        print('play')

    def stop(self):
        print('stop')

    def speed(n)
        print('speed: %d' % (n))

