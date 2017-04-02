import matplotlib.pyplot as plt
import numpy as np
from Analysis import *

def printdata(xys):
    '''only print out the data'''
    n = len(xys)
    for i in range(n):
        print('x', i, '=', xys[i]['x'])
        print('y', i, '=', xys[i]['y'])


def printanalysis(xys, result):
    '''only print out the analysis result'''
    n = len(xys)
    for i in range(n):
        print(result[i])
            

def printall(xys, result):
    '''print out both the data and corresponding analysis result'''
    n = len(xys)
    for i in range(n):
        print('x', i, '=', xys[i]['x'])
        print('y', i, '=', xys[i]['y'])
        print(result[i], '\n')


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
    fig = plt.figure(figsize=(10,7))
    
    plt.subplot(221)
    plotData(xys[0]['x'], xys[0]['y'])
    a,b,predicted=linearfitData(xys[0]['x'], xys[0]['y'])
    plotlinearfitData(a,xys[0]['x'],predicted)     
    plt.title('Sample1')       
    
    plt.subplot(222)
    plotData(xys[1]['x'], xys[1]['y'])
    a,b,predicted=linearfitData(xys[1]['x'], xys[1]['y'])
    plotlinearfitData(a,xys[1]['x'],predicted)   
    plt.title('Sample2')
    
    plt.subplot(223)
    plotData(xys[2]['x'], xys[2]['y'])
    a,b,predicted=linearfitData(xys[2]['x'], xys[2]['y'])
    plotlinearfitData(a,xys[2]['x'],predicted) 
    plt.title('Sample3')
        
    plt.subplot(224)
    plotData(xys[3]['x'], xys[3]['y'])
    a,b,predicte=linearfitData(xys[3]['x'], xys[3]['y'])
    plotlinearfitData(a,xys[3]['x'],predicted) 
    plt.title('Sample4')
    
    plt.show()
