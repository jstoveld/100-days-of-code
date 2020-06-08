#Make necessary imports
import quandl
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split


#Get Amazon stock data
BA = quandl.get("WIKI/BA")
print(BA.head())


#Get only the data for the Adjusted Close column
BA = BA[['Adj. Close']]
print(BA.head())


#Predict for 30 days; Predicted has the data of Adj. Close shifted up by 30 rows
forecast_len=30
BA['Predicted'] = BA[['Adj. Close']].shift(-forecast_len)
print(BA.tail())


#Drop the Predicted column, turn it into a NumPy array to create dataset
x=np.array(BA.drop(['Predicted'],1))
#Remove last 30 rows
x=x[:-forecast_len]
print(x)


#Create dependent dataset for predicted values, remove the last 30 rows
y=np.array(BA['Predicted'])
y=y[:-forecast_len]
print(y)


#Split datasets into training and test sets (80% and 20%)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


#Create SVR model and train it
svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1) 
svr_rbf.fit(x_train,y_train)


#Get score
svr_rbf_confidence=svr_rbf.score(x_test,y_test)
print(f"SVR Confidence: {round(svr_rbf_confidence*100,2)}%")


#Create Linear Regression model and train it
lr=LinearRegression()
lr.fit(x_train,y_train)


#Get score for Linear Regression
lr_confidence=lr.score(x_test,y_test)
print(f"Linear Regression Confidence: {round(lr_confidence*100,2)}%")