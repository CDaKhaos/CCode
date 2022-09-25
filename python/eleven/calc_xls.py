import openpyxl as xls
import calc_eleven as calc

# workbook as wb
# worksheet as ws
from math import ceil
lst = [1, 2, 3, 4, 5]
def list_ceil(lst, num=3):
    return list(map(lambda x: lst[x * num : x * num + num], list(range(0, ceil(len(lst) / num)))))
# print(test(lst, 2))


file_name = './test.xlsx'
cell_heigh = 58
cell_width = 26
cell_font = xls.styles.Font(size=20)
cell_border = xls.styles.Border(bottom=xls.styles.Side(
    border_style="dashed", color='000000'))
cell_align = xls.styles.Alignment(horizontal='left', vertical='center')
calc_row = 14

wb = xls.Workbook()

ws = wb.active
ws.title = 'eleven'
# print(ws.title)

# ws.cell(1, 1).value = '10+20='+str_space
calc = calc.c_calc(calc_row*9, 20)
calc.create()
list_ques = calc.get_question()
list_calc_ceil = list_ceil(list_ques)
# for n in list_calc:
    # print(n[0])
for que in list_calc_ceil:
    ws.append(que)

rows = ws.max_row
cols = ws.max_column
for r in range(1, rows+1):
    for c in range(1, cols+1):
        ws.cell(r, c).font = cell_font
        ws.cell(r, c).alignment = cell_align
        if (r % (calc_row/2)) == 0:
            ws.cell(r, c).border = cell_border


for r in range(1, rows+1):
    ws.row_dimensions[r].height = cell_heigh

for c in ['A', 'B', 'C']:
    ws.column_dimensions[c].width = cell_width

ws.page_margins = xls.worksheet.page.PageMargins(top=0.2, bottom=0.1)

wb.save(file_name)
