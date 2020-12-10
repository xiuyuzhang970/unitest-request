#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: xiuyu
@time: 20-06-01
"""

import json
import os
import requests
import package


# 接口GET,POST方法
class request:
    def __init__(self, api, data, type):
        self.api = api
        self.data = data
        self.type = type
        self.post_data = json.dumps(self.data)

    def get_api(self):
        re = requests.get(self.api, data=self.post_data)
        return re.status_code

    def post_api(self):
        re = requests.post(self.api, data=self.post_data)
        return re.status_code

    def html(self):
        if self.type == 'post':
            try:
                print(self.post_api())
                return self.post_api()
            except:
                print('连接异常:由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。' + 'api=' + self.api)
        elif self.type == 'get':
            try:
                print(self.get_api())
                return self.get_api()
            except:
                print('连接异常:由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。' + 'api=' + self.api)
        else:
            print('报错:找不到操作方法' + 'api=' + self.api)


if __name__ == '__main__':
    pass
    # excel_path = os.path.abspath('..') + r'/yongli/yongli.xlsx'
    # excel_data = package.excel.ExcelData(excel_path, 'Sheet1')
    # api_test = excel_data.get_date()
    # re = request(api_test[0]['api'], api_test[0]['data'], api_test[0]['type'])
    # re.html()
