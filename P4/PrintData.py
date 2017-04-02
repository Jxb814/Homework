import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from Analysis import *


def printdata(xys):
    '''only print out the data'''
    n = len(xys)
    for i in range(n):
        print('x', i, '=', xys[i]['x'])
        print('y', i, '=', xys[i]['y'], '\n')


def printanalysis(xys, result):
    '''only print out the analysis result'''
    n = len(xys)
    table = []
    for i in range(n):
        table.append([i, result[i]['x_average'], result[i]['y_average'],
                       result[i]['x_variance'],result[i]['y_variance'],
                       result[i]['xy_corrcoef']])
    
    headers=['No.', 'x_average', 'y_average', 'x_variance', 'y_variance', 'xy_corrcoef']
    print (tabulate(table, headers, tablefmt = 'rst'))


def plotData(x, y):
    '''plot the discrete data'''
    X = np.array(x)
    Y = np.array(y)
    
    plt.plot(X, Y, 'ro', label = 'Discrete data')


def plotlinearfitData(a, x, predicted):
    '''plot the predicted line'''
    X = np.array(x)

    plt.plot(X, predicted,
             label = 'Displacements predicted\nby linear fit, a = ' 
             + str(round(a, 5)))
   
    plt.legend(loc = 'best')


def showfigure(xys):
    '''show the pieces as four parts within one big figure'''
    fig = plt.figure(figsize = (10,7))

    plt.subplot(221)
    plotData(xys[0]['x'], xys[0]['y'])
    a, b, predicted = linearfitData(xys[0]['x'], xys[0]['y'])
    plotlinearfitData(a, xys[0]['x'], predicted)     
    plt.title('Sample1')       
    
    plt.subplot(222)
    plotData(xys[1]['x'], xys[1]['y'])
    a, b, predicted = linearfitData(xys[1]['x'], xys[1]['y'])
    plotlinearfitData(a, xys[1]['x'], predicted)   
    plt.title('Sample2')
    
    plt.subplot(223)
    plotData(xys[2]['x'], xys[2]['y'])
    a, b, predicted = linearfitData(xys[2]['x'], xys[2]['y'])
    plotlinearfitData(a, xys[2]['x'], predicted) 
    plt.title('Sample3')
        
    plt.subplot(224)
    plotData(xys[3]['x'], xys[3]['y'])
    a, b, predicted = linearfitData(xys[3]['x'], xys[3]['y'])
    plotlinearfitData(a, xys[3]['x'], predicted) 
    plt.title('Sample4')
    
    plt.show()
    
def printmorefig(xys):
    '''
    print more
    '''
    fig = plt.figure(figsize = (16,7))
    n = len(xys)
    a, b = divmod(n,2)
    if b==0:
        for i in range(n):
            plt.subplot(2, 2, i+1)             #中间参数写a就报错？？？
            plotData(xys[i]['x'], xys[i]['y'])
            a, b, predicted = linearfitData(xys[i]['x'], xys[i]['y'])
            plotlinearfitData(a, xys[i]['x'], predicted)
            r = 'Sample' + str(i+1)
            plt.title(r)       
    else:
        for i in range(n):
            plt.subplot(2, a+1, i+1)    
            plotData(xys[i]['x'], xys[i]['y'])
            a, b, predicted = linearfitData(xys[i]['x'], xys[i]['y'])
            plotlinearfitData(a, xys[i]['x'], predicted)           
            r = 'Sample' + str(i+1)
            plt.title(r) 
            
    plt.show()
    
       
'''
def printmorefig(xys):
    ''''''
    n = len(xys)
    a, b = divmod(n,4)
    for i in range(a):
        plt.figure(i)
        if a>i or b==0:
            plt.subplot(221)
            plotData(xys[0]['x'], xys[0]['y'])
            a, b, predicted = linearfitData(xys[0]['x'], xys[0]['y'])
            plotlinearfitData(a, xys[0]['x'], predicted)           
    
            plt.subplot(222)
            plotData(xys[1]['x'], xys[1]['y'])
            a, b, predicted = linearfitData(xys[1]['x'], xys[1]['y'])
            plotlinearfitData(a, xys[1]['x'], predicted)   
    
            plt.subplot(223)
            plotData(xys[2]['x'], xys[2]['y'])
            a, b, predicted = linearfitData(xys[2]['x'], xys[2]['y'])
            plotlinearfitData(a, xys[2]['x'], predicted) 
        
            plt.subplot(224)
            plotData(xys[3]['x'], xys[3]['y'])
            a, b, predicted = linearfitData(xys[3]['x'], xys[3]['y'])
            plotlinearfitData(a, xys[3]['x'], predicted) 
        elif b==0:
            plt.subplot(221)
            plotData(xys[0]['x'], xys[0]['y'])
            a, b, predicted = linearfitData(xys[0]['x'], xys[0]['y'])
            plotlinearfitData(a, xys[0]['x'], predicted)           
    
            plt.subplot(222)
            plotData(xys[1]['x'], xys[1]['y'])
            a, b, predicted = linearfitData(xys[1]['x'], xys[1]['y'])
            plotlinearfitData(a, xys[1]['x'], predicted)   
    
            plt.subplot(223)
            plotData(xys[2]['x'], xys[2]['y'])
            a, b, predicted = linearfitData(xys[2]['x'], xys[2]['y'])
            plotlinearfitData(a, xys[2]['x'], predicted) 
        
            plt.subplot(224)
            plotData(xys[3]['x'], xys[3]['y'])
            a, b, predicted = linearfitData(xys[3]['x'], xys[3]['y'])
            plotlinearfitData(a, xys[3]['x'], predicted) 
        elif b==1:
            plt.subplot(221)                 
            plotData(xys[0]['x'], xys[0]['y'])
            a, b, predicted = linearfitData(xys[0]['x'], xys[0]['y'])
            plotlinearfitData(a, xys[0]['x'], predicted)           
        elif b==2:
            plt.subplot(221)
            plotData(xys[0]['x'], xys[0]['y'])
            a, b, predicted = linearfitData(xys[0]['x'], xys[0]['y'])
            plotlinearfitData(a, xys[0]['x'], predicted)           
    
            plt.subplot(222)
            plotData(xys[1]['x'], xys[1]['y'])
            a, b, predicted = linearfitData(xys[1]['x'], xys[1]['y'])
            plotlinearfitData(a, xys[1]['x'], predicted) 
        elif b==3:
            plt.subplot(221)
            plotData(xys[0]['x'], xys[0]['y'])
            a, b, predicted = linearfitData(xys[0]['x'], xys[0]['y'])
            plotlinearfitData(a, xys[0]['x'], predicted)           
    
            plt.subplot(222)
            plotData(xys[1]['x'], xys[1]['y'])
            a, b, predicted = linearfitData(xys[1]['x'], xys[1]['y'])
            plotlinearfitData(a, xys[1]['x'], predicted)   
    
            plt.subplot(223)
            plotData(xys[2]['x'], xys[2]['y'])
            a, b, predicted = linearfitData(xys[2]['x'], xys[2]['y'])
            plotlinearfitData(a, xys[2]['x'], predicted) 
'''                   
            