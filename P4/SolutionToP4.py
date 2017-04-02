from ReadData import *
from PrintData import *
from Analysis import *

filename = 'data4.xlsx'

data = readdata(filename)

analysis(xys)

#printdata(xys)               
#printanalysis(xys, result)     
printall(xys, result)

showfigure(xys)
