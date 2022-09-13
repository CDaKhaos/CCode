from enum import Enum
from simulation import *
import time


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
        # subscrip
        super().subscrip_interaction(['on_start'])

    def sim(self, step):
        # print("consumer, mid=%d" % self.mid)
        if self.doing:
            # print("consumer, mid=%d" % self.mid

            self.lift_time -= 1

            if self.finish():
                self.doing = False
                g_interaction.publish('on_finish', self)

    def on_interaction(self, name, msg):
        def on_start(msg):
            if msg == self:
                self.doing = True

        return eval('%s(msg)' % (name))

    def finish(self):
        return self.lift_time == 0

    def is_VIP(self):
        return self.type == em_csm_type.VIP


class model_producer(model_base):
    def __init__(self):
        super().__init__()
        self.list_done_consumer = list()
        self.list_wait_consumer = list()
        self.cur_consumer = None
        # subscrip
        super().subscrip_interaction(['on_finish'])

    def sim(self, step):
        if self.cur_consumer == None:
            if len(self.list_wait_consumer) == 0:
                print('mid:%d wait' % self.get_mid())
            else:
                self.cur_consumer = self.list_wait_consumer.pop(0)
                g_interaction.publish('on_start', self.cur_consumer)

        else:
            # working
            pass

    def on_interaction(self, name, msg):
        def on_finish(msg):
            if msg == self.cur_consumer:
                print("consum:%d, type:%s is finish" %
                      (self.cur_consumer.get_mid(), self.cur_consumer.type))
                self.list_done_consumer.append(self.cur_consumer)
                self.cur_consumer = None

        return eval('%s(msg)' % (name))

    def add_work(self, consumer):
        self.list_wait_consumer.append(consumer)

    def is_work(self):
        return self.cur_consumer != None


class model_market(model_base):
    def __init__(self):
        super().__init__()
        self.list_consumer = list()
        self.list_producer = list()

    def sim(self, step):
        #print("market, mid=%d" % self.mid)
        for pro in self.list_producer:
            if len(self.list_consumer) > 0 and pro.is_work() == False:
                pro.add_work(self.list_consumer.pop(0))

    def add_consumer(self, consumer):
        if consumer.is_VIP():
            self.list_consumer.insert(0, consumer)
        else:
            self.list_consumer.append(consumer)

    def add_producer(self, producer):
        self.list_producer.append(producer)

    def finish(self):
        b_ret = True
        for pro in self.list_producer:
            b_ret &= pro.is_work()

        return len(self.list_consumer) == 0 and not b_ret


if __name__ == '__main__':
    main = sim_main()

    market = model_market()

    p1 = model_producer()
    p2 = model_producer()
    # p3 = model_producer()
    market.add_producer(p1)
    market.add_producer(p2)
    # market.add_producer(p3)

    c1 = model_consumer(em_csm_type.A)
    c2 = model_consumer(em_csm_type.B)
    c3 = model_consumer(em_csm_type.VIP)
    market.add_consumer(c1)
    market.add_consumer(c2)
    market.add_consumer(c3)

    time.sleep(1)
    main.set_pro_ctrl(em_pro_ctrl.START)
    main.set_speed(1.0)

    while True:
        time.sleep(2)
        if market.finish():
            main.set_exit()
            break
