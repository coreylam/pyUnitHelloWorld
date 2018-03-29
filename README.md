# pyUnitHelloWorld
个人学习使用python的unittest进行单元测试的学习代码.

主文件为 `auto.py` .
功能类为 `widget.py`

使用了HTML输出测试结果
---
这里使用了 [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html), 不过由于该文件不支持中文, 所以对 `HTMLTestRunner.py` 进行小小的修改, 支持中文输出.具体改动如下:

	#在首行添加如下代码
    #coding=utf-8
    
    # 在import 部分添加如下代码
    reload(sys)
	sys.setdefaultencoding('utf-8')
    
对于中文输出, 还使用了github上另一个中文输出的资源([HTMLTestRunnerCN](https://github.com/findyou/HTMLTestRunnerCN)), 但对其中的字体和对齐进行了个性化的修改,改动不大.