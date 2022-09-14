if __package__ is None or __package__ == '':
    from sim_interaction import model_interaction
else:
    from .sim_interaction import model_interaction


class model_base(model_interaction, object):
    register_cls = list()
    model_id = 0

    def __new__(cls, *args, **kwargs):
        new_cls = super(model_base, cls).__new__(cls)
        if cls.__name__ not in ["model_base", "model_man"]:
            # print(cls.__name__)
            model_base.register_cls.append(new_cls)
        return new_cls

    @staticmethod
    def get_model_id():
        mid = model_base.model_id
        model_base.model_id += 1
        return mid

    def __init__(self):
        self.__mid = self.get_model_id()
        self.__b_sim_run = True
        pass
    
    def get_mid(self):
        return self.__mid

    def set_sim_run(self, b = False):
        self.__b_sim_run = b

    def get_sim_run(self):
        return self.__b_sim_run 

    def sim(self, step):
        raise NotImplementedError


class model_man():
    def __init__(self):
        pass

    def sim(self):
        print("sim")

    def do_sim(self, step):
        # print(model_base.register_cls)
        # cnt = 0
        # print('register_cls num:', len(model_base.register_cls))
        for m in model_base.register_cls:
            if m.get_sim_run():
                # cnt += 1
                m.sim(step)
        # print('     running cls:', cnt)


# test
class model_a(model_base):
    def __init__(self):
        super().__init__()

    def sim(self, step):
        print("a,mid=%d" % self.get_mid())


class model_aa(model_a):
    def __init__(self):
        super().__init__()

    def sim(self, step):
        print("aa,mid=%d" % self.mid)


class model_b(model_base):
    def __init__(self):
        super().__init__()
        pass

    def sim(self, step):
        print("b,mid=%d" % self.get_mid())


if __name__ == '__main__':
    sim = model_man()

    a = model_a()
    aa = model_aa()
    b = model_b()
    a1 = model_a()

    sim.do_sim()
