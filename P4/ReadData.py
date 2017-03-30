import xlrd

x = []
y = []

def readdata():
    data = xlrd.open_workbook('data4.xlsx')

    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    n = int(ncols/2)
    global x, y

    for i in range(n):
        x.append(table.col_values(i*2))
        y.append(table.col_values(i*2+1))
        
    return n

n = readdata()

def printdata():
    for i in range(n):
        print('x', i, '=', x[i])
        print('y', i, '=', y[i])
