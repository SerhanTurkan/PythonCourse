#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats

def linear_regression(X, y):
    Beta,error, t1, t2 = None, None, None, None

    # for handling NaN values
    X_clean = X.dropna().to_numpy()
    y = y.dropna().to_numpy()

    # adding 1 to the X matrix for the intercept
    one_column = np.ones((X_clean.shape[0], 1))
    X = np.concatenate((one_column, X_clean), axis=1)
    
    # Beta
    Beta = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y))

    # Y_hat
    n = X.shape[1]
    h = np.ones((X.shape[0], 1))
    theta = Beta.reshape(1, n)
    for i in range(0, X.shape[0]):
        h[i] = float(np.matmul(theta, X[i]))
    y_hat = h.reshape(X.shape[0])

    # Residuals
    e = np.subtract(y, y_hat)
    ss_numerator = np.dot(e.T, e)
    sample_no = X.shape[0]
    denom = sample_no - n

    # Variance of Beta
    sigma_squared = np.true_divide(ss_numerator, denom)
    inverse = np.linalg.inv(np.dot(X.T, X))
    variance_B = np.dot(sigma_squared, inverse)
    var_B = np.diag(variance_B)

    # Standard error of Beta
    error = np.sqrt(var_B)

    # T-statistics
    t = stats.t.ppf(0.975, denom)
    t_part = t * error

    # Credible intervals (t2 upper and t1 lower)
    upper = np.add(theta, t_part)
    t2 = upper.reshape(-1, )
    lower = np.subtract(theta, t_part)
    t1 = lower.reshape(-1, )
    return Beta, error, t1, t2, X_clean, y

