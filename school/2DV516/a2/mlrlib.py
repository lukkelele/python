import numpy as np

    # two columns
def normalize_matrix(X):
    x0_col, x1_col = X[:,0], X[:,1]
    x0_std, x1_std = np.std(x0_col), np.std(x1_col)
    x0_mean, x1_mean = np.mean(x0_col), np.mean(x1_col)
    x0_subt, x1_subt = np.subtract(x0_col, x0_mean), np.subtract(x1_col, x1_mean)
    x0_norm, x1_norm = np.divide(x0_subt, x0_std), np.divide(x1_subt, x1_std) 
    Xn = np.concatenate((x0_norm.reshape(len(x0_col), 1), x1_norm.reshape(len(x0_col), 1)), axis=1)
    return Xn

    # x is the value to be normalized
    # X is the column which holds values of same kind
def normalize_val(x, X):
    x_mean = np.mean(X)
    x_std = np.std(X)
    x_norm = (x-x_mean)/x_std
    return x_norm

def extend_matrix(n, X):
    return np.c_[np.ones((n, 1)), X]

    # Normal equation
def calc_beta(Xe, y):
    B = np.linalg.inv(Xe.T.dot(Xe)).dot(Xe.T).dot(y)
    return B

def calc_j(Xe, y, beta):
    j = np.dot(Xe, beta) - y
    return j

# Cost function
def calc_cost(j, n):
    J = (j.T.dot(j)) / n
    return J

def calc_height(beta, x0, x1):
    height = beta[0] + beta[1]*x0 + beta[2]*x1
    return height
