from mod_consumer import em_csm_type
from sys import path
path.append('../')
from simulation import *


class model_producer(model_base):
    def __init__(self):
        super().__init__()
        self.list_done_consumer = list()
        self.list_wait_consumer = list()
        self.cur_consumer = None
        self.work_time = 0
        # subscrip
        super().subscrip_interaction(['on_finish'])

    def __del__(self):
        self.print()

    def sim(self, step):
        self.work_time += 1
        # if (self.get_mid() == 2):
            # print('work_time:', self.work_time)
        if self.cur_consumer == None:
            if len(self.list_wait_consumer) == 0:
                print('pro:%d wait' % self.get_mid())
            else:
                self.cur_consumer = self.list_wait_consumer.pop(0)
                g_interaction.publish('on_start', self.cur_consumer)
        else:
            # working
            # g_interaction.publish('on_work', self.cur_consumer)
            # if (self.get_mid() == 2):
                # print("consum:%d, type:%s is doing" %
                    # (self.cur_consumer.get_mid(), self.cur_consumer.type))
            pass

    def on_interaction(self, name, msg):
        def on_finish(msg):
            if msg == self.cur_consumer:
                # if (self.get_mid() == 2):
                    # print("consum:%d, type:%s is finish" %
                        # (self.cur_consumer.get_mid(), self.cur_consumer.type))
                self.list_done_consumer.append(self.cur_consumer)
                self.cur_consumer = None

        return eval('%s(msg)' % (name))

    def add_work(self, consumer):
        self.list_wait_consumer.append(consumer)

    def is_work(self):
        # if (self.get_mid() == 2 and self.get_sim_run() == True):
            # print(self.cur_consumer != None)
        return self.cur_consumer != None

    def print(self):
        print('Pro:%d Done:%d using:%d' %
              (self.get_mid(), len(self.list_done_consumer), self.work_time))
        cnt_A = cnt_B = cnt_vip = 0
        strA = strB = strVIP = ''
        for done in self.list_done_consumer:
            match (done.type):
                case em_csm_type.A:
                    cnt_A += 1
                    strA += ' %d'%done.get_mid()
                case em_csm_type.B:
                    cnt_B += 1
                    strB += ' %d'%done.get_mid()
                case em_csm_type.VIP:
                    cnt_vip += 1
                    strVIP += ' %d'%done.get_mid()
        work_time = cnt_A*em_csm_type.A.value + cnt_B * \
            em_csm_type.B.value + cnt_vip*em_csm_type.VIP.value
        print('    A:%d, B:%d, VIP:%d, count:%d' %
              (cnt_A, cnt_B, cnt_vip, work_time))
        print('    A:', strA)
        print('    B:', strB)
        print('    V:', strVIP)
