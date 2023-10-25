import data_prepro as prepro
import matplotlib.pyplot as plt
import numpy as np
import colorset
import math
import copy

setting_megre_freq = 1
setting_seperate_time = 60*30
setting_len_doa = 5
setting_pos_min = 1
setting_pos_max = 5
setting_megre_doa_time = 10
setting_megre_doa_angel = 8


class line():
    def __init__(self, p1: list, p2: list):
        A = p1[1] - p2[1]
        B = p2[0] - p1[0]
        C = (p1[0] * p2[1] - p2[0] * p1[1])
        self.line_data = (A, B, -C)

        self.p1 = p1
        self.p2 = p2

    def get(self):
        return self.line_data

    def intersection(self, other):
        l1 = self.get()
        l2 = other.get()
        D = l1[0] * l2[1] - l1[1] * l2[0]
        Dx = l1[2] * l2[1] - l1[1] * l2[2]
        Dy = l1[0] * l2[2] - l1[2] * l2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            bret = self.dis(self.p1, x, y) & self.dis(other.p1, x, y)

            xmin = min(self.p1[0], self.p2[0])
            xmax = max(self.p1[0], self.p2[0])
            ymin = min(self.p1[1], self.p2[1])
            ymax = max(self.p1[1], self.p2[1])
            brange = (x > xmin) & (x < xmax) & (y > ymin) & (y < ymax)

            if bret & brange:
                return x, y
        return False

    def dis(self, pos: list, x, y):
        x1 = pos[0] - x
        y1 = pos[1] - y
        dis = math.sqrt(x1 * x1 + y1 * y1)
        return (dis > setting_pos_min) & (dis < setting_pos_max)

    def show(self, plt):
        plt.plot((self.p1[0], self.p2[0]),
                 (self.p1[1], self.p2[1]), color='blue')


class result_freqlist():
    def __init__(self):
        self.id = 0
        self.type = ''

        self.controy = ''
        self.plat_name = ''
        self.plat_kind = ''
        self.radio_name = ''

        self.freq_min = 0
        self.freq_max = 0
        self.freq = 0       # mid_freq
        self.set_freq: set = set()
        self.list_freq: list = []

        self.time_start = 0
        self.time_end = 0
        self.time_duration = 0
        self.list_time: list = []

        self.list_doa: list = []

        self.list_lon_p: list = []
        self.list_lat_p: list = []

        self.list_lon_t: list = []
        self.list_lon_t: list = []

        self.list_id: list = []

        # temp
        self.list_doa_line: list = []
        self.list_pos: list = []

    def print(self):
        print(self.id, self.set_freq, self.time_start,
              self.time_duration, self.list_id)

    def _add_param(self, data):
        self.set_freq.add(data.freq)
        self.list_freq.append(data.freq)
        self.list_time.append(data.time)
        self.list_doa.append(data.doa)
        self.list_lon_p.append(data.lon_p)
        self.list_lat_p.append(data.lat_p)
        self.list_id.append(data.id)

    def add_one(self, data):
        self.type = data.type
        self.freq = data.freq
        self.time_start = self.time_end = data.time
        self._add_param(data)

    def add_ori(self, data):
        if (data.time - self.time_end < setting_seperate_time) & (math.fabs(data.freq - self.freq) < setting_megre_freq):   # merge
            self.time_end = data.time
            self._add_param(data)
            return True
        else:       # new
            return False

    def pro_data(self):
        self.time_start = min(self.list_time)
        self.time_end = max(self.list_time)
        self.time_duration = self.time_end - self.time_start

        self.freq_min = min(self.set_freq)
        self.freq_max = min(self.set_freq)
        self.freq = (self.freq_min + self.freq_max) / 2

    def _cons_doa(self):
        self.list_doa_line.clear()

        list_lines = []
        lines = []
        time_temp = self.list_time[0]
        doa_temp = self.list_doa[0]
        for doa, time, index in zip(self.list_doa, self.list_time, range(0, len(self.list_doa))):
            if (time - time_temp < setting_megre_doa_time) & (math.fabs(doa - doa_temp) < setting_megre_doa_angel):
                lines.append(index)
            else:
                list_lines.append(copy.deepcopy(lines))
                lines.clear()
                time_temp = time
                doa_temp = doa
                lines.append(index)

        if lines:
            list_lines.append(lines)

        for l in list_lines:
            index = l[0]
            doa = self.list_doa[index]
            lon = self.list_lon_p[index]
            lat = self.list_lat_p[index]

            rad = np.radians(doa)
            x = lon + setting_len_doa * np.cos(rad)
            y = lat + setting_len_doa * np.sin(rad)
            self.list_doa_line.append(line((lon, lat), (x, y)))

        # print(lines)

        return len(self.list_doa_line) > 0

    def get_pos(self):
        if self._cons_doa() == False:
            return False
        index = 0
        for l1 in self.list_doa_line:
            index += 1
            for l2 in self.list_doa_line[index:]:
                pos = l1.intersection(l2)
                if pos != False:
                    self.list_pos.append(pos)
        print("pos count:", len(self.list_pos))


class pro_freqlist():
    def __init__(self, data):
        self.data_ori = data
        self.list_result: list = []

    def new_res(self, ori):
        res = result_freqlist()
        res.add_one(ori)
        self.list_result.append(res)

    def pro(self):
        self.new_res(self.data_ori[0])
        for ori in self.data_ori[1:]:
            is_new = False
            for res in reversed(self.list_result):
                if res.add_ori(ori) == True:  # merge
                    is_new = False
                    break
                else:          # new
                    is_new = True
            if is_new == True:
                self.new_res(ori)

        index = 0
        for res in self.list_result:
            res.id = index
            res.pro_data()
            index += 1

            res.get_pos()

        # print(len(self.list_result))
        # for x in self.list_result:
            # x.print()

    def show(self):
        plt.figure()
        i = 0
        colors = colorset.get_colors()
        # print(colors[1][0])
        plt.subplot(1, 2, 1)
        for x in self.list_result:
            plt.scatter(x.list_time, x.list_freq, c=colors[i], label=x.freq)
            i += 1
        plt.legend()
        plt.title("freq")

        i = 0
        plt.subplot(1, 2, 2)
        for x in self.list_result:
            plt.scatter(x.list_time, x.list_doa, c=colors[i], label=x.freq)
            i += 1
        plt.title("doa")

        plt.legend()
        plt.show()

    def show_doa_time(self):
        plt.figure()
        num = len(self.list_result)
        row = int(num / 4) + 1
        col = 5
        i = 1
        for x in self.list_result:
            plt.subplot(row, col, i)
            i += 1
            plt.scatter(x.list_time, x.list_doa)
            plt.title(x.freq)

        plt.legend()
        plt.show()

    def show_doa(self):
        plt.figure()
        num = len(self.list_result)
        col = 4
        row = int(num / col) + 1
        i = 1
        doa_len = 10
        for data in self.list_result:
            # if len(data.list_id) < 5:
            # continue

            plt.subplot(row, col, i)
            i += 1
            plt.plot(data.list_lon_p, data.list_lat_p,
                     color="black", marker='*')

            for doa in data.list_doa_line:
                doa.show(plt)

            if len(data.list_pos) < 1000:
                for pos in data.list_pos:
                    plt.scatter(pos[0], pos[1], color='red')

            plt.title(str(data.freq))

        plt.legend()
        plt.show()


if __name__ == '__main__':
    data_pre = prepro.data_read('Data.xlsx', 'Sheet1')
    pre_f = pro_freqlist(data_pre.read())
    pre_f.pro()
    pre_f.show_doa()
