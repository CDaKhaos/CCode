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
        # 1.把49随机分成两份（天、地）
        rand = num
        rand_temp = int(rand / 1.3141592)
        left = random.randint(rand - rand_temp, rand + rand_temp)
        right = num - left

        # 2.从任意一组那条一个（人）
        right -= 1

        # 3.天 除以 4 ，得到余数，如果整除，余数为4，从天中减去余数
        l = self.__div(left)

        # 4.地 按照第三步做
        r = self.__div(right)

        # 5.2步 1个 + 3 步余数 + 4步余数  （不是9，就是5）
        res = 1 + l + r
        num -= res
        return res

    # 二变 
    # 1.两份剩余的重新组合，重复一变的过程，5步过后，不是4，就是8

    # 三变，重复第二变

    # 三变走完，只能是24,28,32,96
    # 用这个数除以 4 得到爻，为初，放在最下面
    def __YAO(self):
        n = 49
        c = 0
        list_c = []
        for i in range(0, 3):
            c = self.__Change(n)
            n -= c
        return int(n / 4)

    # 重复6次，得到一个挂， 7、9为阳，6、8为阴；6是老阴，9是老阳
    # 老变少不变
    def GUA(self):
        list_y = []
        for i in range(0, 6):
            list_y.append(self.__YAO())

        """ 
        变爻-朱熹
        1.6个爻都没有变爻，6爻组成的本卦卦辞
        2.一个爻发生了变化，这个爻的爻辞
        3.当2个爻都是变爻的时候，那么就要看这2个爻的爻辞，以上面一个爻的爻辞为主，下面一个爻的爻辞为辅。
        4.当3个爻都是变爻的时候，那么看本卦的卦辞以及变卦的卦辞，以本卦的卦辞为主，变卦的卦辞为辅
        5.当4个爻都是变爻的时候，那就看另外不变的2个爻的爻辞，以下面一个爻的爻辞为主，上面一个爻的爻辞为辅
        6.当5个爻都是变爻的时候，直接看不变的那个爻的爻辞
        7.当6个爻都是变爻的时候，如果本卦是乾卦或者坤卦，那么就看“用九”跟“用六”，如果是其他卦，那么直接看变卦的卦辞。

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


    
