import time
import HtmlTestRunner
from common.get_conf import *
from run.case_list import *
import unittest

testsuit = unittest.TestSuite()
for case in all_cases:
    testsuit.addTest(unittest.makeSuite(case))
    print(case)

report_time = time.strftime("%Y-%m-%d_%H_%M_%S")
# filename = report_folder + report_time + '_Test_Report.html'
# fp = open(filename, 'w')
runner = HtmlTestRunner.HTMLTestRunner(report_title="Anroid Test Rerpot", descriptions='Anroid Test Report', output=report_folder)
runner.run(testsuit)