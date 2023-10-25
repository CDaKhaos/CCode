"""
处理类-合批、定位
"""

import data_prepro as prepro
import matplotlib.pyplot as plt
import numpy as np
import colorset
import math
import copy

# 配置
# 合批门限-频率（MHz）
setting_megre_freq = 1
# 合批门限-时间(s)
setting_seperate_time = 60*30
# 测向线长度（最大探测距离(100KM)）
setting_len_doa = 3
# 定位校准距离（100KM）
setting_pos_min = 0.1
setting_pos_max = 3
# 测向线融合-时间（s）
setting_megre_doa_time = 10
# 测向线融合-角度（s）
setting_megre_doa_angel = 8
# 删除原始数据集合小于门限值的结论
setting_del_target = 5


# 测向线
class line():
    def __init__(self, p1: list, p2: list):
        # 斜率属性
        A = p1[1] - p2[1]
        B = p2[0] - p1[0]
        C = (p1[0] * p2[1] - p2[0] * p1[1])
        self.line_data = (A, B, -C)

        # 两点
        self.p1 = p1
        self.p2 = p2

    def get(self):
        return self.line_data

    # 判断交点
    def intersection(self, other):
        l1 = self.get()
        l2 = other.get()
        D = l1[0] * l2[1] - l1[1] * l2[0]
        Dx = l1[2] * l2[1] - l1[1] * l2[2]
        Dy = l1[0] * l2[2] - l1[2] * l2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            # 定位点距离交点太近 不需要
            bret = self.dis(self.p1, x, y) & self.dis(other.p1, x, y)

            # 交点在线段内
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

    # 展示
    def show(self, plt):
        plt.plot((self.p1[0], self.p2[0]),
                 (self.p1[1], self.p2[1]), color='blue')

# 结论表


class result_freqlist():
    def __init__(self):
        self.id = 0
        self.type = ''              # 原始-信号类型

        self.controy = ''           # 识别-国家地区
        self.plat_name = ''         # 识别-平台名称
        self.plat_kind = ''         # 识别-平台类型
        self.radio_name = ''        # 识别-电台名称

        self.freq_min = 0           # 计算-最小频率
        self.freq_max = 0           # 计算-最大频率
        self.freq = 0               # 原始_频率，根据门限合批
        self.set_freq: set = set()  # 原始积累-频表
        self.list_freq: list = []   # 原始积累-频率列表，用于标绘使用

        self.time_start = 0         # 计算-起始时间
        self.time_end = 0           # 计算-终止时间
        self.time_duration = 0      # 计算-持续时间
        self.list_time: list = []   # 原始积累-时间列表，用于标绘使用

        self.list_doa: list = []    # 原始积累-测向方位列表，用于标绘、和定位计算使用

        self.list_lon_p: list = []  # 原始积累-飞机经度
        self.list_lat_p: list = []  # 原始积累-飞机纬度

        self.list_lon_t: list = []  # 原始积累-目标经度
        self.list_lat_t: list = []  # 原始积累-目标纬度

        self.list_id: list = []     # 原始积累-id

        self.list_doa_line: list = []   # 计算-测向线集合
        self.list_pos: list = []        # 计算-定位结果

    def print(self):
        print(self.id, self.set_freq, self.time_start,
              self.time_duration, self.list_id)

    # 合批-添加参数
    def _add_param(self, data):
        self.set_freq.add(data.freq)
        self.list_freq.append(data.freq)
        self.list_time.append(data.time)
        self.list_doa.append(data.doa)
        self.list_lon_p.append(data.lon_p)
        self.list_lat_p.append(data.lat_p)
        self.list_id.append(data.id)

    # 合批-增加新的
    def add_one(self, data):
        self.type = data.type
        self.freq = data.freq
        self.time_start = self.time_end = data.time
        self._add_param(data)

    # 合批-比较
    def add_ori(self, data):
        if (data.time - self.time_end < setting_seperate_time) & (math.fabs(data.freq - self.freq) < setting_megre_freq):   # merge
            self.time_end = data.time
            self._add_param(data)
            return True
        else:       # new
            return False

    # 计算中间显示数据
    def pro_data(self):
        self.time_start = min(self.list_time)
        self.time_end = max(self.list_time)
        self.time_duration = self.time_end - self.time_start

        self.freq_min = min(self.set_freq)
        self.freq_max = min(self.set_freq)
        self.freq = (self.freq_min + self.freq_max) / 2

    # 构造测向线
    def _cons_doa(self):
        self.list_doa_line.clear()

        # 测向方位合批 通过时间和角度
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

        # 取合并测向方位的第一个数据，计算成测向线
        for l in list_lines:
            index = l[0]
            doa = self.list_doa[index]
            lon = self.list_lon_p[index]
            lat = self.list_lat_p[index]

            rad = np.radians(doa)
            x = lon + setting_len_doa * np.cos(rad)
            y = lat + setting_len_doa * np.sin(rad)
            self.list_doa_line.append(line((lon, lat), (x, y)))
        return len(self.list_doa_line) > 0

    # 根据测向线定位
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


# 处理
class pro_freqlist():
    def __init__(self, data):
        self.data_ori = data            # 原始数据
        self.list_result: list = []     # 结论数据

    # 新建结论数据
    def new_res(self, ori):
        res = result_freqlist()
        res.add_one(ori)
        self.list_result.append(res)

    # 处理过程
    def pro(self):
        # 合批
        self.new_res(self.data_ori[0])      # 第一个是新建
        for ori in self.data_ori[1:]:
            is_new = False
            # 反向遍历结论表比较
            for res in reversed(self.list_result):
                if res.add_ori(ori) == True:  # merge
                    is_new = False
                    break
                else:          # new
                    is_new = True
            if is_new == True:
                self.new_res(ori)

        # 定位
        index = 0
        for res in self.list_result[:]:
            # delete 
            if len(res.list_id) < setting_del_target:
                self.list_result.remove(res)
                continue

            res.id = index
            res.pro_data()
            index += 1

            print(len(res.list_id))
            res.get_pos()

        # 识别

        # print(len(self.list_result))
        # for x in self.list_result:
            # x.print()

    # 所有的目标：时间测向，时间频率展示

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

    # 分别展示所有目标时间测向
    def show_doa_time(self):
        plt.figure()
        num = len(self.list_result)
        row = int(num / 4) + (lambda x:1 if (x > 0) else 0)(num % 4)
        print("row:", row)
        col = 5
        i = 1
        for x in self.list_result:
            plt.subplot(row, col, i)
            i += 1
            plt.scatter(x.list_time, x.list_doa)
            plt.title(x.freq)

        plt.legend()
        plt.show()

    # 展示航迹、测向线、定位结果
    def show_doa(self):
        plt.figure()
        num = len(self.list_result)
        col = 4
        row = int(num / 4) + (lambda x:1 if (x > 0) else 0)(num % 4)
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
    # pre_f.show()
    # pre_f.show_doa_time()
    pre_f.show_doa()
