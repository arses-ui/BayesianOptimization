import xlsxwriter

workbook = xlsxwriter.Workbook('../Desktop/parameters.xlsx')
worksheet = workbook.add_worksheet()

parameters = (
['carrier_GFR',120],
['sheath_GFR', 12],
['speed', 300],
['loops', 1] 
)

row = 0 
col = 0 


for parameter, value in (parameters): 
    worksheet.write(row, col, parameter) 
    worksheet.write(row, col+1, value)
    row+=1

workbook.close()

