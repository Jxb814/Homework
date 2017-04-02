import xlrd

x = []
y = []
xys = []
filename = ''

def readdata(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    n = int(ncols/2)
    
    for i in range(n):    
        xys.append({'x':table.col_values(i*2), 'y':table.col_values(i*2+1)})

    return data

