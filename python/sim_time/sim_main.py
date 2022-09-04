from sim_time import time_thread, sim_event
from sim_model import sim_model, model_a, model_b
import time
from sim_define import em_pro_ctrl

sim = sim_model()


def do_sim_event(count):
    print("sim event: ", count)
    sim.do_sim()


def sim_main():

    a = model_a()
    b = model_b()

    sim.do_sim()

    sim_event.on_event.append(do_sim_event)
    sim_time = time_thread()
    sim_time.start()

    time.sleep(2)
    sim_time.set_pro_ctrl(em_pro_ctrl.START)
    sim_time.fast = 2.0

    sim_time.join()
    print('Over')


if __name__ == '__main__':
    sim_main()
