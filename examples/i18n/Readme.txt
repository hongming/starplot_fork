目前i18n内的字体，是微软Windows的微软雅黑。 如果使用Mac OS设备，请讲中文字体名称替换。

安装和运行
1、安装Python环境
	1.1 访问https://www.python.org/downloads/，下载并完成安装，留意勾选“Add to PATH”选项。
	1.2 打开Windows的命令行提示符，输入python --version，如果返回类似Python 3.13.5的信息，说明安装成功。

2、安装StarPlot的软件库
	2.1 在命令行提示符界面，输入pip install starplot，按提示完成安装。

3、将压缩包解压至C盘特定目录，比如C:\starplot

4、在命令行提示符界面内，切换至这个目录，cd C:\starplot

5、运行命令python map_sagittarius_cn.py，即可生成新版本map_sagittarius.png

第5点例子修改说明
这个文件是从https://starplot.dev/examples/map-sagittarius/例子修改

第20-23行，这里约定了显示区域，通过十进制的RA和DEC范围。

第5行、通过 from i18n.ZH_CN import …… 引用中文化对应文件，这些文件在i18n目录内，可以自行添加、编辑，注意恒星使用HIP编号（https://starplot.dev/data/star-designations/），深空天体使用对应的name（https://starplot.dev/data/dsos/，梅西耶使用对应NGC）

第9和15行，注释掉源文件的extension.ANTIQUE样式文件。引入Local_styles内对应的文件，主要是添加中文字体；字号大小、颜色、背景色等都可以在这里调整。

第51和61行，注释掉原例子，改为只显示_.name.isin里的天体，并且label_fn对应对应的中文内容

第126行，通过labels，显示星座的中文名称

更多细节，请参考开发者的原始文档https://starplot.dev/examples/和https://starplot.dev/reference-mapplot/