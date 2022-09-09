import time
import sys
sys.path.append(".//simulation")

from sim_interaction import g_interaction
from sim_model import model_base
from sim_main import sim_main
from sim_define import em_pro_ctrl
from enum import Enum

class em_csm_type(Enum):
    A = 2
    B = 4
    VIP = 6


class model_consumer(model_base):
    def __init__(self, em_scm_type):
        super().__init__()
        self.type = em_scm_type
        self.use_time = em_scm_type.value
        self.lift_time = em_scm_type.value
        self.doing = False

    def sim(self):
        # print("consumer, mid=%d" % self.mid)
        if self.doing:
            #print("consumer, mid=%d" % self.mid)
            self.lift_time -= 1

        if self.finish():
            g_interaction.publish('on_finish', self)

    def in_market(self):
        self.doing = True

    def finish(self):
        return self.lift_time == 0

    def is_VIP(self):
        return self.type == em_csm_type.VIP


class model_producer(model_base):
    def __init__(self):
        super().__init__()

    def sim(self):
        pass
        #print("producer,mid=%d" % self.mid)


class model_market(model_base):
    def __init__(self):
        super().__init__()
        self.list_consumer = []
        self.cur_csm = None
        # subscrip
        super().subscrip_interaction(['on_finish'])

    def sim(self):
        #print("market, mid=%d" % self.mid)
        if self.cur_csm == None and len(self.list_consumer) > 0:
            self.cur_csm = self.list_consumer.pop(0)
            self.cur_csm.in_market()

    def on_interaction(self, name, msg):
        def on_finish(msg):
            # print(msg == self.cur_csm) True
            print("consum:%d, type:%s is finish" %
                  (self.cur_csm.mid, self.cur_csm.type))
            self.cur_csm = None

        return eval('%s(msg)' % (name))

    def add_consumer(self, consumer):
        if consumer.is_VIP():
            self.list_consumer.insert(0, consumer)
        else:
            self.list_consumer.append(consumer)

    def finish(self):
        return len(self.list_consumer) == 0 and self.cur_csm == None


if __name__ == '__main__':
    main = sim_main()

    market = model_market()

    c1 = model_consumer(em_csm_type.A)
    c2 = model_consumer(em_csm_type.B)
    c3 = model_consumer(em_csm_type.VIP)

    p1 = model_producer()

    market.add_consumer(c1)
    market.add_consumer(c2)
    market.add_consumer(c3)

    time.sleep(2)
    main.set_pro_ctrl(em_pro_ctrl.START)
    main.set_speed(1.0)

    while True:
        time.sleep(2)
        if market.finish():
            main.set_exit()
            break
