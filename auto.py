#!/usr/bin/python
# -*- coding:utf-8 -*- 


from widget import Widget
import unittest

from log import log


##用于使用HTML进行报告输出的库
from HTMLTestRunner import HTMLTestRunner


# 执行测试的类
class WidgetTestCase(unittest.TestCase): 
    '''继承于Testcase, 是功能类 Widget 对应的测试类'''

    def setUp(self):
        '''
            是父类TestCase中定义的函数
            在setUp()方法中进行测试前的初始化工作
        '''
        # print "do something before test.Prepare environment."
        self.widget = Widget()

    def tearDown(self):
        '''
            是父类TestCase中定义的函数
            在tearDown()方法中执行测试后的清除工作
        '''
        # print "do something after test.Clean up."
        self.widget = None

    @classmethod
    def setUpClass(cls):
        '''
            如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们可以用 setUpClass() 与 tearDownClass()
        '''
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        '''
            如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们可以用 setUpClass() 与 tearDownClass()
        '''
        print "This tearDownClass() method only called once too."

    @log
    def testSize(self):
        '''
            测试类中,所有以test开头的函数,都可以在调用unittest.mian()被自动执行
            也可以自己构造测试集
        '''
        self.assertEqual(self.widget.getSize(), (40, 40))

    @log
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (1020, 100))

    @log
    def runTest(self):
        '''
            PyUnit测试框架在运行一个测试用例时，TestCase子类定义的setUp()、runTest()和tearDown()方法被依次执行，最简单的测试用例只需覆盖runTest()方法来执行特定的测试代码就可以了
        '''
        widget = Widget()
        self.assertEqual(widget.getSize(), (40, 40))
        
    ## 跳过某个测试用例
    ## skip装饰器一共有三个 unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition, reason)，skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
    @unittest.skip("I don't want to run this case.")
    def testDispose(self):
        pass


# 构造测试集
def gen_suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    suite.addTest(WidgetTestCase("testDispose"))
    # suite.addTest(WidgetTestCase("testResize"))
    return suite


# 测试
if __name__ == "__main__":

    #==========================================================
    # 调用测试集的第一种方法
    # unittest.main(defaultTest = 'gen_suite')
    # unittest.main()


    #==========================================================
    # 调用测试集的另一种方法
    # 构造测试集
    # 执行测试
    # suite = gen_suite()
    # # runner = unittest.TextTestRunner()
    # runner = unittest.TextTestRunner(verbosity=2) # 参数用于指定输出测试函数名称
    # runner.run(suite)

    #==========================================================
    # 将结果用文件输出
    # suite = gen_suite()
    # with open('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    #===========================================================
    # 将结果用HTML报告的形式输出
    # 资料来源 :http://tungwaiyip.info/software/HTMLTestRunner.html
    # suite = gen_suite()
    # with open('HTMLReport.html', 'w') as f:
    #     runner = HTMLTestRunner(stream=f,
    #                             title='MathFunc Test Report',
    #                             description='generated by HTMLTestRunner.',
    #                             verbosity=2
    #                             )
    #     runner.run(suite)


    #===========================================================
    # 中文HTML结果的输出, 资料来源:https://github.com/findyou/HTMLTestRunnerCN
    import HTMLTestRunnerCN
    suite = gen_suite()
    with open('res/HTMLReportCN.html', 'w') as f:
        runner = HTMLTestRunnerCN.HTMLTestRunner(
            stream=f,
            title=u'Widget单元测试报告',
            description='description',
            tester="corey"
            )
        runner.run(suite)