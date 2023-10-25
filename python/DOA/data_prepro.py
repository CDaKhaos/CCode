import openpyxl as xls


class data():
    def __init__(self, signal_type, freq, time, doa, lon_p, lat_p):
        self.id = -1
        self.type = signal_type
        self.freq = freq
        self.time = time
        self.doa = doa
        self.lon_p = lon_p
        self.lat_p = lat_p
        self.lon_t = 0.0
        self.lat_t = 0.0

    def print(self):
        print(self.id, self.type, self.freq, self.time,
              self.doa, self.lon_p, self.lat_p)


class data_read():
    def __init__(self, file_name, sheet_name):
        self.wb = xls.load_workbook(file_name)
        self.ws = self.wb[sheet_name]

    def read(self):
        self.list_data: list = []
        col_index = [0, 5, 7, 11, 12]
        for row in self.ws.iter_rows(min_row=2, max_row=292, min_col=1, max_col=15, values_only=True):
            d = data('DP',
                     row[col_index[0]],
                     row[col_index[1]].timestamp(),
                     row[col_index[2]]/10,
                     row[col_index[3]],
                     row[col_index[4]])
            self.list_data.append(d)

        # sort by time
        self.list_data.sort(key = lambda x : x.time)

        # given ID
        index = 0
        for d in self.list_data:
            d.id = index
            index += 1

        # ll = list(map(lambda x : x.id, self.list_data))
        # print(ll)


        # test
        # d = data('11', 1,3,4,5,6)
        # self.list_data.append(d)
    
        return self.list_data

    def print(self):
        for data in self.list_data:
            data.print()


if __name__ == '__main__':
    data_pre = data_read('Data.xlsx', 'Sheet1')
    data_pre.read()
    data_pre.print()
