import xlsxwriter


def display_curvature_in_excel(path_and_filename, points, curvature):
    if path_and_filename[-5:] != '.xlsx' and path_and_filename[-4:] != '.xls':
        path_and_filename += '.xlsx'
    filename = path_and_filename
    excel_book = xlsxwriter.Workbook(filename)
    worksheet = excel_book.add_worksheet('sheet 1')
    for i in range(len(curvature) + 1):
        if not i:
            worksheet.write(i, 0, 'x')
            worksheet.write(i, 1, 'y')
            worksheet.write(i, 2, 'curvature')
            continue
        worksheet.write(i, 0, points[0][i-1])
        worksheet.write(i, 1, points[1][i-1])
        worksheet.write(i, 2, curvature[i-1])
    excel_book.close()