from matplotlib.colors import ListedColormap
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
import pandas as pd
import numpy as np
import sys
import ml

np.set_printoptions(threshold=sys.maxsize)

"""
Total of 9 features and the 10th column contains binary labels of either 2 (0) or 4 (1)
"""
data = ml.open_csv_file('./data/breast_cancer.csv')

def run(data, N, a, i, train_p, output=False):
    X, y = data[:,[0,1,2,3,4,5,6,7,8]], data[:,9]
    # Replace y values of 2 and 4 to 0 and 1 respectively
    y = np.where(y == 2, 0, 1) 
    # Normalize and extend data
    Xn = ml.normalize_matrix(X)
    Xne = ml.extend_matrix(Xn)
    # Divide data to training and testing sets
    train_percentage = train_p
    train_size = round(train_percentage * len(X))
    test_size = len(X) - train_size
    X_train, X_test = Xne[:train_size], Xne[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    # Train a linear logistic regression model
    beta, betas = ml.log_gradient_descent(X_train, y_train, iterations=N, learning_rate=a)
    # Plot cost function
    if i == 0:
        print('>> Plotting single cost function')
        plt.subplot(111)
        plt.title('Cost function\nLearning rate: %f\nIterations: %d' % (a, N))
        plt.xlim([0, N])
        ml.log_plot_cost(X_train, y_train, betas)
    # Training errors and accuracy in the training data set
    training_errors = ml.log_estimate_errors(X_train, y_train, beta)
    correct_train = train_size - training_errors
    training_accuracy = round(100*(correct_train/train_size), 3)
    # Test errors and accuracy in the test data set
    test_errors = ml.log_estimate_errors(X_test, y_test, beta)
    correct_test = test_size - test_errors 
    test_accuracy = round(100 * (correct_test/test_size), 3)
    if output: print(f"""[ROUND] {i}
    >> TRAINING         |       TEST
       Errors:   {training_errors}          Errors:   {test_errors}
       Accuracy: {training_accuracy}%     Accuracy: {test_accuracy}% 
------------------------------------------------------------------------""")
    return training_errors, test_errors, training_accuracy, test_accuracy

# Divide data to training and testing sets
train_percentage = 0.80
train_size = round(train_percentage * len(data))
test_size = len(data) - train_size
print(f"""
>> DATA SETS
   Training => {train_size} instances, {round(train_percentage*100, 3)}% 
   Test     => {test_size} instances, {round((1-train_percentage)*100, 3)}%""")

avg_train_err, avg_test_err, avg_train_acc, avg_test_acc = 0, 0, 0, 0
results = []

K = 10
N = 5000
a = 0.010
output=True

for i in range(K):
    np.random.shuffle(data)
    results.append(run(data, N=N, a=a, i=i, train_p=train_percentage, output=output))

for result in results:
    train_err, test_err = result[0], result[1]
    train_acc, test_acc = result[2], result[3]
    avg_train_err += train_err
    avg_train_acc += train_acc
    avg_test_err += test_err
    avg_test_acc += test_acc

avg_train_err = round(avg_train_err / K, 7)
avg_test_err = round(avg_test_err / K, 7)
avg_train_acc = round(avg_train_acc / K, 7)
avg_test_acc = round(avg_test_acc / K, 7)

print(f"""   \nAVERAGE RESULTS {K} rounds
    >> TRAINING          |     TEST
       Errors:   {avg_train_err}          Errors:   {avg_test_err}
       Accuracy: {avg_train_acc}%     Accuracy: {avg_test_acc}% 
------------------------------------------------------------------------""")
print('>> The results are very similar during the repeated runs.')
print('   The difference is to be expected. On average the test results is expected to be a bit lower than the test results.')
print('   A low training set can get good scores on the training data but fail to classify the test data.')
print('   But using all the data for training the model does not make the testing viable because there just isn\'t enough data to test.')
print('   Therefore using 80/20 for splitting the data for the training and test sets is a good choice.')
plt.show()
