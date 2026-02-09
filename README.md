# export_pic
A simple Windows GUI tool that, based on the order of the input text, batch-copies the corresponding character’s TIF/PSD files and outputs them with automatic numbering.

根据输入文本顺序，将对应字符的 TIF / PSD 文件批量复制并自动编号输出的 Windows GUI 工具。
![Downloads](https://img.shields.io/github/downloads/F1yreD/export_pic/total)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=F1yreD.export_pic)
## Windows下载
👉 [下载链接](https://github.com/F1yreD/export_pic/releases/latest)

The executable file is provided for convenience.  
Copyright © 2026 F1yreD.

# 下面可以不看
## if you want to use cmd version:
1. [点击链接下载python包](https://www.python.org/ftp/python/3.13.12/python-3.13.12-amd64.exe)
2. 打开.exe
3. 勾选下面两个选项并点击install now

#### cmd使用步骤：
👉 [下载 python脚本](https://github.com/F1yreD/export_pic/releases/tag/cmd_v1.0.0)
1. 按win+r输入cmd运行
2. 输入cd /d C:\Users\sxsc\Desktop     这是你存放.py文件的文件夹的路径
3. 输入python export_pic.py
3.输入你存放tif文件的文件夹地址，不要带双引号，可以右键文件夹打开属性里面复制
4. 输入你要存放目标文件的文件夹地址，不要带双引号，如果没有这个文件夹会自动创建，如果有这个文件夹会覆盖里面的文件

#### 关于cmd后续使用：
1. 装tif的文件夹可以增加新的tif文件，但同名文件不识别，且文件名必须是一个字
2. 如果需要省去使用步骤的34可以编辑一下export_pic.py文件中的config字段
3. 字数上限为1e5

## if you want to use gui version:
1. install python and pyinstaller(you can use "pip install python" and "pip install pyinstaller" to install it)
2. right click to run cmd in file folder
3. type "pyinstaller -F -w export_pic_gui.py"
4. click "./build/export_pic_gui.exe"