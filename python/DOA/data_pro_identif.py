from datetime import datetime
import matplotlib.pyplot as plt


class c_pos():
    def __init__(self, lon, lat, time):
        self.lon = lon
        self.lat = lat
        self.time = time


class c_track():
    def __init__(self):
        self.lons: list = []
        self.lats: list = []
        self.times: list = []

    def add(self, lon, lat, time):
        self.lons.append(lon)
        self.lats.append(lat)
        self.times.append(time)


def dms_conver(str_dms):
    s = str_dms.replace('°', ',').replace('′', ',').replace('″', '')
    t1 = s.split(',')
    t1 = list(map(int, t1))

    decimal = t1[0] + float(t1[1])/60 + float(t1[2])/3600
    return decimal


class knowledge():
    def __init__(self):
        self.plat_type = 'fix'
        self.track = c_track()

        with open("HKQ.txt", encoding='gb18030') as file:
            lines = file.readlines()
        track = lines[45:200]

        for tt in track:
            turn = tt.split('\t')
            lon = dms_conver(turn[0])
            lat = dms_conver(turn[1]),
            time = datetime.strptime(turn[2], '%Y-%m-%d %H:%M:%S').timestamp()
            self.track.add(lon, lat, time)

    def show(self):
        plt.figure()
        lons = self.track.lons
        lats = self.track.lats
        plt.plot(lons, lats,
                 color="grey", marker='*')
        plt.scatter(lons[0], lats[0], s=100, c='red')
        plt.scatter(lons[-1], lats[-1], s=100, c='blue')

        plt.show()


class pro_identif():
    def __init__(self):
        self._read_knowledge()
        self.lons: list = []
        self.lats: list = []
        self.times: list = []
        self.list_knowledes: list = []
        pass

    def _read_knowledge(self):
        pass

    def set_data(self, lons, lats, times):
        self.lons = lons
        self.lats = lats
        self.times = times
        pass

    def identifi(self):
        for time, index in zip(self.times, len(self.times)):
            for ktime, kindex in zip(self.list_konwledes.times, len(self.list_knowledes.times)):
                pass


if __name__ == '__main__':
    knde = knowledge()
    knde.show()
