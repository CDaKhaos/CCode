import time
import threading

test = 18

class MyEvent:
    onVarChanged = []
    @staticmethod
    def raiseEvent(*args):
        for fun in MyEvent.onVarChanged:
            fun(*args)

def reportVarChange():
    currentVar = test
    while True:
        time.sleep(0.01)
        if test != currentVar:
            # test变量发生了改变，激发事假
            MyEvent.raiseEvent(test)
            currentVar = test

def ChangeProcessor(newVar):
    print("changed to:", newVar)

if __name__ == '__main__':
    # 订阅事件，并指定处理函数
    MyEvent.onVarChanged.append(ChangeProcessor)
    t = threading.Thread(target=reportVarChange)
    t.start()
    time.sleep(1)
    test = 20
    time.sleep(1)
    test = 80
    time.sleep(1)
