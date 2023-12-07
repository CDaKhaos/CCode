# interface
import sys as ss
import math
import copy

# 测向线

# 测向线长度（最大探测距离(100KM)）
setting_len_doa = 3
# 定位校准距离（100KM）
setting_pos_min = 0.1
# 测向线融合-时间（s）
setting_megre_doa_time = 10
# 测向线融合-角度（s）
setting_megre_doa_angel = 8
# 删除原始数据集合小于门限值的结论
setting_del_target = 5


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
        return (dis > setting_pos_min) & True  # (dis < setting_pos_max)


class location():
    def __init__(self):
        self.lons = []
        self.lats = []
        self.doas = []
        self.times = []

        self.list_pos: list = []
        self.list_doa_line: list = []
        pass

    def set_data(self, list_lon: list, list_lat: list, list_doa: list, list_time: list):
        self.list_lon = list_lon
        self.list_lat = list_lat
        self.list_doa = list_doa
        self.list_time = list_time

    """
    # 测向线长度（最大探测距离(100KM)）
    setting_len_doa = 3
    # 定位校准距离（100KM）
    setting_pos_min = 0.1
    # 测向线融合-时间（s）
    setting_megre_doa_time = 10
    # 测向线融合-角度（s）
    setting_megre_doa_angel = 8
    # 删除原始数据集合小于门限值的结论
    setting_del_target = 5
    """
    def set_config(self, rule_len_doa, rule_pos_min, rule_doa_time, rule_doa_angel):
        setting_len_doa = rule_len_doa
        setting_pos_min = rule_pos_min 
        setting_megre_doa_time = rule_doa_time   
        setting_megre_doa_angel = rule_doa_angel

    def get_location(self):
        assert (len(self.list_lon) != 0)
        assert (len(self.list_lon) == len(self.list_lat))
        assert (len(self.list_lon) == len(self.list_doa))
        assert (len(self.list_lon) == len(self.list_time))

        return self.get_pos()

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
            lon = self.list_lon[index]
            lat = self.list_lat[index]

            # construct line
            rad = math.radians(doa)
            x = lon + setting_len_doa * math.cos(rad)
            y = lat + setting_len_doa * math.sin(rad)
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
        return self.list_pos


def data_input():
    strs = ['D:\\work\\111\\location.py', '[104.01928,107.88459]', '[30.57700,30.36498]', '[55,340]', '[1698734788,1698784788]', '3', '0.1', '10', '8'] 
    # strs = ss.argv
    # print(strs)
    list_str = []
    turn = []
    for i in range(1, len(strs)):
        # print(strs[i])
        strA = strs[i]
        strA = strA.replace('[', '').replace(']', '')
        # print(strA)
        turn = strA.split(',')
        turn = list(map(float, turn))
        # print(turn)
        list_str.append(turn)

    return list_str
    # if list_str:
        # lons = list_str[0]
        # lats = list_str[1]
        # doas = list_str[2]
        # times = list_str[3]
        # rule1 = list_str[4][0]
        # rule2 = list_str[5][0]

    # list_res = []
    # list_res.append((lons[0], lats[0]))
    # list_res.append((lons[2], lats[2]))
    # list_res.append((lons[3], lats[3]))
    # print(list_res)

"""
输入：
list: 经度列表
list: 纬度列表
list: 测向列表
list: 时间列表
float: 测向线长度（最大探测距离(100KM)） 默认3
float: 定位校准距离（100KM）默认0.1
float: 测向线融合-时间（s） 默认10
float: 测向线融合-角度（度） 默认8

输出：一个或者多个位置，格式如下
[(x, y),(x1, y1)]
"""
if __name__ == '__main__':
    datas = data_input()

    if len(datas) < 8:
        print("input error")
    else:
        loc = location()
        loc.set_data(datas[0], datas[1], datas[2], datas[3])
        loc.set_config(datas[4][0], datas[5][0], datas[6][0], datas[7][0])

        print(loc.get_location())
