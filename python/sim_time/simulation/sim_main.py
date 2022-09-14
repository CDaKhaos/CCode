if __package__ is None or __package__ == '':
    from sim_time import time_thread, sim_event
    from sim_model import model_man, model_a, model_b
    from sim_define import em_pro_ctrl
else:
    from .sim_time import time_thread, sim_event
    from .sim_model import model_man, model_a, model_b
    from .sim_define import em_pro_ctrl

import time


class sim_main():
    def __init__(self):
        self.sim = model_man()
        self.sim_event = sim_event()
        self.sim_event.on_event.append(self.do_sim_event)
        self.sim_time = time_thread()
        self.sim_time.start()
        self.__step = 0
        pass

    def __del__(self):
        self.sim_time.join()
        print('simulation is over')

    def do_sim_event(self, count):
        # print("sim event: ", count)
        self.__step = count
        self.sim.do_sim(count)

    def set_pro_ctrl(self, em_pro_ctrl):
        print('ctrl:', em_pro_ctrl)
        self.sim_time.set_pro_ctrl(em_pro_ctrl)

    def set_speed(self, speed):
        # print('speed:', speed)
        self.sim_time.fast = speed

    def set_exit(self):
        print('exit')
        self.sim_time.set_exit()

    def get_step(self):
        return self.__step


if __name__ == '__main__':
    main = sim_main()

    a = model_a()
    b = model_b()

    time.sleep(2)
    main.set_pro_ctrl(em_pro_ctrl.START)
    main.set_speed(2.0)

    time.sleep(2)
    main.set_pro_ctrl(em_pro_ctrl.PAUSE)

    time.sleep(2)
    main.set_pro_ctrl(em_pro_ctrl.STOP)

    time.sleep(2)
    main.set_pro_ctrl(em_pro_ctrl.START)

    time.sleep(2)
    main.set_speed(3.0)

    time.sleep(2)
    main.set_pro_ctrl(em_pro_ctrl.STOP)

    time.sleep(2)
    main.set_exit()
