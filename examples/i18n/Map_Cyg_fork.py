from starplot import MapPlot, Projection, callables, _
from starplot.styles import PlotStyle,LabelStyle, extensions

#自定义中文名
from i18n.ZH_CN import constellations_cn,label_dict_open_clusters,label_dict_globular_clusters,label_dict_messier,label_dict_nebula,label_dict_galaxies,label_dict_stars


style = PlotStyle().extend(
    extensions.MAP,
)

#自定义样式和字体等，以extensions.ANTIQUE为基础
style = PlotStyle.load_from_file("Local_styles/style_extend_blue_light.yml")


p = MapPlot(
    projection=Projection.MILLER,
    ra_min=270,
    ra_max=330,
    dec_min=-10,
    dec_max=60,
    style=style,
    resolution=2000, #打印版10000,
    autoscale=True,
)
p.constellations()
p.constellation_borders()

p.stars(
    where=[_.magnitude <= 2],
    where_labels=[_.magnitude < 0],
    labels=True,
    bayer_labels=False,
    flamsteed_labels=False,
    size_fn=lambda d: callables.size_by_magnitude(d) * 2,  # make them 2x bigger
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
    label_fn=lambda d: label_dict_nebula.get(d.name) #or  d.ngc #d.ic,
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
    font_size=16,               # 字号
    font_name="Microsoft Yahei",# 字体
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
                "font_size": 10,
            "font_weight": "bold",
            "font_color": "#000000",
            #"font_alpha": 1,
        },
    },
    label="Berkeley 82",
)

p.text(
    text="  Cr 338",

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
p.celestial_equator(label='夜语星趴 Night Whisper Star Party')
p.milky_way()
p.constellation_labels(labels=constellations_cn)
p.export("map_Cyg_fork.png", padding=0.08)