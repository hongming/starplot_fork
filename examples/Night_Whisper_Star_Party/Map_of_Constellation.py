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
    "lac": "蝎虎座",
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
    "sge": "天箭座",
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

label_dict_open_clusters = {
    "NGC663": "NGC663",
    "NGC129": "NGC129",
    "NGC188": "NGC188",
    "NGC436": "NGC436",
    "NGC559": "NGC559",
    "NGC6645": "NGC6645",
    "NGC6649": "NGC6649",
    "NGC6709": "NGC6709",
    "NGC6755": "NGC6755",
    "NGC6791": "NGC6791",
    "NGC6802": "NGC6802",
    "NGC6871": "NGC6871",
    "NGC6882": "NGC6882",
    "NGC6885": "NGC6885",
    "NGC6940": "NGC6940",
    "NGC7044": "NGC7044",
    "NGC7062": "NGC7062",
    "NGC7128": "NGC7128",
    "NGC7160": "NGC7160",
    "NGC7209": "NGC7209",
    "NGC7243": "NGC7243",
    "NGC7296": "NGC7296",
    "NGC7429": "NGC7429",
    "NGC7510": "NGC7510",
    "NGC7686": "NGC7686",
    "NGC7790": "NGC7790",
    "NGC6664": "NGC6664茶杯星团",
    "NGC6811": "NGC6811洞穴星团",
    "NGC6939": "NGC6939飞雁星团",
    "NGC6866": "NGC6866风筝星团",
    "NGC1502": "NGC1502海盗旗星团",
    "NGC6819": "NGC6819狐头星团",
    "NGC7789": "NGC7789卡罗琳玫瑰星团",
    "NGC457": "NGC457猫头鹰星团",
    "NGC654": "NGC654谜蝶形团",
    "NGC6910": "NGC6910木马星团",
    "NGC6633": "NGC6633双胞胎星团 / Cr 380",
    "NGC225": "NGC225睡鼠星团",
    "NGC7380": "NGC7380巫师星云",
    "NGC884": "NGC884英仙双星团",
    "NGC869": "NGC869英仙座双星团",
    "NGC6823": "NGC6823云雕星团",
}

label_dict_globular_clusters = {
    "NGC5053":"NGC5053",
    "NGC5466":"NGC5466",
    "NGC6144":"NGC6144",
    "NGC6229":"NGC6229",
    "NGC6235":"NGC6235",
    "NGC6356":"NGC6356",
    "NGC6366":"NGC6366",
    "NGC6441":"NGC6441",
    "NGC6535":"NGC6535",
    "NGC6539":"NGC6539",
    "NGC6569":"NGC6569",
    "NGC6712":"NGC6712",
    "NGC6749":"NGC6749",
    "NGC6760":"NGC6760",
    "NGC6934":"NGC6934",
    "NGC7006":"NGC7006",
  }  

label_dict_messier={
    "NGC7078":"M15飞马座大星团",
    "NGC7099":"M30海蜇星团",
    "NGC6405":"M6蝴蝶星团",
    "NGC6838":"M71箭矢星团",
    "NGC6523":"M8礁湖星云",
    "NGC6611":"M16老鹰星云",
    "NGC1039":"M34螺旋星团",
    "NGC5904":"M5玫瑰星团",
    "NGC6656":"M22人马座大星团",
    "NGC598":"M33三角座星系",
    "NGC6514":"M20三裂星云",
    "NGC6618":"M17天鹅星云",
    "NGC6475":"M7托勒密星团",
    "NGC5194":"M51涡状星系",
    "NGC6205":"M13武仙大球状星团",
    "NGC224":"M31仙女座星系",
    "NGC650":"M76小哑铃星云",
    "NGC7654":"M52蝎状星团",
    "NGC6853":"M27哑铃星云",
    "NGC6705":"M11野鸭星团",
}

lable_dict_nebula={
    "NGC6720":"M57环状星云",
    "NGC7009":"NGC7009土星状星云",
    "IC1295":"IC1295",
    "NGC7814":"NGC7814电弧星系",
    "IC4997":"IC4997",
    "NGC6891":"NGC6891",
    "NGC6905":"NGC6905蓝闪星云",
    "NGC5005":"NGC5005",
    "NGC6842":"NGC6842",
    "NGC5033 ":"NGC5033 ",
    "NGC6818":"NGC6818小宝石星云",
    "IC4593":"IC4593白眼豌豆星云",
    "NGC6309":"NGC6309方盒星云",
    "NGC6369":"NGC6369小幽灵",
    "NGC6572":"NGC6572翡翠星云",
    "IC5117":"IC5117",
    "NGC6857":"NGC6857",
    "NGC7008":"NGC7008",
    "NGC7026":"NGC7026",
    "NGC7048":"NGC7048",
    "NGC7000":"NGC7000北美星云",
    "IC5146":"IC5146茧状星云",
    "NGC6888":"NGC6888眉月星云",
    "IC5070":"IC5070鹈鹕星云",
    "IC1318":"IC1318天津一星云",
    "NGC6894":"NGC6894小指环星云",
    "NGC6826":"NGC6826眨眼行星状星云",
    "NGC7027":"NGC7027珠宝虫星云",
    "NGC5906":"NGC5906",
    "NGC6543":"NGC6543猫眼星云",
    "NGC6765":"NGC6765",
    "NGC6804":"NGC6804",
    "NGC6741":"NGC6741幻影条纹星云",
    "NGC6751":"NGC6751蒲公英星云",
    "NGC6781":"NGC6781雪球星云",
    "NGC6210":"NGC6210海龟星云",
    "NGC185":"NGC185",
    "NGC147":"NGC147",
    "IC1848":"IC1848灵魂星云",
    "NGC7635":"NGC7635气泡星云",
    "IC1805":"IC1805心脏星云",
    "NGC7662":"NGC7662蓝雪球星云",
    "NGC7354":"NGC7354",
    "NGC40":"NGC40蝴蝶结星云",
    "IC1396":"IC1396象鼻星云",
}

lable_dict_stars={
    88818:"100 Her",
    79607:"17 Crb",
    99675:"31 Cyg",
    72524:"39 Boo",
    91971:"4 Lyr(织女二)",
    104214:"61 Cyg",
    86831:"61 Oph",
    78820:"Acrab(房宿四)",
    95947:"Albireo(辇道增七)",
    75411:"Alkalurops",
    92946:"Alya(徐)",
    83608:"Arrakis(天棓增九)",
    63125:"常陈一",
    86614:"Dziban(女史增一)",
    96688:"H N 84",
    72105:"Izar",
    79043:"Marsic(晋)",
    94075:"Struve2474/70",
    99:"WZ Cas",
    78727:"Grassias(西咸一)",
    97496:"Zeta Sge",
    72622:"氐宿一",
    84345:"帝座",
    80763:"Antares(心宿二)",
    84405:"Guniibuu哈哈",
}


style = PlotStyle().extend(
    extensions.ANTIQUE,
    #extensions.NORD ,
    extensions.MAP,
)

style.dso_open_cluster.label.font_family = 'Microsoft YaHei'
style.dso_open_cluster.label.font_size = '24'
style.dso_globular_cluster.label.font_family = 'Microsoft YaHei'
style.dso_globular_cluster.label.font_size = '24'
style.dso_nebula.label.font_family = 'Microsoft YaHei'
style.dso_nebula.label.font_size = '24'
style.dso_dark_nebula.label.font_family = 'Microsoft YaHei'
style.dso_dark_nebula.label.font_size = '24'
style.dso_planetary_nebula.label.font_family = 'Microsoft YaHei'
style.dso_planetary_nebula.label.font_size = '20'
style.dso_galaxy.label.font_family = 'Microsoft YaHei'
style.dso_galaxy.label.font_size = '24'
style.ecliptic.label.font_family = 'Microsoft YaHei'
style.ecliptic.label.font_size = '26'
style.celestial_equator.label.font_family = 'Microsoft YaHei'
style.celestial_equator.label.font_size = '26'

p = MapPlot(
    projection=Projection.MILLER,
    ra_min=-30,
    ra_max=30,
    dec_min=30,
    dec_max=70,
    style=style,
    resolution=4000,
    autoscale=True,
)
p.constellations()
p.constellation_borders()

p.stars(
    where=[_.magnitude <= 3],
    labels=None,
    size_fn=lambda d: callables.size_by_magnitude(d) * 2,  # make them 2x bigger
    style__marker__symbol="star_8",
    style__label__offset_x=8,
    style__label__offset_y=-8,
    style__label__border_width=2,
    style__label__border_color="#fefaed",
    style__label__font_family="microsoft Yahei",
    label_fn=lambda d: lable_dict_stars.get(d.name)
)
p.stars(
    where=[
        _.magnitude > 3,
        _.magnitude < 5,
    ],
    bayer_labels=True,
    flamsteed_labels=True,
    catalog="big-sky-mag11",
    style__label__font_family="microsoft Yahei",
    label_fn=lambda d: lable_dict_stars.get(d.name)
)



p.nebula(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 16),_.name.isin(["NGC6720","NGC7009","IC1295","NGC7814","IC4997","NGC6891","NGC6905","NGC5005","NGC6842","NGC5033 ","NGC6818","IC4593","NGC6309","NGC6572","NGC6369","IC5117","NGC6857","NGC7008","NGC7026","NGC7048","NGC7000","IC5146","NGC6888","IC5070","IC1318","NGC6894","NGC6826","NGC7027","NGC5906","NGC6543","NGC6765","NGC6804","NGC6741","NGC6751","NGC6781","NGC6210","NGC185","NGC147","IC1848","NGC7635","IC1805","NGC7662","NGC7354","NGC40","IC1396"])
    ],
    true_size=False,
    label_fn=lambda d: lable_dict_nebula.get(d.name) #or  d.ngc #d.ic,
)

p.messier(where=[_.magnitude < 11], true_size=False, label_fn=lambda d: f"M{d.m}")

""" p.messier(where=[_.magnitude < 16,
               _.name.isin(["NGC1039","NGC1068","NGC1904","NGC1912","NGC1952","NGC1960","NGC1976","NGC1982","NGC205","NGC2068","NGC2099","NGC2168","NGC221","NGC224","NGC2287","NGC2323","NGC2422","NGC2437","NGC2447","NGC2548","NGC2632","NGC2682","NGC3031","NGC3034","NGC3351","NGC3368","NGC3379","NGC3556","NGC3587","NGC3623","NGC3627","NGC3992","NGC4192","NGC4254","NGC4258","NGC4303","NGC4321","NGC4374","NGC4382","NGC4406","NGC4472","NGC4486","NGC4501","NGC4548","NGC4552","NGC4569","NGC4579","NGC4590","NGC4594","NGC4621","NGC4649","NGC4736","NGC4826","NGC5024","NGC5055","NGC5194","NGC5236","NGC5272","NGC5457","NGC581","NGC5866","NGC5904","NGC598","NGC6093","NGC6121","NGC6171","NGC6205","NGC6218","NGC6254","NGC6266","NGC6273","NGC628","NGC6333","NGC6341","NGC6402","NGC6405","NGC6475","NGC6494","NGC650","NGC6514","NGC6523","NGC6531","NGC6611","NGC6613","NGC6618","NGC6626","NGC6637","NGC6656","NGC6681","NGC6694","NGC6705","NGC6715","NGC6720","NGC6779","NGC6809","NGC6838","NGC6853","NGC6864","NGC6913","NGC6981","NGC6994","NGC7078","NGC7089","NGC7092","NGC7099","NGC7654"])
                  ],
           true_size=False, 
           #label_fn=lambda d: f"M{d.m}"
           label_fn = lambda d: label_dict_messier.get(d.name) # or f"M{d.m}"
        ) """

p.open_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 10),_.name.isin(["NGC6649","NGC6664","NGC6823","NGC6882","NGC6885","NGC6940","NGC1502","NGC6645","NGC6633","NGC6802","NGC6811","NGC6819","NGC6866","NGC6871","NGC6910","NGC7044","NGC7062","NGC7128","NGC6791","NGC6709","NGC6755","NGC129","NGC225","NGC436","NGC457","NGC559","NGC654","NGC663","NGC7789","NGC7790","NGC7686","NGC188","NGC6939","NGC7160","NGC7380","NGC7429","NGC7510","NGC7209","NGC7243","NGC7296","NGC869","NGC884"])
        ],
    true_size=False,
    #label_fn=lambda d: d.ngc,
    label_fn = lambda d: label_dict_open_clusters.get(d.name) #or d.ngc
)
p.globular_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 13),_.name.isin(["NGC5053","NGC5466","NGC6144","NGC6229","NGC6235","NGC6356","NGC6366","NGC6441","NGC6535","NGC6539","NGC6569","NGC6712","NGC6749","NGC6760","NGC6934","NGC7006"])
    ],
    true_size=False,
    #label_fn=lambda d: d.ngc,
    label_fn = lambda d: label_dict_globular_clusters.get(d.name)
)



#衣架星群
p.marker(
    ra=291.35,
    dec=20.186,
    style={
        "marker": {
            "size":50,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
            "font_size": 40,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Mel111",
)
p.text(
    text="Cr 399",

    ra=291.35,
    dec=21.986,
    hide_on_collision=False,
    )

p.ecliptic(label='夜语星趴@红柯窑')
p.celestial_equator(label='夜语星趴@红柯窑')
p.milky_way()
p.constellation_labels(style__font_size=80,style__font_name="microsoft Yahei",labels=constellations_cn)
p.export("map_M31.png", padding=0.08)