from ReadData import *
from sklearn import linear_model
import matplotlib.pyplot as plt

def linear_model_main(x, y, predict_value):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    X_parameters = []
    for i in x:
        X_parameters.append([i])
    Y_parameters = y
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions


# Function to show the resutls of linear fit model
def show_linear_line(x, y):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    X_parameters = []
    for i in x:
        X_parameters.append([i])
    Y_parameters = y
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()