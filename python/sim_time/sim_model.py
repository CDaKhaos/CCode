class model_base(object):
    register_cls = list()
    model_id = 0

    def __new__(cls, *args, **kwargs):
        new_cls = super(model_base, cls).__new__(cls)
        if cls.__name__ not in ["model_base", "sim_model"]:
            # print(cls.__name__)
            model_base.register_cls.append(new_cls)
        return new_cls

    @staticmethod
    def get_model_id():
        mid = model_base.model_id
        model_base.model_id += 1
        return mid

    def __init__(self):
        self.mid = self.get_model_id()
        pass

    def sim(self):
        raise NotImplementedError


class model_a(model_base):
    def __init__(self):
        super().__init__()

    def sim(self):
        print("a,mid=%d" % self.mid)


class model_aa(model_a):
    def __init__(self):
        super().__init__()

    def sim(self):
        print("aa,mid=%d" % self.mid)


class model_b(model_base):
    def __init__(self):
        super().__init__()
        pass

    def sim(self):
        print("b,mid=%d" % self.mid)


class sim_model(model_base):
    def __init__(self):
        pass

    def sim(self):
        print("sim")

    def do_sim(self):
        # print(model_base.register_cls)
        for m in model_base.register_cls:
            m.sim()


if __name__ == '__main__':
    sim = sim_model()

    a = model_a()
    aa = model_aa()
    b = model_b()
    a1 = model_a()

    sim.print()
