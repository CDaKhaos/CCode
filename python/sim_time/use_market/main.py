import sys
sys.path.append('../')
import time

from simulation import *
import settings
from mod_consumer import model_consumer, em_csm_type
from mod_producer import model_producer
from mod_market import model_market

if __name__ == '__main__':
    cls_set = settings.settings()

    main = sim_main()
    market = model_market()

    time.sleep(2)
    main.set_pro_ctrl(em_pro_ctrl.START)
    main.set_speed(cls_set.speed)

    t_begin = time.time()
    while True:
        time.sleep(1 / cls_set.speed * 10)
        # market.print
        if market.finish():
            t_end = time.time()
            main.set_exit()
            break
    print('spend time:', t_end - t_begin)
