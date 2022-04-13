import numpy as np



def extend_x(n, X):
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
    print(f"Cost J: {J}\nlength_J: {len(J)}")
    return J

def calc_height(beta, mom, dad):
    height = beta[0] + beta[1]*mom + beta[2]*dad
    print(height)
    return height
