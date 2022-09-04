class meta_cls(type):
    regist_cls = list()

    def __new__(cls, name, bases, attrs):
        new_cls = super(meta_cls, cls).__new__(cls, name, bases, attrs)
        if name not in ["base", "sim_model"]:
            print("type of {} is {} name is {}".format(name, type(new_cls), new_cls.__name__))
            print(new_cls)
            meta_cls.regist_cls.append(new_cls)
        return new_cls


class base(object, metaclass=meta_cls):
    def __init__(self):
        pass

    def sim(self):
        raise NotImplementedError


class model_a(base):
    def __init__(self):
        print("a __init__")

    def sim(self):
        print("a")


class model_aa(model_a):
    def __init__(self):
        print("aa __init__")

    def sim(self):
        print("aa")


class model_b(base):
    def __init__(self):
        print("b __init__")

    def sim(self):
        print("b")


class sim_model(base):
    def __init__(self):
        pass

    def print(self):
        print(meta_cls.regist_cls)
        for m in meta_cls.regist_cls:
            m.sim(self)


if __name__ == '__main__':
    print('begin')
    sim = sim_model()

    a = model_a()
    aa = model_aa()
    b = model_b()
    a1 = model_a()

    sim.print()
