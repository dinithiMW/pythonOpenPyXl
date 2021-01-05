import openpyxl as xl
from openpyxl.chart import BarChart,Reference

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
print(sheet.max_row)