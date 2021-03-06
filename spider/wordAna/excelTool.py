
#文件中用到了xlrd模块

import xlrd             #读excel工具
import xlsxwriter       #写excel工具
from config.n_conf import dirPath

class ExcelOperator():
    '''
    excel操作工具
    getInfo为读取excel表数据，返回类型为list,list中每个元素为dict，对应键值为 列名：值
        参数为filePath：  excel文件的绝对地址

    '''

    def __init__(self):
        #用于关键词分析后的excel数据表
        self.colnames = ["index","title","display_url","display_time","source",
                         "keywords","abstract","images","tag","feature","textContent""htmlContent","img"]
    def getExcelInfo(self,filePath):
        try:
            data = xlrd.open_workbook(filePath)
            list = []
            if data:
                table = data.sheet_by_index(0)
                if table:
                    nrows = table.nrows  # 表的行数
                    colnames = table.row_values(0)  # 表的列名(list)
                    clen = len(colnames)  # 列名个数
                    for rownum in range(1, nrows):
                        row = table.row_values(rownum)
                        if row:
                            app = {}
                            for i in range(1, clen):
                                app[self.colnames[i]] = row[i]
                            list.append(app)

            return list
        except:
            print ("xlrd读取" + filePath + "文件出错")
            exit()

    def saveToExcel(self,excelName,sheetName,data):
        """
        将数据生成excel表
        :param data: 数据
        :param excelName  保存的excel表名,绝对路径
        :param sheetName  工作表名称
        :return:     返回生成的excel表
        """
        # 设置excel表名称
        print(excelName)
        open(excelName,'w')
        jr_work = xlsxwriter.Workbook(excelName)            #避免混淆
        jr_sheet = jr_work.add_worksheet(sheetName)
        bold = jr_work.add_format({'bold': True})  # 设置一个加粗的格式对象
        jr_sheet.set_column('A:H', 40)
        jr_sheet.set_column('C:D', 15)
        jr_sheet.write(0, 0, 'index', bold)
        jr_sheet.write(0, 1, 'title', bold)
        jr_sheet.write(0, 2, 'display_url', bold)
        jr_sheet.write(0, 3, 'display_time', bold)
        jr_sheet.write(0, 4, 'source', bold)
        jr_sheet.write(0, 5, 'keywords', bold)
        jr_sheet.write(0, 6, 'abstract', bold)
        jr_sheet.write(0, 7, 'images', bold)
        jr_sheet.write(0, 8, 'tag', bold)
        jr_sheet.write(0, 9, 'feature', bold)
        jr_sheet.write(0, 10, 'textContent',bold)
        jr_sheet.write(0, 11, 'htmlContent',bold)
        jr_sheet.write(0, 12, 'img_url', bold)
        line = 0
        for eachData in data:
            line += 1
            jr_sheet.write(line, 0, str(line))
            jr_sheet.write(line, 1, eachData["title"])
            jr_sheet.write(line, 2, eachData["display_url"])
            jr_sheet.write(line, 3, eachData["display_time"])
            jr_sheet.write(line, 4, eachData["source"])
            jr_sheet.write(line, 5, eachData["keywords"])
            jr_sheet.write(line, 6, eachData["abstract"])
            if eachData["display_url"].find("sina.com") != -1:
                if eachData["img"]:
                    sinaImg = ','.join(eachData["img"])
                    jr_sheet.write(line, 7, sinaImg)
            else:
                jr_sheet.write (line, 7, str (eachData ["images"]))
            jr_sheet.write(line, 8, eachData["tag"])
            jr_sheet.write(line, 9, ' '.join(eachData["feature"]),bold)
            jr_sheet.write(line, 10, eachData["textContent"])
            jr_sheet.write(line, 11, eachData["htmlContent"])
            jr_sheet.write(line, 12, ','.join(eachData["img"]))
        jr_work.close()
        log = "%sExcel文件保存完成" % (excelName)
        with open(dirPath+"/log.txt", 'a') as fp:
            fp.write(log + "\n")
        print(log)








