import unittest
from BT25_setup_teardown import ExampleSeleniumTestCase
from BT26 import ExampleSeleniumTestCase1
import HtmlTestRunner

def sampleTestSuite():
    mySuite = unittest.TestSuite()
    mySuite.addTest(ExampleSeleniumTestCase('test_open_google'))
    mySuite.addTest(ExampleSeleniumTestCase('test_open_vnexpress'))
    # mySuite.addTest(SampleTestcase1('test_case1'))
    # mySuite.addTest(SampleTestcase1('test_case2'))
    return mySuite
if __name__ == '__main__':
    mySuite = sampleTestSuite()
    runner = HtmlTestRunner.HTMLTestRunner(report_title='Sample Report')
    runner.run(mySuite)

    
