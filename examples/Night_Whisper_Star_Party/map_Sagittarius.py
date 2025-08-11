from starplot import MapPlot, Projection, callables, _
from starplot.styles import PlotStyle,LabelStyle, extensions

constellations_cn = {
    "and": "仙女",
    "ant": "唧筒",
    "aps": "天燕",
    "aql": "天鹰",
    "aqr": "宝瓶",
    "ara": "天坛",
    "ari": "白羊",
    "aur": "御夫",
    "boo": "牧夫",
    "cma": "大犬",
    "cmi": "小犬",
    "cvn": "猎犬",
    "cae": "雕具",
    "cam": "鹿豹",
    "cap": "摩羯",
    "car": "船底",
    "cas": "仙后",
    "cen": "半人马",
    "cep": "仙王",
    "cet": "鲸鱼",
    "cha": "蝘蜓",
    "cir": "圆规",
    "cnc": "巨蟹",
    "col": "天鸽",
    "com": "后发",
    "cra": "南冕",
    "crb": "北冕",
    "crt": "巨爵",
    "cru": "南十字",
    "crv": "乌鸦",
    "cyg": "天鹅",
    "del": "海豚",
    "dor": "剑鱼",
    "dra": "天龙",
    "equ": "小马",
    "eri": "波江",
    "for": "炉",
    "gem": "双子",
    "gru": "天鹤",
    "her": "武仙",
    "hor": "时钟",
    "hya": "长蛇",
    "hyi": "水蛇",
    "ind": "印第安",
    "lmi": "小狮",
    "lac": "蝎虎",
    "leo": "狮子",
    "lep": "天兔",
    "lib": "天秤",
    "lup": "豺狼",
    "lyn": "天猫",
    "lyr": "天琴",
    "men": "山案",
    "mic": "显微镜",
    "mon": "麒麟",
    "mus": "苍蝇",
    "nor": "矩尺",
    "oct": "南极",
    "oph": "蛇夫",
    "ori": "猎户",
    "pav": "孔雀",
    "peg": "飞马",
    "per": "英仙",
    "phe": "凤凰",
    "pic": "绘架",
    "psa": "南鱼",
    "psc": "双鱼",
    "pup": "船尾",
    "pyx": "罗盘",
    "ret": "网罟",
    "scl": "玉夫",
    "sco": "天蝎",
    "sct": "盾牌",
    "ser1": "巨蛇座头",
    "ser2": "巨蛇座尾",
    "sex": "六分仪",
    "sge": "天箭",
    "sgr": "人马",
    "tau": "金牛",
    "tel": "望远镜",
    "tra": "南三角",
    "tri": "三角",
    "tuc": "杜鹃",
    "uma": "大熊",
    "umi": "小熊",
    "vel": "船帆",
    "vir": "室女",
    "vol": "飞鱼",
    "vul": "狐狸"
}

label_dict_open_clusters = {
    "NGC0663": "NGC663",
    "NGC0129": "NGC129",
    "NGC0188": "NGC188",
    "NGC0436": "NGC436",
    "NGC0559": "NGC559",
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
    "NGC0457": "NGC457猫头鹰星团",
    "NGC0654": "NGC654谜蝶形团",
    "NGC6910": "NGC6910木马星团",
    "NGC6633": "NGC6633双胞胎星团",
    "NGC0225": "NGC225睡鼠星团",
    "NGC7380": "NGC7380巫师星云",
    "NGC0884": "NGC884英仙双星团",
    "NGC0869": "NGC869英仙座双星团",
    "NGC6823": "NGC6823云雕星团",
    "IC4665": "IC 4665",
    "IC4756": "IC 4756",
    "IC4996": "IC 4996"

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
    "NGC0625":"M10",
    "NGC0670":"M11野鸭星团",
    "NGC0205":"M110",
    "NGC0621":"M12",
    "NGC6205":"M13",
    "NGC6402":"M14",
    "NGC7078":"M15",
    "NGC6611":"M16鹰状星云",
    "NGC6618":"M17天鹅星云",
    "NGC0651":"M18",
    "NGC7089":"M2",
    "NGC6514":"M20三裂星云",
    "NGC6531":"M21",
    "NGC6656":"M22",
    "NGC6494":"M23",
    "NGC6603":"M24",
    "NGC4725":"M25",
    "NGC6853":"M27哑铃星云",
    "NGC6626":"M28",
    "NGC5272":"M3",
    "NGC7099":"M30海蜇星团",
    "NGC0224":"M31仙女座大星云",
    "NGC0598":"M33",
    "NGC1039":"M34螺旋星团",
    "NGC7092":"M39",
    "NGC6121":"M4",
    "NGC5904":"M5玫瑰星团",
    "NGC5194":"M51",
    "NGC7654":"M52蝎状星团",
    "NGC6715":"M54",
    "NGC6779":"M56",
    "NGC6720":"环状星云",
    "NGC6405":"M6蝴蝶星团",
    "NGC6475":"M7托勒密星团",
    "NGC6838":"M71",
    "NGC6981":"M72",
    "NGC6994":"M73",
    "NGC0650":"M76小哑铃星云",
    "NGC6523":"M8礁湖星云",
    "NGC6093":"M80",
    "NGC6341":"M92",
}

lable_dict_nebula={
    "C9":"洞穴星云LBN529",
    "IC1295":"IC1295",
    "IC1318":"IC1318天津一星云",
    "IC1396":"IC1396象鼻星云",
    "IC1805":"IC1805心脏星云",
    "IC1848":"IC1848灵魂星云",
    "IC4593":"IC4593白眼豌豆星云",
    "IC4997":"IC4997",
    "IC5070":"IC5070鹈鹕星云",
    "IC5117":"IC5117",
    "IC5146":"IC5146茧状星云",
    "NGC0147":"NGC147",
    "NGC0185":"NGC185",
    "NGC0040":"NGC40蝴蝶结星云",
    "NGC5005":"NGC5005",
    "NGC5033 ":"NGC5033 ",
    "NGC5906":"NGC5906",
    "NGC6210":"NGC6210海龟星云",
    "NGC6309":"NGC6309方盒星云",
    "NGC6369":"NGC6369小幽灵",
    "NGC6543":"NGC6543猫眼星云",
    "NGC6572":"NGC6572翡翠星云",
    "NGC6741":"NGC6741幻影条纹星云",
    "NGC6751":"NGC6751蒲公英星云",
    "NGC6765":"NGC6765",
    "NGC6781":"NGC6781雪球星云",
    "NGC6804":"NGC6804",
    "NGC6818":"NGC6818小宝石星云",
    "NGC6826":"NGC6826眨眼行星状星云",
    "NGC6842":"NGC6842",
    "NGC6857":"NGC6857",
    "NGC6888":"眉月星云",
    "NGC6891":"NGC6891",
    "NGC6894":"NGC6894小指环星云",
    "NGC6905":"NGC6905蓝闪星云",
    "NGC7000":"NGC7000北美星云",
    "NGC7008":"NGC7008",
    "NGC7009":"NGC7009土星状星云",
    "NGC7026":"NGC7026",
    "NGC7027":"NGC7027珠宝虫星云",
    "NGC7048":"NGC7048",
    "NGC7354":"NGC7354",
    "NGC7635":"NGC7635气泡星云",
    "NGC7662":"NGC7662蓝雪球星云",
    "NGC7814":"NGC7814电弧星系",

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
    84345:"帝",
    80763:"Antares(心宿二)",
    84405:"Guniibuu哈哈",
}

label_dict_galaxies={
    "NGC5545":"Arp199",
    "NGC6045":"Arp71",
    "NGC5394":"苍鹭星系/Arp84",
    "IC0010":"IC0010",
    "IC1101":"IC1101",

}

style = PlotStyle().extend(
    extensions.ANTIQUE,
    #extensions.NORD ,
    extensions.MAP,
)

style.dso_open_cluster.label.font_family = 'Microsoft YaHei'
style.dso_open_cluster.label.font_size = '18'
style.dso_globular_cluster.label.font_family = 'Microsoft YaHei'
style.dso_globular_cluster.label.font_size = '18'
style.dso_nebula.label.font_family = 'Microsoft YaHei'
style.dso_nebula.label.font_size = '18'
style.dso_dark_nebula.label.font_family = 'Microsoft YaHei'
style.dso_dark_nebula.label.font_size = '18'
style.dso_planetary_nebula.label.font_family = 'Microsoft YaHei'
style.dso_planetary_nebula.label.font_size = '18'
style.dso_galaxy.label.font_family = 'Microsoft YaHei'
style.dso_galaxy.label.font_size = '18'
style.dso_hii_ionized_region.label.font_family = 'Microsoft YaHei'
style.dso_hii_ionized_region.label.font_size = '18'
style.ecliptic.label.font_family = 'Microsoft YaHei'
style.ecliptic.label.font_size = '26'
style.celestial_equator.label.font_family = 'Microsoft YaHei'
style.celestial_equator.label.font_size = '26'

p = MapPlot(
    projection=Projection.MILLER,
    ra_min=235, #15.6 * 15,
    ra_max=295, #19.8 * 15,
    dec_min=-45,
    dec_max=25,
    style=style,
    resolution=2000, #10000,
    autoscale=True,
)
p.constellations()
p.constellation_borders()

p.stars(
    where=[_.magnitude <= 2],
    where_labels=[_.magnitude < 0],
    labels=None,
    bayer_labels=False,
    flamsteed_labels=False,
    size_fn=lambda d: callables.size_by_magnitude(d) * 2,  # make them 2x bigger
    # style__marker__symbol="star_8",
    # style__label__offset_x=8,
    # style__label__offset_y=-8,
    # style__label__border_width=2,
    # style__label__border_color="#fefaed",
    # style__label__font_family="microsoft Yahei",
    #label_fn=lambda d: lable_dict_stars.get(d.name)
)
p.stars(
    where=[
        _.magnitude > 2,
        _.magnitude <= 7,
    ],
    where_labels=[_.magnitude < 0],
    labels=None,
    bayer_labels=False,
    flamsteed_labels=False,
    catalog="big-sky-mag11",
    style__label__font_family="microsoft Yahei",
    #label_fn=lambda d: lable_dict_stars.get(d.name)
) 



p.nebula(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 16),_.name.isin(["NGC7009","IC1295","NGC7814","IC4997","NGC6891","NGC6905","NGC5005","NGC6842","NGC5033 ","NGC6818","IC4593","NGC6309","NGC6572","NGC6369","IC5117","NGC6857","NGC7008","NGC7026","NGC7048","NGC7000","IC5146","IC5070","IC1318","NGC6894","NGC6826","NGC6888","NGC7027","NGC5906","NGC6543","NGC6765","NGC6804","NGC6741","NGC6751","NGC6781","NGC6210","NGC0185","NGC0147","IC1848","NGC7635","IC1805","NGC7662","NGC7354","NGC0040","IC1396","C9"])
    ],
    true_size=True,
    label_fn=lambda d: lable_dict_nebula.get(d.name) #or  d.ngc #d.ic,
)

p.messier(where=[(_.magnitude.isnull()) | (_.magnitude < 16),
               _.name.isin(["NGC1039","NGC1068","NGC1904","NGC1912","NGC1952","NGC1960","NGC1976","NGC1982","NGC0205","NGC2068","NGC2099","NGC2168","NGC0221","NGC0224","NGC2287","NGC2323","NGC2422","NGC2437","NGC2447","NGC2548","NGC2632","NGC2682","NGC3031","NGC3034","NGC3351","NGC3368","NGC3379","NGC3556","NGC3587","NGC3623","NGC3627","NGC3992","NGC4192","NGC4254","NGC4258","NGC4303","NGC4321","NGC4374","NGC4382","NGC4406","NGC4472","NGC4486","NGC4501","NGC4548","NGC4552","NGC4569","NGC4579","NGC4590","NGC4594","NGC4621","NGC4649","NGC4736","NGC4826","NGC5024","NGC5055","NGC5194","NGC5236","NGC5272","NGC5457","NGC0581","NGC5866","NGC5904","NGC0598","NGC6093","NGC6121","NGC6171","NGC6205","NGC6218","NGC6254","NGC6266","NGC6273","NGC0628","NGC6333","NGC6341","NGC6402","NGC6405","NGC6475","NGC6494","NGC0650","NGC6514","NGC6523","NGC6531","NGC6611","NGC6613","NGC6618","NGC6626","NGC6637","NGC6656","NGC6681","NGC6694","NGC6705","NGC6715","NGC6720","NGC6779","NGC6809","NGC6838","NGC6853","NGC6864","NGC6913","NGC6981","NGC6994","NGC7078","NGC7089","NGC7092","NGC7099","NGC7654"])
                  ],
           true_size=False, 
           #label_fn=lambda d: f"M{d.m}"
           label_fn = lambda d: label_dict_messier.get(d.name) # or f"M{d.m}"
        )

p.open_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 16),_.name.isin(["NGC6649","NGC6664","NGC6823","NGC6882","NGC6885","NGC6940","NGC1502","NGC6645","NGC6633","NGC6802","NGC6811","NGC6819","NGC6866","NGC6871","NGC6910","NGC7044","NGC7062","NGC7128","NGC6791","NGC6709","NGC6755","NGC0129","NGC0225","NGC0436","NGC0457","NGC0559","NGC0654","NGC0663","NGC7789","NGC7790","NGC7686","NGC0188","NGC6939","NGC7160","NGC7380","NGC7429","NGC7510","NGC7209","NGC7243","NGC7296","NGC0869","NGC0884"])
        ],
    true_size=False,
    label_fn = lambda d: label_dict_open_clusters.get(d.name) #or d.ngc
)
p.globular_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 13),_.name.isin(["NGC5053","NGC5466","NGC6144","NGC6229","NGC6235","NGC6356","NGC6366","NGC6441","NGC6535","NGC6539","NGC6569","NGC6712","NGC6749","NGC6760","NGC6934","NGC7006"])
    ],
    true_size=False,
    label_fn = lambda d: label_dict_globular_clusters.get(d.name)
)

p.galaxies(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 13),_.name.isin(["NGC5053","NGC5466","NGC6144","NGC6229","NGC6235","NGC6356","NGC6366","NGC6441","NGC6535","NGC6539","NGC6569","NGC6712","NGC6749","NGC6760","NGC6934","NGC7006"])
    ],
    true_size=False,
    label_fn = lambda d: label_dict_galaxies.get(d.name)
)

style2 = LabelStyle(
    font_color="orange",        # 字体颜色
    font_size=16, #12               # 字号
    font_name="Microsoft Yahei",
)
############衣架星群-开始############
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
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="衣架星群/Cr 399",
)

p.text(
    text="衣架星群/Cr 399",

    ra=291.35,
    dec=21.986,
        style=style2,
    hide_on_collision=False,
    )
############衣架星群-结束############


############B142-巴纳德的E星云-开始############
p.marker(
    ra=294.9244,
    dec=10.5225,
    style={
        "marker": {
            "size":20,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="22衣架星群/Cr 399",
)

p.text(
    text="E星云/B142",

    ra=294.9244,
    dec=10.5225,
        style=style2,
    hide_on_collision=False,
    )
############B142-巴纳德的E星云-结束############

############Berkeley 82-开始############
p.marker(
    ra=287.8463,
    dec=13.1137,
    style={
        "marker": {
            "size":5,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
            "font_size": 12,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Berkeley 82",
)

p.text(
    text="Berkeley 82",

    ra=287.8463,
    dec=13.1137,
        style=style2,
    hide_on_collision=False,
    )
############Berkeley 82-结束############

############Berkeley 87-开始############
p.marker(
    ra=305.4019,
    dec=37.5046,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
            "font_size": 12,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Berkeley 87",
)

p.text(
    text="Berkeley 87",

    ra=305.4019,
    dec=37.5046,
        style=style2,
    hide_on_collision=False,
    )
############Berkeley 87-结束############


############Cr 338-开始############
p.marker(
    ra=264.5278,
    dec=-37.7214,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Berkeley 82",
)

p.text(
    text="Cr 338",

    ra=264.5278,
    dec=-37.7214,
        style=style2,
    hide_on_collision=False,
    )
############Cr 338-结束############


###########Sh2-101郁金香星云-开始############
p.marker(
    ra=299.9846,
    dec=35.2801,
    style={
        "marker": {
            "size":20,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Sh2-101郁金香星云",
)

p.text(
    text="Sh2-101郁金香星云",

    ra=299.9846,
    dec=35.2801,
        style=style2,
    hide_on_collision=False,
    )
############Sh2-101郁金香星云-结束############


###########Trumpler 2-开始############
p.marker(
    ra=39.3281,
    dec=55.9803,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Trumpler 2",
)

p.text(
    text="Trumpler 2",

    ra=39.3281,
    dec=55.9803,
        style=style2,
    hide_on_collision=False,
    )
############Trumpler 2-结束############

###########Trumpler 27-开始############
p.marker(
    ra=264.0526,
    dec=-33.4843,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Trumpler 27",
)

p.text(
    text="Trumpler 27",

    ra=264.0526,
    dec=-33.4843,
        style=style2,
    hide_on_collision=False,
    )
############Trumpler 27-结束############



###########Stock 23-开始############
p.marker(
    ra=49.0478,
    dec=60.1115,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Stock 23",
)

p.text(
    text="Stock 23",
    ra=49.0478,
    dec=60.1115,
        style=style2,
    hide_on_collision=False,
    )
############Stock 23-结束############


###########King 12-开始############
p.marker(
    ra=358.2697,
    dec=61.9501,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="King 12",
)

p.text(
    text="King 12",
    ra=358.2697,
    dec=61.9501,
        style=style2,
    hide_on_collision=False,
    )
############King 12-结束############


###########Palomar6-开始############
p.marker(
    ra=265.9285,
    dec=-26.2228,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Palomar6",
)

p.text(
    text="Palomar6",
    ra=265.9285,
    dec=-26.2228,
        style=style2,
    hide_on_collision=False,
    )
############Palomar6-结束############


###########Palomar12-开始############
p.marker(
    ra=326.6674,
    dec=-21.2509,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Palomar12",
)

p.text(
    text="Palomar12",
    ra=326.6674,
    dec=-21.2509,
        style=style2,
    hide_on_collision=False,
    )
############Palomar12-结束############


###########Palomar5-开始############
p.marker(
    ra=229.0211,
    dec=-0.1094,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Palomar5",
)

p.text(
    text="Palomar5",
    ra=229.0211,
    dec=-0.1094,
        style=style2,
    hide_on_collision=False,
    )
############Palomar5-结束############


###########Terzan3-开始############
p.marker(
    ra=247.1680,
    dec=-35.3550,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Terzan3",
)

p.text(
    text="Terzan3",
    ra=247.1680,
    dec=-35.3550,
        style=style2,
    hide_on_collision=False,
    )
############Terzan3-结束############

###########Terzan9-开始############
p.marker(
    ra=270.4147,
    dec=-26.84,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Terzan9",
)

p.text(
    text="Terzan9",
    ra=270.4147,
    dec=-26.84,
        style=style2,
    hide_on_collision=False,
    )
############Terzan9-结束############

###########Palomar14-开始############
p.marker(
    ra=242.7494,
    dec=14.9706,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Palomar14",
)

p.text(
    text="Palomar14",
    ra=242.7494,
    dec=14.9706,
        style=style2,
    hide_on_collision=False,
    )
############Palomar14-结束############


###########Palomar15-开始############
p.marker(
    ra=254.9643,
    dec=-0.5314,
    style={
        "marker": {
            "size":10,
            "symbol": "circle",
            "fill": "full",
            "color": "#ed7eed",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
                "font_size": 14,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Palomar15",
)

p.text(
    text="Palomar15",
    ra=254.9643,
    dec=-0.5314,
        style=style2,
    hide_on_collision=False,
    )
############Palomar15-结束############

p.ecliptic(label='夜语星趴 Night Whisper Star Party')
p.celestial_equator(label='星趴 Night Whisper Star Party')
p.milky_way()
p.constellation_labels(style__font_size=80,style__font_name="microsoft Yahei",labels=constellations_cn)
p.export("map_Sagittarius.png", padding=0.08)