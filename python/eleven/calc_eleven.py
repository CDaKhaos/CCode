import random
from sin_def import get_file_addr


class c_calc():
    def __init__(self, counts, max_result, list_result=[], list_num=[]):
        self.counts = counts
        self.max_result = max_result
        self.list_result = list_result
        self.list_num = list_num

    def create(self):
        self.list_result = []
        self.list_num = []
        while len(self.list_result) < self.counts:
            x1 = random.randint(1, self.max_result)
            x2 = random.randint(1, self.max_result)

            n_symbol = random.randint(1, 2)
            str_symbol = ''
            n_res = 0

            if n_symbol == 1:  # add
                if x1 + x2 > self.max_result:
                    continue
                str_symbol = '+'
                n_res = x1 + x2
            elif n_symbol == 2:  # sub
                if x1 < x2:
                    x1, x2 = x2, x1
                str_symbol = '-'
                n_res = x1 - x2

            str = '%d %s %d = ' % (x1, str_symbol, x2)
            if str in self.list_result:
                continue

            self.list_result.append(str)
            self.list_num.append([str, n_res])
        # print(self.list_num)
        return self.list_num

    def get_question(self):
        return self.list_result

    def get_one_calc(self, index_list):
        if index_list < len(self.list_num):
            return self.list_num[index_list]
        else:
            return None

    def check_calc(self, index_list, n_res):
        return self.list_num[index_list][1] == n_res

    def print(self):
        index = 1
        for str_calc in self.list_result:
            str_print = '%2d:\t %s    ' % (index, str_calc)
            print(str_print)
            index += 1

    def output(self):
        index = 1
        output_file = get_file_addr('calc', 'docx')
        calc_file = open(output_file, 'w')

        for str_calc in self.list_result:
            str_print = '%2d:\t %s =   ' % (index, str_calc)
            calc_file.write(str_print + '\n\n')
            index += 1

        calc_file.close()


if __name__ == '__main__':
    count = 50
    max_result = 20
    calc = c_calc(count, max_result)
    calc.create()
    # calc.create()
#    for i in range(count+1):
#        print(calc.get_one_calc(i))
    calc.print()
    # calc.output()
