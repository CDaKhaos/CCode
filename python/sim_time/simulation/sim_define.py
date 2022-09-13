from enum import Enum
import random

class em_pro_ctrl(Enum):
    START = 1
    PAUSE = 2
    STOP = 3

    @staticmethod
    def random():
        return random.choices(list(em_pro_ctrl))[0]
    

if __name__ == "__main__":
    # print(em_pro_ctrl.STOP.value)
    print(em_pro_ctrl.random())

