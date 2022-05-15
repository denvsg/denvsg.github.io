# 表格文件 读写


2、表格读写
2.1：xlrd/xlwt库，新版不支持xlsx格式，读取最大行为65535
1、使用xlrd.open_workbook(file)创建一个工作表对象
2、使用 sheet_names()  方法获取workbook中所有工作表的名字
3、获取表格：以下三个函数都会返回一个xlrd.sheet.Sheet()对象
table = wb.sheets()[0]  # 通过索引顺序获取
table = wb.sheet_by_index(0)) #通过索引顺序获取
table = wb.sheet_by_name(sheet_name)#通过名称获取
4、行
nrows = table.nrows  #获取该sheet中的有效行数
table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表,类型+数据
table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
table.row_len(rowx) #返回该列的有效单元格长度
5、列
ncols = table.ncols   #获取列表的有效列数
table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表
table.col_values(colx, start_rowx=0, end_rowx=None)   #返回由该列中所有单元格的数据组成的列表
6、单元格cell
table.cell(rowx,colx)   #返回单元格对象 类型+数据
table.cell_type(rowx,colx)    #返回单元格中的数据类型
table.cell_value(rowx,colx)   #返回单元格中的数据
table.cell_xf_index(rowx, colx)   # 暂时还没有搞懂
7、遍历读取示例
for i in range(nrows):
for j in range(ncol):
print(table.cell_value(i,j),end=" ")
print()

        写表格：写需要先倒入xlwt库，即import xlwt
            # 创建一个workbook 设置编码
            workbook = xlwt.Workbook(encoding = 'utf-8')
            # 创建一个worksheet
            worksheet = workbook.add_sheet('My Worksheet')
            # 写入excel
            # 参数对应 行, 列, 值 worksheet.write(1,0, label = 'this is test')
            # 保存    workbook.save('Excel_test.xls')
        写入样式：
            style = xlwt.XFStyle() # 初始化样式
            font = xlwt.Font() # 为样式创建字体
            font.name = 'Times New Roman'
            font.bold = True # 黑体
            font.underline = True # 下划线
            font.italic = True # 斜体字
            style.font = font # 设定样式
            worksheet.write(0, 0, 'Unformatted value') # 不带样式的写入
            worksheet.write(1, 0, 'Formatted value', style) # 带样式的写入

            # 设置单元格宽度 worksheet.col(0).width = 3333


    2.2：openpyxl
        from openpyxl import Workbook或者from openpyxl import load_workbook
        前者 不需要有excel文件存在 后者需要传入一个excel文件，前者可以凭空产生一个 后者不行,即读取和新建写入

        openpyxl三步走
        1、获取work book
            使用workbook或load_workbook方法，例如
            from openpyxl import Workbook
            from openpyxl import load_workbook
            wb = Workbook()
            wb = load_workbook("file.xlsx")
        2、获取 work sheet
            使用 workbook.active方法获取当前工作表
            使用 workbook[sheet_name] 获取指定表名的工作表 #直接在work_book后面[ sheet_name ]
            使用 workbook.create_sheet([sheetname],[index]) 新建一张表，接受间隔可选参数：表名和索引，不给默认表名，在表后新建
            使用 workbook.get_sheet_names()/workbook.sheetnames 获取所有工作表
            Worksheet:
                title：表格的标题
                max_row：表格的最大行
                min_row：表格的最小行
                max_column：表格的最大列
                min_column：表格的最小列
                rows：按行获取单元格(Cell对象) - 生成器
                columns：按列获取单元格(Cell对象) - 生成器
                values：按行获取表格的内容(数据) - 生成器
            Cell:
                row：单元格所在的行
                column：单元格坐在的列
                value：单元格的值
                coordinate：单元格的坐标

        3、获取单元格 进行操作
            遍历单元格
                sheet = wb['sheetname']
                for row in sheet.rows:
                    # 循环遍历每一个单元格
                    for cell in row:
                        # 获取单元格的内容
                        print(cell.value, end=',')
                    print()
        4、保存文件
            使用save方法保存 workbook.save(filename)

    2.3：pandas 数据分析常用的库，依赖于xlrd，openpyxl
        import pandas as pd
        file = "books.xls"
        data = pd.read_excel(file) #读取表格文件，使用sheet_name参数指定表单

        data= pd.to_excel(file) 进行写入表格
        print(data)


