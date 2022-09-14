import folium

# m = folium.Map()

# 高德-卫星影像图
GD_WX = 'https://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}'
GD_WX_Attr = '高德-卫星影像图'

GD_JD = 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=8&ltype=11',
GD_JD_Attr = '高德-街道路网图',

GD_CG = 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7',
GD_CG_Attr = '高德-常规图',

XZBJ = 'http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/administrative_division_boundaryandlabel/MapServer/tile/{z}/{y}/{x}',
XZBJ_Attr = '中国行政区划边界',

# 腾讯地图
TX = 'https://rt0.map.gtimg.com/tile?z={z}&x={x}&y={-y}'
TX_Attr = '腾讯地图' 

# 天地图
TDT = 'http://t7.tianditu.gov.cn/img_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&tk='
TDT_Attr = '天地图-影像'

_tiles = GD_WX
_attr = GD_WX_Attr

m = folium.Map([40.002694, 116.322373],
               tiles=_tiles,
               attr=_attr,
               zoom_start=15,
               control_scale=True
               )
m.save('map.html')
