import random
from data import EightDiagrams, ChangesDiagrams

class divination():
    def __init__(self):
        pass

    def __div(self, num):
        n = num % 4
        if n == 0:
            n = 4
        return n

    def __Change(self, num):
        # 1.��49����ֳ����ݣ��졢�أ�
        rand = num
        rand_temp = int(rand / 1.3141592)
        left = random.randint(rand - rand_temp, rand + rand_temp)
        right = num - left

        # 2.������һ������һ�����ˣ�
        right -= 1

        # 3.�� ���� 4 ���õ��������������������Ϊ4�������м�ȥ����
        l = self.__div(left)

        # 4.�� ���յ�������
        r = self.__div(right)

        # 5.2�� 1�� + 3 ������ + 4������  ������9������5��
        res = 1 + l + r
        num -= res
        return res

    # ���� 
    # 1.����ʣ���������ϣ��ظ�һ��Ĺ��̣�5�����󣬲���4������8

    # ���䣬�ظ��ڶ���

    # �������ֻ꣬����24,28,32,96
    # ����������� 4 �õ�س��Ϊ��������������
    def __YAO(self):
        n = 49
        c = 0
        list_c = []
        for i in range(0, 3):
            c = self.__Change(n)
            n -= c
        return int(n / 4)

    # �ظ�6�Σ��õ�һ���ң� 7��9Ϊ����6��8Ϊ����6��������9������
    # �ϱ��ٲ���
    def GUA(self):
        list_y = []
        for i in range(0, 6):
            list_y.append(self.__YAO())

        """ 
        ��س-����
        1.6��س��û�б�س��6س��ɵı����Դ�
        2.һ��س�����˱仯�����س��س��
        3.��2��س���Ǳ�س��ʱ����ô��Ҫ����2��س��س�ǣ�������һ��س��س��Ϊ��������һ��س��س��Ϊ����
        4.��3��س���Ǳ�س��ʱ����ô�����Ե��Դ��Լ����Ե��Դǣ��Ա��Ե��Դ�Ϊ�������Ե��Դ�Ϊ��
        5.��4��س���Ǳ�س��ʱ���ǾͿ����ⲻ���2��س��س�ǣ�������һ��س��س��Ϊ��������һ��س��س��Ϊ��
        6.��5��س���Ǳ�س��ʱ��ֱ�ӿ�������Ǹ�س��س��
        7.��6��س���Ǳ�س��ʱ�����������Ǭ�Ի������ԣ���ô�Ϳ����þš�����������������������ԣ���ôֱ�ӿ����Ե��Դǡ�

        """
        list_res = []
        for y in list_y:
            if y % 2 == 0:
                list_res.insert(0, 0)
            else:
                list_res.insert(0, 1)
        
        e1 = tuple(list_res[0:3])
        e2 = tuple(list_res[3:6])

        # print(EightDiagrams(e1))
        # print(EightDiagrams(e2))

        gua = (EightDiagrams(e1), EightDiagrams(e2))
        return ChangesDiagrams(gua)

if __name__ == '__main__':
    div = divination()
    print(div.GUA())


    
