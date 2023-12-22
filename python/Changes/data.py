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
    QIAN = (EightDiagrams.TIAN, EightDiagrams.TIAN)
    KUN  = (EightDiagrams.DI , EightDiagrams.DI)
    ZHUN  = (EightDiagrams.SHUI , EightDiagrams.LEI)
    MENG  = (EightDiagrams.SHAN , EightDiagrams.SHUI)
    XU  = (EightDiagrams.SHUI , EightDiagrams.TIAN)
    SONG  = (EightDiagrams.TIAN , EightDiagrams.SHUI)
    SHI  = (EightDiagrams.DI , EightDiagrams.SHUI)
    BI  = (EightDiagrams.SHUI , EightDiagrams.DI)

    XIAOXU = (EightDiagrams.FENG , EightDiagrams.TIAN)
    LV  = (EightDiagrams.TIAN, EightDiagrams.ZE)
    TAI = (EightDiagrams.DI , EightDiagrams.TIAN)
    PI = (EightDiagrams.TIAN , EightDiagrams.DI)
    TONGREN = (EightDiagrams.TIAN , EightDiagrams.HUO)
    DAYOU = (EightDiagrams.HUO , EightDiagrams.TIAN)
    DI_SHAN_QIAN = (EightDiagrams.DI , EightDiagrams.SHAN)
    YU = (EightDiagrams.LEI , EightDiagrams.DI)

    SUI = (EightDiagrams.ZE , EightDiagrams.LEI)
    GU = (EightDiagrams.SHAN , EightDiagrams.FENG)
    LIN = (EightDiagrams.DI , EightDiagrams.ZE)
    GUAN = (EightDiagrams.FENG , EightDiagrams.DI)
    SHIKE = (EightDiagrams.HUO , EightDiagrams.LEI)
    BEN = (EightDiagrams.SHAN , EightDiagrams.HUO)
    BO = (EightDiagrams.SHAN , EightDiagrams.DI)
    FU = (EightDiagrams.DI , EightDiagrams.LEI)

    WUWANG = (EightDiagrams.TIAN , EightDiagrams.LEI)
    DAXU = (EightDiagrams.SHAN , EightDiagrams.TIAN)
    YI = (EightDiagrams.SHAN , EightDiagrams.LEI)
    DAGUO = (EightDiagrams.ZE , EightDiagrams.FENG )
    KAN  = (EightDiagrams.SHUI, EightDiagrams.SHUI)
    LI   = (EightDiagrams.HUO , EightDiagrams.HUO)
    XIAN = (EightDiagrams.ZE , EightDiagrams.SHAN)
    HENG = (EightDiagrams.LEI , EightDiagrams.FENG)

    DUN = (EightDiagrams.TIAN , EightDiagrams.SHAN)
    DAZHUANG = (EightDiagrams.LEI , EightDiagrams.TIAN)
    JIN = (EightDiagrams.HUO , EightDiagrams.DI)
    MINGYI = (EightDiagrams.DI , EightDiagrams.HUO)
    JIAREN = (EightDiagrams.FENG , EightDiagrams.HUO)
    KUI = (EightDiagrams.HUO , EightDiagrams.ZE)
    SHUI_SHAN_QIAN = (EightDiagrams.SHUI , EightDiagrams.SHAN)
    JIE = (EightDiagrams.LEI , EightDiagrams.SHUI)

    SUN = (EightDiagrams.SHAN , EightDiagrams.ZE)
    FENG_LEI_YI = (EightDiagrams.FENG , EightDiagrams.LEI)
    JUE = (EightDiagrams.ZE , EightDiagrams.TIAN)
    GOU = (EightDiagrams.TIAN , EightDiagrams.FENG)
    CUI = (EightDiagrams.ZE , EightDiagrams.DI)
    SHENG = (EightDiagrams.DI , EightDiagrams.FENG)
    ZE_SHUI_KUN = (EightDiagrams.ZE , EightDiagrams.SHUI)
    JING = (EightDiagrams.SHUI , EightDiagrams.FENG)

    GE = (EightDiagrams.ZE , EightDiagrams.HUO)
    DING = (EightDiagrams.HUO , EightDiagrams.FENG)
    ZHEN = (EightDiagrams.LEI , EightDiagrams.LEI)
    GEN  = (EightDiagrams.SHAN, EightDiagrams.SHAN)
    JIAN = (EightDiagrams.FENG , EightDiagrams.SHAN)
    GUIMEI = (EightDiagrams.LEI , EightDiagrams.ZE)
    FENG = (EightDiagrams.LEI , EightDiagrams.HUO)
    HUO_SHAN_LV = (EightDiagrams.HUO , EightDiagrams.SHAN)

    XUN  = (EightDiagrams.FENG, EightDiagrams.FENG)
    DUI  = (EightDiagrams.ZE  , EightDiagrams.ZE )
    HUAN = (EightDiagrams.FENG , EightDiagrams.SHUI)
    SHUI_ZE_JIE = (EightDiagrams.SHUI , EightDiagrams.ZE)
    ZHONGFU = (EightDiagrams.FENG , EightDiagrams.ZE)
    XIAOGUO = (EightDiagrams.LEI , EightDiagrams.SHAN)
    JIJI = (EightDiagrams.SHUI , EightDiagrams.HUO)
    WEIJI = (EightDiagrams.HUO , EightDiagrams.SHUI)

class ChangesName(Enum):
    QIAN = (EightDiagrams.TIAN, EightDiagrams.TIAN, "ǬΪ��")
    KUN  = (EightDiagrams.DI , EightDiagrams.DI , "��Ϊ��")
    ZHUN  = (EightDiagrams.SHUI , EightDiagrams.LEI , "ˮ����")
    MENG  = (EightDiagrams.SHAN , EightDiagrams.SHUI , "ɽˮ��")
    XU  = (EightDiagrams.SHUI , EightDiagrams.TIAN , "ˮ����")
    SONG  = (EightDiagrams.TIAN , EightDiagrams.SHUI , "��ˮ��")
    SHI  = (EightDiagrams.DI , EightDiagrams.SHUI , "��ˮʦ")
    BI  = (EightDiagrams.SHUI , EightDiagrams.DI , "ˮ�ر�")

    XIAOXU = (EightDiagrams.FENG , EightDiagrams.TIAN , "����С��")
    LV  = (EightDiagrams.TIAN, EightDiagrams.ZE, "������")
    TAI = (EightDiagrams.DI , EightDiagrams.TIAN , "����̩")
    PI = (EightDiagrams.TIAN , EightDiagrams.DI , "��ط�")
    TONGREN = (EightDiagrams.TIAN , EightDiagrams.HUO , "���ͬ��")
    DAYOU = (EightDiagrams.HUO , EightDiagrams.TIAN , "�������")
    DI_SHAN_QIAN = (EightDiagrams.DI , EightDiagrams.SHAN , "��ɽǫ")
    YU = (EightDiagrams.LEI , EightDiagrams.DI , "�׵�ԥ")

    SUI = (EightDiagrams.ZE , EightDiagrams.LEI , "������")
    GU = (EightDiagrams.SHAN , EightDiagrams.FENG , "ɽ���")
    LIN = (EightDiagrams.DI , EightDiagrams.ZE , "������")
    GUAN = (EightDiagrams.FENG , EightDiagrams.DI , "��ع�")
    SHIKE = (EightDiagrams.HUO , EightDiagrams.LEI , "�������")
    BEN = (EightDiagrams.SHAN , EightDiagrams.HUO , "ɽ����")
    BO = (EightDiagrams.SHAN , EightDiagrams.DI , "ɽ�ذ�")
    FU = (EightDiagrams.DI , EightDiagrams.LEI , "���׸�")

    WUWANG = (EightDiagrams.TIAN , EightDiagrams.LEI , "��������")
    DAXU = (EightDiagrams.SHAN , EightDiagrams.TIAN , "ɽ�����")
    YI = (EightDiagrams.SHAN , EightDiagrams.LEI , "ɽ����")
    DAGUO = (EightDiagrams.ZE , EightDiagrams.FENG , "�����")
    KAN  = (EightDiagrams.SHUI, EightDiagrams.SHUI, "��Ϊˮ")
    LI   = (EightDiagrams.HUO , EightDiagrams.HUO , "��Ϊ��")
    XIAN = (EightDiagrams.ZE , EightDiagrams.SHAN , "��ɽ��")
    HENG = (EightDiagrams.LEI , EightDiagrams.FENG , "�׷��")

    DUN = (EightDiagrams.TIAN , EightDiagrams.SHAN , "��ɽ��")
    DAZHUANG = (EightDiagrams.LEI , EightDiagrams.TIAN , "�����׳")
    JIN = (EightDiagrams.HUO , EightDiagrams.DI , "��ؽ�")
    MINGYI = (EightDiagrams.DI , EightDiagrams.HUO , "�ػ�����")
    JIAREN = (EightDiagrams.FENG , EightDiagrams.HUO , "������")
    KUI = (EightDiagrams.HUO , EightDiagrams.ZE , "�����")
    SHUI_SHAN_QIAN = (EightDiagrams.SHUI , EightDiagrams.SHAN , "ˮɽ�")
    JIE = (EightDiagrams.LEI , EightDiagrams.SHUI , "��ˮ��")

    SUN = (EightDiagrams.SHAN , EightDiagrams.ZE , "ɽ����")
    FENG_LEI_YI = (EightDiagrams.FENG , EightDiagrams.LEI , "������")
    JUE = (EightDiagrams.ZE , EightDiagrams.TIAN , "�����")
    GOU = (EightDiagrams.TIAN , EightDiagrams.FENG , "��犥")
    CUI = (EightDiagrams.ZE , EightDiagrams.DI , "�����")
    SHENG = (EightDiagrams.DI , EightDiagrams.FENG , "�ط���")
    ZE_SHUI_KUN = (EightDiagrams.ZE , EightDiagrams.SHUI , "��ˮ��")
    JING = (EightDiagrams.SHUI , EightDiagrams.FENG , "ˮ�羮")

    GE = (EightDiagrams.ZE , EightDiagrams.HUO , "����")
    DING = (EightDiagrams.HUO , EightDiagrams.FENG , "��綦")
    ZHEN = (EightDiagrams.LEI , EightDiagrams.LEI , "��Ϊ��")
    GEN  = (EightDiagrams.SHAN, EightDiagrams.SHAN, "��Ϊɽ")
    JIAN = (EightDiagrams.FENG , EightDiagrams.SHAN , "��ɽ��")
    GUIMEI = (EightDiagrams.LEI , EightDiagrams.ZE , "�������")
    FENG = (EightDiagrams.LEI , EightDiagrams.HUO , "�׻��")
    HUO_SHAN_LV = (EightDiagrams.HUO , EightDiagrams.SHAN , "��ɽ��")

    XUN  = (EightDiagrams.FENG, EightDiagrams.FENG, "��Ϊ��")
    DUI  = (EightDiagrams.ZE  , EightDiagrams.ZE  , "��Ϊ��")
    HUAN = (EightDiagrams.FENG , EightDiagrams.SHUI , "��ˮ��")
    SHUI_ZE_JIE = (EightDiagrams.SHUI , EightDiagrams.ZE , "ˮ���")
    ZHONGFU = (EightDiagrams.FENG , EightDiagrams.ZE , "��������")
    XIAOGUO = (EightDiagrams.LEI , EightDiagrams.SHAN , "��ɽС��")
    JIJI = (EightDiagrams.SHUI , EightDiagrams.HUO , "ˮ��ȼ�")
    WEIJI = (EightDiagrams.HUO , EightDiagrams.SHUI , "��ˮδ��")


if __name__ == '__main__':
    print(type(EightDiagrams.TIAN.value))
    
    
    
    
    
    

