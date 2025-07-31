from datetime import datetime
from pytz import timezone
from starplot import OpticPlot, DSO, _
from starplot.callables import color_by_bv
from starplot.optics import Refractor,Scope
from starplot.styles import PlotStyle, extensions

dt = datetime.now(timezone("Asia/Shanghai")).replace(2025, 8, 16, 22, 0, 0)

style = PlotStyle().extend(
    extensions.GRAYSCALE_DARK,
    extensions.OPTIC,
)

p = OpticPlot(
    # M45
    ra=59.351417,
    dec=63.070083,
    lat=30.363484,
    lon=117.836394,
    # Telescope
    optic=Scope(
        focal_length=430,
        eyepiece_focal_length=20,
        eyepiece_fov=82,
    ),
    dt=dt,
    style=style,
    resolution=4096,
    autoscale=True,
)
p.stars(
    where=[_.magnitude < 18],
    color_fn=color_by_bv,
)
#p.info()
style.title.font_family = 'Microsoft YaHei'
style.title.font_size = '60'

p.title(
    text="NGC 1502 & Kemble's Cascade(甘伯串珠)"
)
""" #NGC1502
p.marker(
    ra=61.953583,
    dec=62.314528,
    style={
        "marker": {
            "size":120,
            "symbol": "circle",
            "fill": "none",
            "color": "#f2ffc3",
            "edge_color": "#e0c1e0",
            "alpha": 0.4,
        },
        "label": {
            "font_size": 40,
            "font_weight": "bold",
            "font_color": "#FD7E07",
            #"font_alpha": 1,
        },
    },
    label="Mel111",
)


p.text(
    text="NGC1905",
    ra=61.953583,
    dec=62.314528,
    hide_on_collision=False,
    style={
         "text": {
            "font_size": 40,
            "font_weight": "bold",
            "font_color": "#FD7E07",
         }
        },
    ) """

p.export("optic_NGC1502.png", padding=0.1, transparent=True)