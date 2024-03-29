# COMPARATIVE ANALYSIS OF ML APPROACHES ON THE PREDICTION OF THE ELECTRONIC PROPERTIES OF PEROVSKITE: A CASE STUDY OF THE ABX3 AND A2BB'X6 STRUCTURES

# AUTHOR - (1) * Ericsson Chenebuah, (1) Michel Nganbe and (2) Alain Tchagang 
# 1: Department of Mechanical Engineering, University of Ottawa, 75 Laurier Ave. East, Ottawa, ON, K1N 6N5 Canada
# 2: Digital Technologies Research Centre, National Research Council of Canada, 1200 Montréal Road, Ottawa, ON, K1A 0R6 Canada
# * email: echen013@uottawa.ca 
# (15-Nov-2020)

import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
%matplotlib inline 
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn import ensemble
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV 
# Best Hyperparameters identified using GridSearchCV with only ideal arguments implemented in all models


df = pd.read_csv('combine.csv') #Combined ABX3 and A2BB'X6 Perovskite Structures.
X=df.drop("Eg",1)
df['Eg'] = df['Eg'].astype('float64') 
y = np.asarray(df['Eg']) # Code simulated for predicting the energy bandgap.

# Model 1 - Gradient boosting regression (GBR)
from sklearn.ensemble import GradientBoostingRegressor
X_train1, X_test1, y_train1, y_test1 = train_test_split( X, y, test_size=0.1, random_state=9)
gbr = GridSearchCV (GradientBoostingRegressor (),{
    'n_estimators': [2000], 'max_depth': [2], 'min_samples_split': [2], 'learning_rate': [0.1],
    'loss': ['ls'], 'random_state':[72]}, cv=5)
gbr.fit(X_train1, y_train1)
y_predicted1 = gbr.predict(X_test1)
gbr_score = gbr.score(X_train1,y_train1)
gbr_score1 = gbr.score(X_test1,y_test1)

# Model 2 - Kernel Ridge Regression (KRR)
from sklearn.kernel_ridge import KernelRidge
X_train2, X_test2, y_train2, y_test2 = train_test_split( X, y, test_size=0.1, random_state=9)
krr = GridSearchCV (KernelRidge (),{ 'alpha':[0.001],'kernel':['linear']}, cv=5)
krr.fit(X_train2, y_train2)
y_predicted2 = krr.predict(X_test2)
krr_score = krr.score(X_train2,y_train2)
krr_score1 = krr.score(X_test2,y_test2)

# Model 3 - Support Vector Regression (SVR)
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
X_train3, X_test3, y_train3, y_test3 = train_test_split( X, y, test_size=0.1, random_state=10)
steps = [('scaler', StandardScaler()), ('SVM', SVR())]
pipeline = Pipeline(steps) 
grid = GridSearchCV(pipeline, param_grid= {'SVM__C':[100], 'SVM__gamma':['auto'], 'SVM__kernel': ['rbf'],
                                           'SVM__epsilon':[0.001]}, cv=5)
grid.fit(X_train3, y_train3)
svr_score = grid.score(X_train3,y_train3)
svr_score1 = grid.score(X_test3,y_test3)
y_predicted3 = grid.predict(X_test3)

# Model 4 - Decision Tree Regression (DTR)
from sklearn.tree import DecisionTreeRegressor
X_train4, X_test4, y_train4, y_test4 = train_test_split( X, y, test_size=0.1, random_state=9)
dtr = GridSearchCV (DecisionTreeRegressor(),{
    'criterion':['friedman_mse'], 'random_state':[72], 'splitter':['best'], 'max_depth':[None]}, cv=5)
dtr.fit(X_train4, y_train4)
dtr_score = dtr.score(X_train4,y_train4)
dtr_score1 = dtr.score(X_test4,y_test4)
y_predicted4 = dtr.predict(X_test4)

# Model 5 - AdaBoost Regression (ABR)
from sklearn.ensemble import AdaBoostRegressor
X_train5, X_test5, y_train5, y_test5 = train_test_split( X, y, test_size=0.1, random_state=9)
abr = GridSearchCV (AdaBoostRegressor (),{
    'random_state':[0], 'n_estimators':[1000], 'learning_rate':[0.001], 'loss': ['exponential']}, cv=5)
abr.fit(X_train5, y_train5)
abr_score = abr.score(X_train5,y_train5)
abr_score1 = abr.score(X_test5,y_test5)
y_predicted5 = abr.predict(X_test5)

# Model 6 - Bayesian Ridge (BR)
from sklearn import linear_model
X_train6, X_test6, y_train6, y_test6 = train_test_split( X, y, test_size=0.1, random_state=9)
br = GridSearchCV (linear_model.BayesianRidge(),{'tol':[1e-3]}, cv=5)
br.fit(X_train6, y_train6)
br_score = br.score(X_train6,y_train6)
br_score1 = br.score(X_test6,y_test6)
y_predicted6 = br.predict(X_test6)

# Model 7 - Multilayer Perceptron (MLP)
from sklearn.neural_network import MLPRegressor
X_train7, X_test7, y_train7, y_test7 = train_test_split( X, y, test_size=0.1, random_state=9)
mlp = GridSearchCV (MLPRegressor (),{
    'random_state':[0], 'max_iter':[10000], 'alpha':[0.001],}, cv=5)
mlp.fit(X_train7, y_train7)
mlp_score = mlp.score(X_train7,y_train7)
mlp_score1 = mlp.score(X_test7,y_test7)
y_predicted7 = mlp.predict(X_test7)

# Model 8 - Random Forest Regression (RFR)
from sklearn.ensemble import RandomForestRegressor
X_train8, X_test8, y_train8, y_test8 = train_test_split( X, y, test_size=0.1, random_state=9)
rfr = GridSearchCV (RandomForestRegressor(),{'max_depth':[None], 'random_state':[0], 'criterion':['mse']
                                             }, cv=5)
rfr.fit(X_train8, y_train8)
rfr_score = rfr.score(X_train8,y_train8)
rfr_score1 = rfr.score(X_test8,y_test8)
y_predicted8 = rfr.predict(X_test8)

# Model 9 - K-Nearest Neighbor (KNR)
from sklearn.neighbors import KNeighborsRegressor
X_train9, X_test9, y_train9, y_test9 = train_test_split( X, y, test_size=0.1, random_state=9)
knr = GridSearchCV (KNeighborsRegressor(),{'n_neighbors':[4]}, cv=5)
knr.fit(X_train9, y_train9)
knr_score = knr.score(X_train9,y_train9)
knr_score1 = knr.score(X_test9,y_test9)
y_predicted9 = knr.predict(X_test9)

# Model 10 - Passive Aggressive Regression (PAR)
from sklearn.linear_model import PassiveAggressiveRegressor
X_train10, X_test10, y_train10, y_test10 = train_test_split( X, y, test_size=0.1, random_state=9)
par = GridSearchCV (PassiveAggressiveRegressor(),{'max_iter':[1000], 'random_state':[10], 'tol':[1e-10]},
                   cv=5)
par.fit(X_train10, y_train10)
par_score = par.score(X_train10,y_train10)
par_score1 = par.score(X_test10,y_test10)
y_predicted10 = par.predict(X_test10)

# Model 11 - Gaussian Process Regression (GPR)
from sklearn.gaussian_process import GaussianProcessRegressor
X_train11, X_test11, y_train11, y_test11 = train_test_split( X, y, test_size=0.1, random_state=7)
gpr = GridSearchCV (GaussianProcessRegressor(), {}, cv=5)
gpr.fit(X_train11, y_train11)
gpr_score = gpr.score(X_train11,y_train11)
gpr_score1 = gpr.score(X_test11,y_test11)
y_predicted11 = gpr.predict(X_test11)

# Model 12 - Stochastic Gradient Descent (SGD)
from sklearn.linear_model import SGDRegressor
X_train12, X_test12, y_train12, y_test12 = train_test_split( X, y, test_size=0.1, random_state=9)
sgd = (make_pipeline(StandardScaler(),SGDRegressor(max_iter=1000,tol=1e-1500,alpha=0.0001,epsilon=0.0001)))
sgd.fit(X_train12, y_train12)
sgd_score = sgd.score(X_train12,y_train12)
sgd_score1 = sgd.score(X_test12,y_test12)
y_predicted12 = sgd.predict(X_test12)

# Standard Accuracy Results
print('GBR Model| R2 sq on train set: %.4f'% gbr_score)
print('GBR Model| R2 sq on test set: %.4f'% gbr_score1)
print("GBR Model| MSE on test set: %.4f"% mean_squared_error(y_test1, y_predicted1))
print("GBR Model| MAE on test set: %.4f"% mean_absolute_error(y_test1, y_predicted1))
print ("---------------------------------")
print('KRR Model| R2 sq on train set: %.4f'% krr_score)
print('KRR Model| R2 sq on test set: %.4f'% krr_score1)
print('KRR Model| MSE on test set: %.4f'% mean_squared_error(y_test2, y_predicted2))
print('KRR Model| MAE on test set: %.4f'% mean_absolute_error(y_test2, y_predicted2))
print ("---------------------------------")
print('SVR Model| R2 sq on train set: %.4f'% svr_score)
print('SVR Model| R2 sq on test set: %.4f'% svr_score1)
print('SVR Model| MSE on test set: %.4f'% mean_squared_error(y_test3, y_predicted3))
print('SVR Model| MAE on test set: %.4f'% mean_absolute_error(y_test3, y_predicted3))
print ("---------------------------------")
print('DTR Model| R2 sq on train set: %.4f'% dtr_score)
print('DTR Model| R2 sq on test set: %.4f'% dtr_score1)
print('DTR Model| MSE on test set: %.4f'% mean_squared_error(y_test4, y_predicted4))
print('DTR Model| MAE on test set: %.4f'% mean_absolute_error(y_test4, y_predicted4))
print ("---------------------------------")
print('ABR Model| R2 sq on train set: %.4f'% abr_score)
print('ABR Model| R2 sq on test set: %.4f'% abr_score1)
print('ABR Model| MSE on test set: %.4f'% mean_squared_error(y_test5, y_predicted5))
print('ABR Model| MAE on test set: %.4f'% mean_absolute_error(y_test5, y_predicted5))
print ("---------------------------------")
print('BR Model| R2 sq on train set: %.4f'% br_score)
print('BR Model| R2 sq on test set: %.4f'% br_score1)
print('BR Model| MSE on test set: %.4f'% mean_squared_error(y_test6, y_predicted6))
print('BR Model| MAE on test set: %.4f'% mean_absolute_error(y_test6, y_predicted6))
print ("---------------------------------")
print('MLP Model| R2 sq on train set: %.4f'% mlp_score)
print('MLP Model| R2 sq on test set: %.4f'% mlp_score1)
print('MLP Model| MSE on test set: %.4f'% mean_squared_error(y_test7, y_predicted7))
print('MLP Model| MAE on test set: %.4f'% mean_absolute_error(y_test7, y_predicted7))
print ("---------------------------------")
print('RFR Model| R2 sq on train set: %.4f'% rfr_score)
print('RFR Model| R2 sq on test set: %.4f'% rfr_score1)
print('RFR Model| MSE on test set: %.4f'% mean_squared_error(y_test8, y_predicted8))
print('RFR Model| MAE on test set: %.4f'% mean_absolute_error(y_test8, y_predicted8))
print ("---------------------------------")
print('KNR Model| R2 sq on train set: %.4f'% knr_score)
print('KNR Model| R2 sq on test set: %.4f'% knr_score1)
print('KNR Model| MSE on test set: %.4f'% mean_squared_error(y_test9, y_predicted9))
print('KNR Model| MAE on test set: %.4f'% mean_absolute_error(y_test9, y_predicted9))
print ("---------------------------------")
print('PAR Model| R2 sq on train set: %.4f'% par_score)
print('PAR Model| R2 sq on test set: %.4f'% par_score1)
print('PAR Model| MSE on test set: %.4f'% mean_squared_error(y_test10, y_predicted10))
print('PAR Model| MAE on test set: %.4f'% mean_absolute_error(y_test10, y_predicted10))
print ("---------------------------------")
print('GPR Model| R2 sq on train set: %.4f'% gpr_score)
print('GPR Model| R2 sq on test set: %.4f'% gpr_score1)
print('GPR Model| MSE on test set: %.4f'% mean_squared_error(y_test11, y_predicted11))
print('GPR Model| MAE on test set: %.4f'% mean_absolute_error(y_test11, y_predicted11))
print ("---------------------------------")
print('SGD Model| R2 sq on train set: %.4f'% sgd_score)
print('SGD Model| R2 sq on test set: %.4f'% sgd_score1)
print('SGD Model| MSE on test set: %.4f'% mean_squared_error(y_test12, y_predicted12))
print('SGD Model| MAE on test set: %.4f'% mean_absolute_error(y_test12, y_predicted12))