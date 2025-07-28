## Updates：
1、替换中文星座名称，例子位置：examples\map_sagittarius_with_Chinese_Constellation_Name/map_sagittarius.py
<img src="examples\map_sagittarius_with_Chinese_Constellation_Name/map_sagittarius.png">


# <img src="https://raw.githubusercontent.com/steveberardi/starplot/main/docs/images/favicon.svg" width="48" style="vertical-align:middle"> Starplot
![Python](https://img.shields.io/pypi/pyversions/starplot?style=for-the-badge&color=6388b0)
![PyPI](https://img.shields.io/pypi/v/starplot?style=for-the-badge&color=57a8a8)
![License](https://img.shields.io/github/license/steveberardi/starplot?style=for-the-badge&color=8b63b0)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/steveberardi/starplot/test.yml?style=for-the-badge&color=88b063)

**Starplot** is a Python library for creating star charts and maps of the sky.

- ⭐ **Zenith Plots** - shows the entire sky at a specific time and place
- 🗺️ **Map Plots** - including many map projections
- 🌃 **Horizon Plots** - shows the horizon at a specific time and place
- 🔭 **Optic Plots** - shows what you'll see through an optic (e.g. telescope) at a specific time and place
- 🪐 **Planets and Deep Sky Objects (DSOs)** - more than 14,000 objects built-in
- 🎨 **Custom Styles** - for all objects
- 📥 **Export** - png, svg, jpeg
- 🚀 **Data Backend** - powered by DuckDB + Ibis for fast object lookup
- 🧭 **Label Collision Avoidance**

## Examples
*Zenith plot of the stars from a specific time/location:*
![starchart-blue](https://starplot.dev/images/examples/star_chart_basic.png)

*Map around the constellation Orion:*
![map-orion](https://starplot.dev/images/examples/map_orion.png)

*The Pleiades star cluster, as seen through a refractor telescope from a specific time and location:*
![optic-pleiades](https://starplot.dev/images/examples/optic_m45.png)

## Basic Usage

To create a star chart for tonight's sky as seen from [Palomar Mountain](https://en.wikipedia.org/wiki/Palomar_Mountain) in California:

```python
from datetime import datetime
from pytz import timezone
import starplot as sp

tz = timezone("America/Los_Angeles")

p = sp.MapPlot(
    projection=sp.Projection.ZENITH,
    lat=33.363484,
    lon=-116.836394,
    dt=datetime.now(tz).replace(hour=22),
    style=sp.styles.PlotStyle().extend(
        sp.styles.extensions.BLUE_MEDIUM,
    ),
    resolution=4096,
    autoscale=True,
)
p.constellations()
p.stars(where=[_.magnitude < 4.6])
p.constellation_labels()
p.export("starchart.png")
```

## Documentation

[https://starplot.dev](https://starplot.dev)


## Demo
For a demo of Starplot's zenith plots, check out: 

[Sky Atlas - Star Chart Creator](https://skyatlas.app/star-charts/)

## Discord

Chat with other starplotters on our Discord server:

https://discord.gg/WewJJjshFu

## Contributing

Contributing to Starplot is welcome and very much appreciated! Please see [here](CONTRIBUTING.md) for details.

## Coming Soon
- 🧮 Coordinate system helpers
- 🌑 Planet moons
- ✴️ Custom markers
- ☄️ Comet model
- 😄 🔭 Clear skies

See more details on the [Public Roadmap](https://trello.com/b/sUksygn4/starplot-roadmap)

## License
[MIT License](https://github.com/steveberardi/starplot/blob/main/LICENSE)
