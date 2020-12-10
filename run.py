import package
import os
import json
import unittest
import case
import HtmlTestRunner


def run_case():
    """
    打包test
    :return:
    """
    suite = unittest.TestSuite()
    suite.addTest((case.ApiTest('test_01')))
    # st = open('../report/report.html', 'wb')
    runner = HtmlTestRunner.HTMLTestRunner(output='example_suite')
    runner.run(suite)


if __name__ == '__main__':
    excel_path = os.path.abspath('..') + r'request_unitest/yongli/yongli.xlsx'
    excel_data = package.excel.ExcelData(excel_path, 'Sheet1')
    api_test = excel_data.get_date()
    run_case()
