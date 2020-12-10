#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: xiuyu
@time: 20-06-01
"""

import xlrd
import os


class ExcelData:
    """
    获取excel基本功能获取接口数据
    """

    def __init__(self, xlsname, sheetname):
        self.xlsname = xlsname
        self.sheetname = sheetname
        self.workbook = xlrd.open_workbook(self.xlsname)
        self.sheet_data = self.sheet_data()
        self.row_length = self.get_row_num()

    # 打开指定sheetname
    def sheet_data(self):
        return self.workbook.sheet_by_name(self.sheetname)

    # 获取excel行数
    def get_row_num(self):
        return self.sheet_data.nrows

    # 获取指定sheet
    def get_sheet(self):
        sheetname = self.workbook.sheet_names()
        return sheetname

    # 获取数据url+data
    def get_date(self):
        api_list = []
        value = None
        # 将登录参数以列表数据返回
        for i in range(1, self.row_length):
            value = self.sheet_data.row_values(i)
            date = {
                "api": value[0],
                "data": value[1],
                "type": value[2]
            }
            api_list.append(date)
        return api_list


if __name__ == '__main__':
    pass
    # print(os.path.abspath('..'))
    # excel_path = os.path.abspath('..') + r'/yongli/yongli.xlsx'
    # excel_data = ExcelData(excel_path, 'Sheet1')
    # print(excel_data.get_date())
