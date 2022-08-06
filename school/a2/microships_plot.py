from matplotlib import pyplot as plt
import numpy as np
import ml


data = ml.open_csv_file('./data/microchips.csv')
X1, X2, y = data[:,0], data[:,1], data[:,2]
Xn = ml.normalize_matrix(np.c_[X1, X2])
Xn1, Xn2 = Xn[:, 0], Xn[:, 1]
Xn_e = ml.extend_matrix(Xn)
Xn_ep = ml.polynomial(Xn1, Xn2, 4)
beta = ml.log_gradient_descent(Xn_ep, y)
ml.plot_nonlinear_db(Xn1, Xn2, y, beta, d=4)


plt.show()
