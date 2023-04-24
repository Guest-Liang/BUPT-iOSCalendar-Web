# BUPT-iOSCalendar-Web   
填写学号以及教务密码，从教务系统中获取学期课表制作成ics文件   

## 使用方法   
### 第一步   
本地运行py文件需要`高于python3.10`的`python`环境，以及`nodejs`环境，并且配置好环境变量等，命令行中输入`python -V`以及`node -v`能出现版本号   
nodejs下载地址：https://nodejs.org/en/download/   
安装过程请自行搜索解决   
如果已经配置好，在`cmd`或者`PowerShell`运行以下命令，安装需要的库：   
```python3
pip install icalendar
pip install requests
pip install PyExecJS
pip install pywin32
pip install openpyxl
```   
连接不上或速度过慢可使用清华源：   
```python3
pip install icalendar -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install PyExecJS -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple
```   

### 第二步
在GitHub页面右边的`release`下载`Main.py`文件和`Constant.py`文件   
编辑`Constant.py`文件，在第二、第三行填入学号、教务系统密码   
在第四行修改本学期第一周星期一的日期，以YYYY-MM-DD的格式填入，例如2023-02-20，注意不要填错   
然后在当前目录空白处右键"在终端中打开"（win11），或者按win+R键打开运行，输入`Powershell`or`cmd`，打开命令行窗口，执行   
```python3
python Main.py
```   
看到最后的`[Success]`就说明成功了，ics文件生成在当前目录下    
如果失败了请提issue，并附上一切必要的信息   

### 第三步
得到的ics文件导入Apple设备中即可使用。  
推荐添加到一个新的日历：以学年命名或者学习，这样万一添加错误还可以通过删除整个日历来重新添加，不需要一个个手动删除   
**建议在日历中新建好新的日历再打开ics文件添加**   
确保在添加到日历前全部检查一遍，包括日期、上课时长等等，否则需要重新添加   
有问题千万不要导入！

# 目前bug：  
iOS & iPadOS不能识别私有属性中的颜色，导致`X-APPLE-CALENDAR-COLOR`这一项参数无效   