import unittest
import package
import os
import json
import HtmlTestRunner


class ApiTest(unittest.TestCase):
    """
    媒体接口
    """
    def Set
    def test_01(self):
        re = package.request(api_test[0]['api'], api_test[0]['data'], api_test[0]['type'])
        code = re.html()
        self.assertEqual(code, 200, '返回状态码错误，不为200')


if __name__ == '__main__':
    pass
    # excel_path = os.path.abspath('..') + r'/yongli/yongli.xlsx'
    # excel_data = package.excel.ExcelData(excel_path, 'Sheet1')
    # api_test = excel_data.get_date()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
