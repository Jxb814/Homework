from ReadData import *
from PrintData import *
from Analysis import *


filename = 'data4.xlsx'
XYs = []
Result = []

data, XYs = readdata(filename)

Result = analysis(XYs)

printdata(XYs)               
printanalysis(XYs, Result)     

#showfigure(XYs)            only for four groups of data
printmorefig(XYs)           # for all 
