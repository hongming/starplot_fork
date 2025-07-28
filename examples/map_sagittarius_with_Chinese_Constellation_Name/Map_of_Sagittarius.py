from starplot import MapPlot, Projection, callables, _
from starplot.styles import PlotStyle, extensions

constellations_cn = {
    "and": "仙女座",
    "ant": "唧筒座",
    "aps": "天燕座",
    "aql": "天鹰座",
    "aqr": "宝瓶座",
    "ara": "天坛座",
    "ari": "白羊座",
    "aur": "御夫座",
    "boo": "牧夫座",
    "cma": "大犬座",
    "cmi": "小犬座",
    "cvn": "猎犬座",
    "cae": "雕具座",
    "cam": "鹿豹座",
    "cap": "摩羯座",
    "car": "船底座",
    "cas": "仙后座",
    "cen": "半人马座",
    "cep": "仙王座",
    "cet": "鲸鱼座",
    "cha": "蝘蜓座",
    "cir": "圆规座",
    "cnc": "巨蟹座",
    "col": "天鸽座",
    "com": "后发座",
    "cra": "南冕座",
    "crb": "北冕座",
    "crt": "巨爵座",
    "cru": "南十字座",
    "crv": "乌鸦座",
    "cyg": "天鹅座",
    "del": "海豚座",
    "dor": "剑鱼座",
    "dra": "天龙座",
    "equ": "小马座",
    "eri": "波江座",
    "for": "炉座",
    "gem": "双子座",
    "gru": "天鹤座",
    "her": "武仙座",
    "hor": "时钟座",
    "hya": "长蛇座",
    "hyi": "水蛇座",
    "ind": "印第安座",
    "lmi": "小狮座",
    "lac": "壁蛇座",
    "leo": "狮子座",
    "lep": "天兔座",
    "lib": "天秤座",
    "lup": "豺狼座",
    "lyn": "天猫座",
    "lyr": "天琴座",
    "men": "山案座",
    "mic": "显微镜座",
    "mon": "麒麟座",
    "mus": "苍蝇座",
    "nor": "矩尺座",
    "oct": "南极座",
    "oph": "蛇夫座",
    "ori": "猎户座",
    "pav": "孔雀座",
    "peg": "飞马座",
    "per": "英仙座",
    "phe": "凤凰座",
    "pic": "绘架座",
    "psa": "南鱼座",
    "psc": "双鱼座",
    "pup": "船尾座",
    "pyx": "罗盘座",
    "ret": "网罟座",
    "scl": "玉夫座",
    "sco": "天蝎座",
    "sct": "盾牌座",
    "ser1": "巨蛇座头",
    "ser2": "巨蛇座尾",
    "sex": "六分仪座",
    "sge": "箭座",
    "sgr": "人马座",
    "tau": "金牛座",
    "tel": "望远镜座",
    "tra": "南三角座",
    "tri": "三角座",
    "tuc": "杜鹃座",
    "uma": "大熊座",
    "umi": "小熊座",
    "vel": "船帆座",
    "vir": "室女座",
    "vol": "飞鱼座",
    "vul": "小狐座"
}

style = PlotStyle().extend(
    extensions.ANTIQUE,
    extensions.MAP,
)
p = MapPlot(
    projection=Projection.MILLER,
    ra_min=15.6 * 15,
    ra_max=19.8 * 15,
    dec_min=-45.2,
    dec_max=-3,
    style=style,
    resolution=4000,
    autoscale=True,
)
p.constellations()
p.constellation_borders()

p.stars(
    where=[_.magnitude <= 3],
    size_fn=lambda d: callables.size_by_magnitude(d) * 2,  # make them 2x bigger
    style__marker__symbol="star_8",
    style__label__offset_x=8,
    style__label__offset_y=-8,
    style__label__border_width=2,
    style__label__border_color="#fefaed",
)
p.stars(
    where=[
        _.magnitude > 3,
        _.magnitude < 9,
    ],
    bayer_labels=True,
    flamsteed_labels=True,
    catalog="big-sky-mag11",
)

p.nebula(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 12),
    ],
    true_size=True,
    label_fn=lambda d: d.ic,
)
p.open_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 12),
    ],
    true_size=False,
    label_fn=lambda d: d.ngc,
)
p.globular_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 12),
    ],
    true_size=False,
    label_fn=lambda d: d.ngc,
)
p.ecliptic()
p.celestial_equator()
p.milky_way()
p.constellation_labels(style__font_size=80,style__font_name="microsoft Yahei",labels=constellations_cn)
p.export("map_sagittarius.png", padding=0.08)