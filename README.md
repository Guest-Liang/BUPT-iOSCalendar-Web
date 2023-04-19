# BUPT-iOSCalendar-Web   
填写学号以及教务密码，从教务系统中获取学期课表制作成ics文件   

## 使用方法   
### 第一步   
需要`高于python3.10`的`python`环境，并且配置好环境变量等，确保`Powershell`中输入`python`能出现版本号并进入python环境。如果已经配置好，在`cmd`或者`PowerShell`运行以下代码，安装需要的库：   
```python3
pip install icalendar
pip install requests
pip install PyExecJS
```   
连接不上可使用清华源：   
```python3
pip install icalendar -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install PyExecJS -i https://pypi.tuna.tsinghua.edu.cn/simple
```   

### 第二步
在GitHub页面右边的`release`下载`Main.py`文件和`Constant.py`文件，编辑`Constant.py`文件，在第二、第三行填入学号、教务系统密码，然后在当前目录空白处右键“在终端中打开”，或者打开`Powershell`，进入管理员模式，执行   
```python3
python Main.py
```   
看到最后的Success就说明成功了，ics文件生成在当前目录下    
如果失败了请提issue，并附上一切必要的信息   

### 第三步
得到的ics文件导入Apple设备中即可使用。  
推荐添加到一个新的日历：以学年命名或者学习，这样万一添加错误还可以通过删除整个日历来重新添加，不需要一个个手动删除   
**建议在日历中新建好新的日历再打开ics文件添加**   
确保在添加到日历前全部检查一遍，不然需要重新添加   
有问题千万不要导入！

