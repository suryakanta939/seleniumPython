import xlrd

class read():
    def getDataFromXcel(self,fileName):
        xlsheeet = xlrd.open_workbook(fileName)
        sh = xlsheeet.sheet_by_name("data")
        totalRow = sh.nrows
        print("total row is "+str(totalRow))
        totalCol = sh.ncols
        print("total col is "+str(totalCol))
        data = []
        for row in range(1, totalRow):
            rowdata=[]
            data.append(rowdata)
            for col in range(0, totalCol):
                result = sh.cell_value(row, col)
                rowdata.append(result)

        return data


run=read()
data=run.getDataFromXcel("C:\\Users\\surya\\Desktop\\name.xlsx")
print(data)