import unittest
from common.calculator import Math

'''
testcase（测试用例）
1、测试类必须继承unittest.TestCase
2、一个测试方法就是一个测试用例，测试方法必须以test开头。
方法：
1)，导入unittest模块。
2)，创建测试类。测试类的命名不做要求，但需要继承unittest.TestCase类。
3)，添加setUp()、tearDown()函数，即测试固件。
4)，定义测试方法，即测试用例。测试方法名称必须以test开头，否则测试时该方法将不会被执行。测试方法里需要添加断言。
5)，调试执行测试用例。执行当前模块的测试用例时，调用unittest.main()方法，该方法会搜索该模块下所有以test开头的测试用例方法，并执行
'''


class SumTest(unittest.TestCase):
    """测试Math类中的sum函数     """

    def setUp(self):
        print("开始执行测试用例{}...".format(self))

    def test_sum01(self):
        m = Math(3, 4)
        self.assertEqual(m.sum(), 7)

    def test_sum02(self):
        m = Math(2, 8)
        self.assertEqual(m.sum(), 11)

    def tearDown(self):
        print("测试用例{}执行结束...".format(self))


if __name__ == '__main__':
    unittest.main()
