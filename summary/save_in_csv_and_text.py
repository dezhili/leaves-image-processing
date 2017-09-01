# save to results of csv format
def save_in_csv_serrations(f, serrations, serrations_names, filename):

    sheet1 = f.add_sheet(filename, cell_overwrite_ok=True)
    for i in range(len(serrations)):
        sheet1.write(0, i, serrations_names[i])
    for i in range(9):
        if i == 0:
            for j in range(1, serrations[i]+1):
                sheet1.write(j, i, j)
            continue
        for j in range(1, len(serrations[i])+1):
            sheet1.write(j, i, serrations[i][j-1])

def save_in_csv_curvatures(f, serrations_curvatures, boundary_curvature, filename):
    # 442_100_curvatures.xls
    sheet2 = f.add_sheet(filename, cell_overwrite_ok=True)
    for i in range(len(serrations_curvatures)):
        sheet2.write(0, i, 'serrations_' + str(i + 1) + '_curvature')
    sheet2.write(0, len(serrations_curvatures), 'boundary_curvature')
    for i in range(len(serrations_curvatures)):
        for j in range(1, len(serrations_curvatures[i]) + 1):
            sheet2.write(j, i, serrations_curvatures[i][j - 1])
    for i in range(1, len(boundary_curvature) + 1):
        sheet2.write(i, len(serrations_curvatures), boundary_curvature[i - 1])