# -*- coding: GBK -*-

from  enum import Enum

class YAO(Enum):
	YIN = 0
	YANG = 1

class EightDiagrams(Enum):
    TIAN = (1, 1, 1)
    DI   = (0, 0, 0)
    LEI  = (0, 0, 1)
    FENG = (1, 1, 0)
    SHUI = (0, 1, 0)
    HUO  = (1, 0, 1)
    SHAN = (1, 0, 0)
    ZE   = (0, 1, 1)

class ChangesDiagrams(Enum):
    QIAN = (EightDiagrams.TIAN, EightDiagrams.TIAN, "乾为天")
    KUN  = (EightDiagrams.DI , EightDiagrams.DI , "坤为地")
    TUN  = (EightDiagrams.SHUI , EightDiagrams.LEI , "水雷屯")
    MENG  = (EightDiagrams.SHAN , EightDiagrams.SHUI , "山水蒙")
    XU  = (EightDiagrams.SHUI , EightDiagrams.TIAN , "水天需")
    SONG  = (EightDiagrams.TIAN , EightDiagrams.SHUI , "天水讼")
    SHI  = (EightDiagrams.DI , EightDiagrams.SHUI , "地水师")
    BI  = (EightDiagrams.SHUI , EightDiagrams.DI , "水地比")

    XIAOCHU = (EightDiagrams.FENG , EightDiagrams.TIAN , "风天小畜")
    LV  = (EightDiagrams.TIAN, EightDiagrams.ZE, "天泽履")
    TAI = (EightDiagrams.DI , EightDiagrams.TIAN , "地天泰")
    PI = (EightDiagrams.TIAN , EightDiagrams.DI , "天地否")
    TONGREN = (EightDiagrams.TIAN , EightDiagrams.HUO , "天火同人")
    DAYOU = (EightDiagrams.HUO , EightDiagrams.TIAN , "火天大有")
    DI_SHAN_QIAN = (EightDiagrams.DI , EightDiagrams.SHAN , "地山谦")
    YU = (EightDiagrams.LEI , EightDiagrams.DI , "雷地豫")

    SUI = (EightDiagrams.ZE , EightDiagrams.LEI , "泽雷随")
    GU = (EightDiagrams.SHAN , EightDiagrams.FENG , "山风蛊")
    LIN = (EightDiagrams.DI , EightDiagrams.ZE , "地泽临")
    GUAN = (EightDiagrams.FENG , EightDiagrams.DI , "风地观")
    SHIKE = (EightDiagrams.HUO , EightDiagrams.LEI , "火雷噬嗑")
    BEN = (EightDiagrams.SHAN , EightDiagrams.HUO , "山火贲")
    BO = (EightDiagrams.SHAN , EightDiagrams.DI , "山地剥")
    FU = (EightDiagrams.DI , EightDiagrams.LEI , "地雷复")

    WUWANG = (EightDiagrams.TIAN , EightDiagrams.LEI , "天雷无妄")
    DAXU = (EightDiagrams.SHAN , EightDiagrams.TIAN , "山天大畜")
    YI = (EightDiagrams.SHAN , EightDiagrams.LEI , "山雷颐")
    DAGUO = (EightDiagrams.ZE , EightDiagrams.FENG , "泽风大过")
    KAN  = (EightDiagrams.SHUI, EightDiagrams.SHUI, "坎为水")
    LI   = (EightDiagrams.HUO , EightDiagrams.HUO , "离为火")
    XIAN = (EightDiagrams.ZE , EightDiagrams.SHAN , "泽山咸")
    HENG = (EightDiagrams.LEI , EightDiagrams.FENG , "雷风恒")

    DUN = (EightDiagrams.TIAN , EightDiagrams.SHAN , "天山遁")
    DAZHUANG = (EightDiagrams.LEI , EightDiagrams.TIAN , "雷天大壮")
    JIN = (EightDiagrams.HUO , EightDiagrams.DI , "火地晋")
    MINGYI = (EightDiagrams.DI , EightDiagrams.HUO , "地火明夷")
    JIAREN = (EightDiagrams.FENG , EightDiagrams.HUO , "风火家人")
    KUI = (EightDiagrams.HUO , EightDiagrams.ZE , "火泽睽")
    SHUI_SHAN_QIAN = (EightDiagrams.SHUI , EightDiagrams.SHAN , "水山蹇")
    JIE = (EightDiagrams.LEI , EightDiagrams.SHUI , "雷水解")

    SUN = (EightDiagrams.SHAN , EightDiagrams.ZE , "山泽损")
    FENG_LEI_YI = (EightDiagrams.FENG , EightDiagrams.LEI , "风雷益")
    JUE = (EightDiagrams.ZE , EightDiagrams.TIAN , "泽天夬")
    GOU = (EightDiagrams.TIAN , EightDiagrams.FENG , "天风姤")
    CUI = (EightDiagrams.ZE , EightDiagrams.DI , "泽地萃")
    SHENG = (EightDiagrams.DI , EightDiagrams.FENG , "地风升")
    ZE_SHUI_KUN = (EightDiagrams.ZE , EightDiagrams.SHUI , "泽水困")
    JING = (EightDiagrams.SHUI , EightDiagrams.FENG , "水风井")

    GE = (EightDiagrams.ZE , EightDiagrams.HUO , "泽火革")
    DING = (EightDiagrams.HUO , EightDiagrams.FENG , "火风鼎")
    ZHEN = (EightDiagrams.LEI , EightDiagrams.LEI , "震为雷")
    GEN  = (EightDiagrams.SHAN, EightDiagrams.SHAN, "艮为山")
    JIAN = (EightDiagrams.FENG , EightDiagrams.SHAN , "风山渐")
    GUIMEI = (EightDiagrams.LEI , EightDiagrams.ZE , "雷泽归妹")
    FENG = (EightDiagrams.LEI , EightDiagrams.HUO , "雷火丰")
    HUO_SHAN_LV = (EightDiagrams.HUO , EightDiagrams.SHAN , "火山旅")

    XUN  = (EightDiagrams.FENG, EightDiagrams.FENG, "巽为风")
    DUI  = (EightDiagrams.ZE  , EightDiagrams.ZE  , "兑为泽")
    HUAN = (EightDiagrams.FENG , EightDiagrams.SHUI , "风水涣")
    SHUI_ZE_JIE = (EightDiagrams.SHUI , EightDiagrams.ZE , "水泽节")
    ZHONGFU = (EightDiagrams.FENG , EightDiagrams.ZE , "风泽中孚")
    XIAOGUO = (EightDiagrams.LEI , EightDiagrams.SHAN , "雷山小过")
    JIJI = (EightDiagrams.SHUI , EightDiagrams.HUO , "水火既济")
    WEIJI = (EightDiagrams.HUO , EightDiagrams.SHUI , "火水未济")

    
    
    
    
    
    

