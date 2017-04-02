import numpy as np


result = []

def analysis(xys):
    # Average of each list
    n = len(xys) 
    for i in range (n):
        result.append({'x_average':np.mean(xys[i]['x']),
                       'y_average':np.mean(xys[i]['y']),
                       'x_variance':np.var(xys[i]['x']),
                       'y_variance':np.var(xys[i]['y']),
                       'xy_corrcoef':np.corrcoef(xys[i]['x'], xys[i]['y'])[0][1]})
    



def linearfitData(x, y):
    X = np.array(x)
    Y = np.array(y)
    a,b = np.polyfit(X, Y, 1)
    predicted = a*X + b
    
    return a,b,predicted
