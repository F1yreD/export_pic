# export_pic


### if you want to use cmd, you should:
1. 打开"Downloads\python-3.9.6-amd64.exe"
2.勾选下面两个选项并点击install now

#### 使用步骤：
1. 按win+r输入cmd运行
2. 输入cd /d C:\Users\sxsc\Desktop     这是你存放.py文件的文件夹的路径
3. 输入python export_pic.py
3.输入你存放tif文件的文件夹地址，不要带双引号，可以右键文件夹打开属性里面复制
4. 输入你要存放目标文件的文件夹地址，不要带双引号，如果没有这个文件夹会自动创建，如果有这个文件夹会覆盖里面的文件

#### 关于后续使用：
1. 装tif的文件夹可以增加新的tif文件，但同名文件不识别，且文件名必须是一个字
2. 如果需要省去使用步骤的34可以编辑一下export_pic.py文件中的config字段



### if you want to use gui, you should:
1. install python and pyinstaller(you can use "pip install python" and "pip install pyinstaller" to install it)
2. right click to run cmd in file folder
3. type "pyinstaller -F -w export_pic_gui.py"
4. click "./build/export_pic_gui.exe"

## download
👉 [下载 Windows 可执行文件（exe）](https://github.com/F1yreD/export_pic/releases/latest)
