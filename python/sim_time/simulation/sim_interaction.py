from collections import defaultdict


class sim_interaction():
    def __init__(self):
        self.dict_interaction = defaultdict(self.subscriber)

    def __get_subscriber__(self, name):
        return self.dict_interaction[name]

    def subscrib(self, name, model):
        self.__get_subscriber__(name).attch(model)

    def publish(self, name, msg):
        # print('publish')
        self.__get_subscriber__(name).send(name, msg)

    class subscriber():
        def __init__(self):
            self._subscribers = set()

        def attch(self, model):
            self._subscribers.add(model)

        def detach(self, model):
            self._subscribers.remove(model)

        def send(self, name, msg):
            # self.print()
            for sub in self._subscribers:
                sub.on_interaction(name, msg)

        def print(self):
            print(self._subscribers)


g_interaction = sim_interaction()


class model_interaction():
    def __init__(self):
        pass

    def _subscrib(self, name):
        g_interaction.subscrib(name, self)

    def subscrip_interaction(self, list_itacn):
        for itacn in list_itacn:
            self._subscrib(itacn)

    def on_interaction(self, name, msg):
        return eval('%s(msg)' % (name))


"""
    @staticmethod
    def raise_interaction(*args):
        for fun in sim_interaction.on_interaction:
            fun(*args)
"""


class A(model_interaction):
    def __init__(self):
        pass

    def on_interaction(self, name, msg):
        def on_open(msg):
            print('A,on_open:', msg)

        return eval('%s(msg)' % (name))


class AA(A):
    def on_interaction(self, name, msg):
        def on_open(msg):
            print('AA,on_open:', msg)

        return eval('%s(msg)' % (name))


class B(model_interaction):
    def __init__(self):
        pass

    def on_interaction(self, name, msg):
        def on_open(msg):
            print('B:on_open')

        def on_close():
            print('on_close')

        return eval('%s(msg)' % (name))


if __name__ == '__main__':

    model_a = A()
    model_a.subscrip_interaction(['on_open', 'on_close'])
    model_aa = AA()
    model_b = B()
    model_b1 = B()
    model_b.subscrip_interaction(['on_open', 'on_close'])
    # model_a.on_interaction('on_open', '2')
    # exc.attch(model_a)
    # exc.attch(model_b)

    g_interaction.publish('on_open', 'msg1')

    pass
