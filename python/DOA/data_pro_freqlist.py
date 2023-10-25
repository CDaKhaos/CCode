import data_prepro as prepro
import copy

setting_megre_freq = 5
setting_seperate_time = 60


class result_freqlist():
    def __init__(self):
        self.id = 0
        self.type = ''

        self.freq_min = 0
        self.freq_max = 0
        self.freq = 0       # mid_freq
        self.set_freq: set = []

        self.time_start = 0
        self.time_end = 0
        self.time_duration = 0

        self.list_doa: list = []

        self.list_lon_p: list = []
        self.list_lat_p: list = []

        self.list_lon_t: list = []
        self.list_lon_t: list = []

        self.list_id: list = []

    def pro_data(self, list_time, list_freq):
        self.time_start = min(list_time)
        self.time_end = max(list_time)
        self.time_duration = self.time_end - self.time_start

        self.set_freq = set(list_freq)
        self.freq_min = min(self.set_freq)
        self.freq_max = min(self.set_freq)
        self.freq = (self.freq_min + self.freq_max) / 2


class data_freq_set():
    def __init__(self):
        self.set_freq: set = []
        self.list_id: list = []

    def add(self, freq, num):
        self.list_id.append(num)
        self.set_freq.append(freq)

    def merge(self, freq_set):
        self.list_id = self.list_id + freq_set.list_id
        self.set_freq = self.set_freq + freq_set.set_freq

    def print(self):
        print("     freq_set:", self.list_id)


class data_freq_dict():
    def __init__(self):
        # key : freq
        # value : data_freq_set
        self.dt_freq: dict = {}

    def add(self, data):
        if data.freq not in self.dt_freq:
            self.dt_freq[data.freq] = data_freq_set()
        self.dt_freq[data.freq].add(data.freq, data.id)

    def sort_key(self):
        self.dt_freq = dict(sorted(self.dt_freq.items(), key=lambda x: x[0]))
        # print(self.dt_freq)

    def merge_freq(self):
        keys = list(self.dt_freq.keys())
        # print(keys)
        v_temp = keys[0]
        for v in keys[1:]:
            if v - v_temp < setting_megre_freq:
                # print(v)
                self.dt_freq[v_temp].merge(self.dt_freq[v])
                del self.dt_freq[v]
            else:
                v_temp = v

        # keys = list(self.dt_freq.keys())
        # print(keys)

    def print(self):
        for key, value in self.dt_freq.items():
            print(" ###freq_set")
            print(" key:", key)
            print(" value:", value.print())

    def get_freq(self):
        return self.freq


class data_type_dict():
    def __init__(self):
        # key: type
        # value: list_freq_dict = []
        self.dt_type: dict = {}

    def add(self, data):
        if data.type not in self.dt_type:
            self.dt_type[data.type] = data_freq_dict()
        self.dt_type[data.type].add(data)

    def sort_key(self):
        for value in self.dt_type.values():
            value.sort_key()

    def merge_freq(self):
        for value in self.dt_type.values():
            value.merge_freq()

    def print(self):
        for key, value in self.dt_type.items():
            print("###type")
            print("key:", key)
            print("value:", value.print())


class pro_freqlist():
    def __init__(self, data):
        self.data_ori = data
        self.list_data_time: list = []
        self.list_dict_type: list = []

        self.list_dict_merge_freq: list = []
        self.list_result: list = []

    def pro(self):
        self.seperate_time()
        self.data_prepro()
        self.merge_freq()

        self.get_result()

    def seperate_time(self):
        list_data: list = []
        t_temp = 0
        for data in self.data_ori:
            if data.time - t_temp > setting_seperate_time:
                # print(data.time, data.id)
                if list_data:
                    self.list_data_time.append(list_data)
                    # print(len(list_data))
                list_data.clear()

            list_data.append(data)
            t_temp = data.time

        # last
        if list_data:
            self.list_data_time.append(list_data)
            # print(len(list_data))

        # print(len(self.list_data_time))

    def data_prepro(self):
        for list_data in self.list_data_time:
            for data in list_data:
                dict_type = data_type_dict()
                dict_type.add(data)
                dict_type.sort_key()
                self.list_dict_type.append(dict_type)

    def merge_freq(self):
        # copy
        self.list_dict_merge_freq = copy.deepcopy(self.list_dict_type)
        # merge
        for data in self.list_dict_merge_freq:
            data.merge_freq()
            data.print()

        # self.dict_type.print()
        # print("")
        # self.dict_merge_freq.print()

    def get_result(self):
        for data in self.list_dict_merge_freq:
            for t, dict_f in data.dt_type.items():
                for f_set in dict_f.dt_freq.values():
                    res = result_freqlist()
                    res.signal_type = t
                    res.list_id = f_set.list_id
                    print(res.list_id)
                    self.list_result.append(res)


        for res in self.list_result:
            list_temp = list(map(lambda x: self.data_ori[x], res.list_id))

            time = list(map(lambda d: d.time, list_temp))
            freq = list(map(lambda d: d.freq, list_temp))

            res.pro_data(time, freq)

            print(res.__dict__)

    def print(self):
        self.dict_type.print()


if __name__ == '__main__':
    data_pre = prepro.data_read('Data.xlsx', 'Sheet1')
    pre_f = pro_freqlist(data_pre.read())
    pre_f.pro()
    pre_f.get_result()
    # pre_f.print()
