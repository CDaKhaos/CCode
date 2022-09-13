from sys import path
path.append('../')
import random
from simulation import *
from enum import Enum


class em_csm_type(Enum):
    A = 2
    B = 4
    VIP = 6

    @staticmethod
    def randomA():
        return random.choices(list(em_csm_type))[0]

    @staticmethod
    def random():
        x = random.randint(0, 100)
        if (x > 99):
            return em_csm_type.VIP
        elif (x > 70):
            return em_csm_type.B
        else:
            return em_csm_type.A


class model_consumer(model_base):
    def __init__(self, em_scm_type):
        super().__init__()
        self.type = em_scm_type
        self.use_time = em_scm_type.value
        self.lift_time = em_scm_type.value
        self.doing = False
        # subscrip
        super().subscrip_interaction(['on_start', 'on_work'])

    def __del__(self):
        # print('del:', self.mid)
        pass

    def sim(self, step):
        # print("consumer, mid=%d" % self.mid)
        if self.doing:
            # print("consumer, mid=%d" % self.mid
            # if (self.get_mid() > 10):
                # print('csm id: %d, lift time:%d' % (self.get_mid(), self.lift_time))

            self.lift_time -= 1

            if self.finish():
                self.doing = False
                self.set_sim_run(False);
                g_interaction.publish('on_finish', self)

    def on_interaction(self, name, msg):
        def on_start(msg):
            if msg == self:
                self.doing = True
        
        def on_work(msg):
            # if msg == self:
                # self.lift_time -= 1
            pass

        return eval('%s(msg)' % (name))

    def finish(self):
        return self.lift_time == 0

    def is_VIP(self):
        return self.type == em_csm_type.VIP

    def print(self):
        print('consumer:', self.mid, self.type)


if __name__ == '__main__':
    print(em_csm_type.randomA())
