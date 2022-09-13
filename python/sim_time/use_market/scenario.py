import settings
import random
import time
import sys
sys.path.append('../')
from mod_producer import model_producer
from mod_consumer import model_consumer, em_csm_type
from simulation import *


class scenario():
    def __init__(self):
        self.cls_set = settings.settings()
        self.__create_count = 0
        pass

    def __del__(self):
        print('create consumer:', self.__create_count)

    def create_consumer(self):
        list_consumer = list()
        num = self.cls_set.create_consumer_num  
        cnt = random.randint(-num, num)
        while cnt > 0:
            type_csm = em_csm_type.random()
            # print(type_csm)
            new = model_consumer(type_csm)
            list_consumer.append(new)
            cnt -= 1
            self.__create_count += 1 
        # print('create:', len(list_consumer))
        # self.__create_count += len(list_consumer)
        return list_consumer

    def create_producer(self):
        list_producer = list()
        cnt = self.cls_set.porducer_work 
        while cnt > 0:
            new = model_producer()
            new.set_sim_run(False)
            list_producer.append(new)
            cnt -= 1
        return list_producer


