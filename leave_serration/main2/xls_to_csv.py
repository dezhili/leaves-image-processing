import xlrd
import csv


def csv_from_excel(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    all_worksheets = workbook.sheet_names()
    for worksheet_name in all_worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        your_csv_file = open(''.join([worksheet_name, '.csv']), 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(worksheet.nrows):
            wr.writerow([entry.encode("utf-8") for entry in worksheet.row_values(rownum)])
        your_csv_file.close()

csv_from_excel('442_100.xls')