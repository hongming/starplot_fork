from starplot import MapPlot, Projection, callables, _
from starplot.styles import PlotStyle, extensions

#新增，自定义中文名，对应规则在i18n的ZH_CN中，注意NGC、M等深空天体从https://starplot.dev/data/dsos/查询编号，恒星需要从https://starplot.dev/data/star-designations/查询HIP编号
from i18n.ZH_CN import constellations_cn,label_dict_open_clusters,label_dict_globular_clusters,label_dict_messier,label_dict_nebula,label_dict_galaxies,label_dict_stars


style = PlotStyle().extend(
    #不使用内置样式，而是使用下方定制的话的样式，包含中文字体微软雅黑“Microsoft yahei”
    #extensions.ANTIQUE,
    extensions.MAP,
)

#新增，自定义样式（字号大小、背景色、文字颜色、字体等，以extensions.ANTIQUE为基础
style = PlotStyle.load_from_file("Local_styles/style_extend_antique.yml")

p = MapPlot(
    projection=Projection.MILLER,
    #以下定义显示区域
    ra_min=15.6 * 15, #RA坐标最小值，十进制
    ra_max=19.8 * 15, #RA坐标最大值，十进制
    dec_min=-45.2, #DEC坐标最小值，十进制
    dec_max=-3, #DEC坐标最大值，十进制
    style=style,
    resolution=4000, #星趴A1打印版使用了10000像素
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
    labels=label_dict_stars, #为特定恒星增加中文名称
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

# 显示星云
""" p.nebula(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 12),
    ],
    true_size=True,
    label_fn=lambda d: d.ic,
) """

# 显示星云，修改，_.name.isin只显示这些星云，避免其他目标干扰
p.nebula(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 16),_.name.isin(["NGC7009","IC1295","NGC7814","IC4997","NGC6891","NGC6905","NGC5005","NGC6842","NGC5033 ","NGC6818","IC4593","NGC6309","NGC6572","NGC6369","IC5117","NGC6857","NGC7008","NGC7026","NGC7048","NGC7000","IC5146","IC5070","IC1318","NGC6894","NGC6826","NGC6888","NGC7027","NGC5906","NGC6543","NGC6765","NGC6804","NGC6741","NGC6751","NGC6781","NGC6210","NGC0185","NGC0147","IC1848","NGC7635","IC1805","NGC7662","NGC7354","NGC0040","IC1396","C9"])
    ],
    true_size=True,
    label_fn=lambda d: label_dict_nebula.get(d.name) #or  d.ngc #d.ic,
)

# 显示疏散星团
""" p.open_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 12),
    ],
    true_size=False,
    label_fn=lambda d: d.ngc,
) """

# 显示疏散星团，修改，只显示特定星团，且通过label_fn控制显示对应的中文名
p.open_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 16),_.name.isin(["NGC6649","NGC6664","NGC6823","NGC6882","NGC6885","NGC6940","NGC1502","NGC6645","NGC6633","NGC6802","NGC6811","NGC6819","NGC6866","NGC6871","NGC6910","NGC7044","NGC7062","NGC7128","NGC6791","NGC6709","NGC6755","NGC0129","NGC0225","NGC0436","NGC0457","NGC0559","NGC0654","NGC0663","NGC7789","NGC7790","NGC7686","NGC0188","NGC6939","NGC7160","NGC7380","NGC7429","NGC7510","NGC7209","NGC7243","NGC7296","NGC0869","NGC0884"])
        ],
    true_size=False,
    label_fn = lambda d: label_dict_open_clusters.get(d.name) #or d.ngc
)

# 显示球状星团，这时只显示编号，比如NGC5053，显示为5053
""" p.globular_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 12),
    ],
    true_size=False,
    label_fn=lambda d: d.ngc,
) """

p.globular_clusters(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 12),
    ],
    true_size=False,
    #label_fn=lambda d: d.ngc, #只显示编号
    label_fn=lambda d: f"NGC{d.ngc}" #带上NGC编号
)

# 显示星系
p.galaxies(
    where=[
        (_.magnitude.isnull()) | (_.magnitude < 13),_.name.isin(["NGC5053","NGC5466","NGC6144","NGC6229","NGC6235","NGC6356","NGC6366","NGC6441","NGC6535","NGC6539","NGC6569","NGC6712","NGC6749","NGC6760","NGC6934","NGC7006"])
    ],
    true_size=False,
    label_fn = lambda d: label_dict_galaxies.get(d.name)
)

# 显示梅西耶天体（部分），且使用中文名
p.messier(where=[(_.magnitude.isnull()) | (_.magnitude < 16),
               _.name.isin(["NGC1039","NGC1068","NGC1904","NGC1912","NGC1952","NGC1960","NGC1976","NGC1982","NGC0205","NGC2068","NGC2099","NGC2168","NGC0221","NGC0224","NGC2287","NGC2323","NGC2422","NGC2437","NGC2447","NGC2548","NGC2632","NGC2682","NGC3031","NGC3034","NGC3351","NGC3368","NGC3379","NGC3556","NGC3587","NGC3623","NGC3627","NGC3992","NGC4192","NGC4254","NGC4258","NGC4303","NGC4321","NGC4374","NGC4382","NGC4406","NGC4472","NGC4486","NGC4501","NGC4548","NGC4552","NGC4569","NGC4579","NGC4590","NGC4594","NGC4621","NGC4649","NGC4736","NGC4826","NGC5024","NGC5055","NGC5194","NGC5236","NGC5272","NGC5457","NGC0581","NGC5866","NGC5904","NGC0598","NGC6093","NGC6121","NGC6171","NGC6205","NGC6218","NGC6254","NGC6266","NGC6273","NGC0628","NGC6333","NGC6341","NGC6402","NGC6405","NGC6475","NGC6494","NGC0650","NGC6514","NGC6523","NGC6531","NGC6611","NGC6613","NGC6618","NGC6626","NGC6637","NGC6656","NGC6681","NGC6694","NGC6705","NGC6715","NGC6720","NGC6779","NGC6809","NGC6838","NGC6853","NGC6864","NGC6913","NGC6981","NGC6994","NGC7078","NGC7089","NGC7092","NGC7099","NGC7654"])
                  ],
           true_size=False, 
           #label_fn=lambda d: f"M{d.m}"
           label_fn = lambda d: label_dict_messier.get(d.name) # or f"M{d.m}"
        )

p.ecliptic()
p.celestial_equator()
p.milky_way()
p.constellation_labels(labels=constellations_cn) #显示星座的名称
p.export("map_sagittarius.png", padding=0.08)
