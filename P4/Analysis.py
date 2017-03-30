from ReadData import *
import numpy as np

def avexy():
    # Average of each list
    print('Average of Each List:')
    for i in range (n):
        print('x', i, ' = ', np.mean(x[i]))
        print('y', i, ' = ', np.mean(y[i]))

def varxy():    
    # Varies of each list
    print('Varies of Each List:')
    for i in range (n):
        print('x', i, ' = ', np.var(x[i]))
        print('y', i, ' = ', np.var(y[i]))

def corrcoefxy():    
    # Correlation coefficient
    for i in range (n):
        c = np.corrcoef(x[i], y[i])
        print('Correlation coefficien of XY', i, ' is ', c[0][1])
