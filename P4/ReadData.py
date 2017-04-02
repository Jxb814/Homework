import xlrd


def readdata(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    n = int(ncols/2)
    x = []
    y = []
    xys = []
    for i in range(n):    
        xys.append({'x':table.col_values(i*2), 'y':table.col_values(i*2+1)})

    return data, xys

