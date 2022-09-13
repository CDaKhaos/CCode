import sys
sys.path.append('../')

from simulation import *
from mod_consumer import em_csm_type
import scenario
import settings

class model_market(model_base):
    def __init__(self):
        super().__init__()
        self.cls_scro = scenario.scenario()
        self.cls_set = settings.settings()
        self.list_consumer = list()
        self.list_consumer_vip = list()
        self.list_producer = self.cls_scro.create_producer()
        self._producer_work = 0

    def __del__(self):
        pass

    def sim(self, step):
        # print("market, mid=%d" % self.mid)
        # create consumer
        if step < self.cls_set.create_consumer_time :
            list_consumer = self.cls_scro.create_consumer()
            for csm in list_consumer:
                self.add_consumer(csm)

        # rule
        consumer_cnt = self.last_consumer()
        num = int(consumer_cnt / self.cls_set.create_consumer_num)
        num = max(1, num)
        self.set_producer_work(num)
        # print('csm cnt:%d, pdc cnt:%d' % (consumer_cnt, num))
        
        # assing consumer
        for pro in self.list_producer:
            if pro.is_work() == False and pro.get_sim_run() == True:
                self.assign_consumer(pro)

    def add_consumer(self, consumer):
        if consumer.is_VIP():
            self.list_consumer_vip.append(consumer)
        else:
            self.list_consumer.append(consumer)

    def last_consumer(self):
        return len(self.list_consumer) + len(self.list_consumer_vip)

    def assign_consumer(self, pro):
        #first VIP
        if len(self.list_consumer_vip) > 0 :
            pro.add_work(self.list_consumer_vip.pop(0))
        elif len(self.list_consumer) > 0 :
            pro.add_work(self.list_consumer.pop(0))

    def add_producer(self, producer):
        self.list_producer.append(producer)

    def set_producer_work(self, num):
        # print('producer work:', num)
        cnt = min(num, self.cls_set.porducer_work)
        if cnt == self._producer_work:
            return

        for pro in self.list_producer:
            pro.set_sim_run(pro.is_work())

        for pro in self.list_producer:
            if (cnt > 0):
                pro.set_sim_run(True)
                cnt -= 1
            else:
                break
        cnt = 0
        for pro in self.list_producer:
            if (pro.get_sim_run()):
                cnt += 1

        self._producer_work = cnt  


    def finish(self):
        b_ret = True
        for pro in self.list_producer:
            b_ret &= pro.is_work()

        return len(self.list_consumer) == 0 and not b_ret
    
    def print(self):
        print('consumer count:', len(self.list_consumer))

