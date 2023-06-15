import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/Badhri/Downloads/data1.csv")
data.head()

shuffle_data = data.sample(frac=1)
train_size = int(0.7 * len(data))
train_set = shuffle_data[:train_size]
test_set = shuffle_data[train_size:]

x_train = train_set['x']
x_test = test_set['x']
y_train = train_set['y']
y_test = test_set['y']
x_train

def simple_linear_regression(input_feature,output):
    Xi = input_feature
    Yi = output
    N = len(Xi)
    
    Yi_mean = Yi.mean()
    Xi_mean = Xi.mean()
    
    sum_YiXi = (Yi*Xi).sum()
    Yi_Xi_ByN = (Yi.sum() * Xi.sum()) / N
    
    sum_XiXi = (Xi*Xi).sum()
    XiXi_ByN = (Xi.sum() * Xi.sum()) / N
    
    slope = (sum_YiXi - Yi_Xi_ByN) / (sum_XiXi - XiXi_ByN)
    
    intercept = Yi_mean - slope * Xi_mean
    
    return (intercept,slope)

train_intercept , train_slope = simple_linear_regression(x_train,y_train)

print ("Intercept",train_intercept)
print ("Slope",train_slope)

print ("Y =",train_intercept,"*X +",train_slope)

plt.scatter(x_train,y_train,color='blue')
plt.plot(x_train,train_slope*x_train+train_intercept,'black')
plt.xlabel("X")
plt.ylabel("Y")

def get_regression_predictions(input_features,intercept,slope):
    predicted_values = input_features*slope + intercept
    
    return predicted_values

y_pred = get_regression_predictions(x_test,train_intercept,train_slope)
y_pred[:5]

y_test[:5]

def R_Mean_Squared(y_test,y_pred):
    
    residual = y_test - y_pred
    
    RES = (residual*residual).mean()
    
    return (RES**(0.5))

R_Mean_Squared(y_test,y_pred)

from sklearn.metrics import r2_score
r2_score(y_test,y_pred)
