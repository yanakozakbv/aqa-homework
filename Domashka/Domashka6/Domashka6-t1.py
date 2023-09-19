"""""1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні
на поточну дату (курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv
"""
import csv

grn = float(36.56)

with open('test_file.csv', 'r') as f:
    rows = csv.reader(f)
    parsedRows = [row for row in rows]
    result = [[(float(item) * grn if item.isnumeric() else item) for item in row] for row in parsedRows]

with open('salaries_uah.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(result)

