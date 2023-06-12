import random
from sin_def import get_file_addr



class c_calc():
    def __init__(self, counts, max_result):
        self.counts = counts
        self.max_result = max_result
        self.list_formula = []
        self.list_level_1 = []

    def create(self):
        self.list_formula = []
        self.list_level_1 = []
        while len(self.list_formula) < self.counts:
            x1 = random.randint(1, self.max_result)
            x2 = random.randint(1, self.max_result)
            x3 = random.randint(1, 9)
            x4 = random.randint(1, 9)

            str_symbol = self.random_symbol()
            n_res = 0

            if str_symbol == '+':  # add
                if x1 + x2 > self.max_result:
                    continue
                n_res = x1 + x2
            elif str_symbol == '-':  # sub
                if x1 < x2:
                    x1, x2 = x2, x1
                n_res = x1 - x2
            elif str_symbol == '*':
                n_res = x3 * x4
                x1, x2 = x3, x4
            elif str_symbol == '/':
                n_res = x3 * x4
                x1, x2, n_res = n_res, x3, x4

            str_formula = '%d %s %d = ' % (x1, str_symbol, x2)
            if [str_formula, n_res] in self.list_formula:
                continue

            self.list_formula.append([str_formula, n_res])

            ##########################
            # level_one : 2022.12.17 add
            list_str = [str(x1), str(x2), str(n_res)]
            x0 = random.randint(0, 2)
            list_str[x0] = '  '
            str_level_1 = '%s %s %s = %s' % (list_str[0], str_symbol, list_str[1], list_str[2])
            self.list_level_1.append(str_level_1)

        return self.list_formula

    def random_symbol(self):
        # return random.choice('+-*/')
        return random.choice('+-')

    def get_question(self):
        return list(map(lambda x: x[0], self.list_formula))
        # return self.list_question

    def get_level_1(self):
        return self.list_level_1

    def get_one_calc(self, index_list):
        if index_list < len(self.list_formula):
            return self.list_formula[index_list]
        else:
            return None

    def check_calc(self, index_list, n_res):
        return self.list_formula[index_list][1] == n_res

    def print(self):
        index = 1
        for str_calc in self.list_formula:
            str_print = '%2d:\t %s %d' % (index, str_calc[0], str_calc[1])
            print(str_print)
            index += 1

    def output(self):
        index = 1
        output_file = get_file_addr('calc', 'docx')
        calc_file = open(output_file, 'w')

        for str_calc in self.list_formula[0]:
            str_print = '%2d:\t %s =   ' % (index, str_calc)
            calc_file.write(str_print + '\n\n')
            index += 1

        calc_file.close()


if __name__ == '__main__':
    count = 10
    max_result = 20
    calc = c_calc(count, max_result)
    # print(calc.random_symbol())
    # calc.create()
    calc.create()
    print(calc.get_level_1())
#    for i in range(count+1):
#        print(calc.get_one_calc(i))
    # calc.print()
