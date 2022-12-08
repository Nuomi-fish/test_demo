import time
import requests
import HTMLTestRunner
import smtplib
import BSTestRunner
import smtplib
import unittest

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 获取当前时间并指定时间格式，用于测试报告命名
now = time.strftime("%Y-%m-%d_%H_%M_%S")
# 测试报告存储路径
report_dir = './report/'
# 创建报告文件，并以写的形式打开文件，用于写入报告内容
fp = open(report_dir + now + "_report.html", 'wb')
# 初始化一个HTMLTestRunner实例对象，用来生成报告
runner = BSTestRunner.BSTestRunner(stream=fp,
                                       title="App自动化测试报告",
                                       description="测试用例情况")

# 定义测试用例路径
test_dir = './testcase'
# 加载测试用例
# testsuite（测试套件） 把多条测试用例集合到一起，通过一系列代码去控制要执行哪些测试方法、测试类或测试用例
''' 方法一：
实例化： suite = unittest.TestSuite() (suite：为TestSuite实例化的名称)
添加用例：suite.addTest(ClassName(“MethodName”)) (ClassName：为类名；MethodName：为方法名) '''
''' 方法二：
从文件中加载测试用例，然后形成测试套件 
'''
suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')  # 通常我们测试脚本会有很多个，存放在某个目录下，那么我们可以批量加载

'''方法三：
测试类中加载用例,形成suite套件
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Add)
'''
# 执行测试用例
runner.run(suite)
fp.close()
# 发送邮件主题
subject = "Python email test"
# 读取附件内容
with open(report_dir + now + "_report.html", 'rb') as fp:
    send_att = fp.read()
# 定义发送邮件的正文、格式、编码
att = MIMEText(send_att, 'text', 'utf-8')
# 定义附件类型
att["Content-Type"] = 'html'
# 显示附件的文件
att['Content-Disposition'] = 'attachment;filename="TestReport.html"'
msg = MIMEMultipart()
msg['Subject'] = Header("自动化测试报告", "utf-8")
msg.attach(att)
# 发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
smtp.login("1900527504@qq.com", "rjmjhvblzgqqbaee")
smtp.sendmail("1900527504@qq.com", "teddy.tang@dbappsecurity.com.cn", msg.as_string())
smtp.quit()


