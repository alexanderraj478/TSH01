from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

data = [
    ['Item', 'Colour'],
    ['pen', 'brown'],
    ['book', 'black'],
    ['plate', 'white'],
    ['chair', 'brown'],
    ['coin', 'gold'],
    ['bed', 'brown'],
    ['notebook', 'white'],
]

for r in data:
    print(r)
    sheet.append(r)

sheet.auto_filter.ref = 'A1:B8'
sheet.auto_filter.add_filter_column(1, ['brown', 'white'], blank=False)
sheet.auto_filter.add_sort_condition('B2:B8')
#sheet.auto_filter.ref = 'B2:B8'
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "", "Vicky")

x = zip(a, b)
print(tuple(x))
#use the tuple() function to display a readable version of the result:

#print(tuple(x))


wb.save('filtered.xlsx')