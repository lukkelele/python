from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
from sklearn.neural_network import MLPClassifier
from matplotlib.ticker import MultipleLocator
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from matplotlib import colors
from math import sqrt, floor
from sklearn.svm import SVC
import numpy as np
import sys
import ml

#np.set_printoptions(threshold=sys.maxsize)

# Fashion MNIST
# Image classification
np.random.seed(5)

train_data, test_data = ml.open_csv_file('./data/fashion-mnist_train.csv'), \
                        ml.open_csv_file('./data/fashion-mnist_test.csv')
# Number of features used to slice data
f_idx = train_data.shape[1]
train_size = 0.12
test_size = train_size * 0.20
train_samples, test_samples = len(train_data), len(test_data)
new_train_size, new_test_size = round(train_size * train_samples), \
                                round(test_size * test_samples)
# Split the data, label on column 0
train_data, test_data = train_data[:new_train_size], test_data[:new_test_size]
X_train, X_test, y_train, y_test = train_data[:, 1:f_idx], test_data[:, 1:f_idx],\
                                   train_data[:,0],  test_data[:,0]
print(">> Dataset sizes\n   Training set: %d samples, %d%% of entire training set" \
                                              % (new_train_size, 100*train_size))
print("   Test set: %d samples, %d%% of entire test set" \
                        % (new_test_size, 100*test_size))
# Train classifier
clf = MLPClassifier()
clf.fit(X_train, y_train)
validation_score_mean = cross_val_score(clf, X_test, y_test).mean()
print(validation_score_mean)

# Generate 16 random numbers to be used as indexes for random sampling
random_samples = np.random.random_integers(0, new_train_size, size=(16,))
#print(f">> Random sample idx: \n{random_samples}")

print(y_train[5])
# Plot 16 random samples from the training set
errors = 0
for i in range(16):
    plt.subplot(4,4,i+1)
    idx = random_samples[i]
    sample = X_train[idx].reshape(1, -1)
    y_pred = clf.predict(sample)[0]
    if y_pred != y_train[idx]:
        errors += 1
        plt.title(f"{i+1}. WRONG")
    else:
        plt.title(f"{i+1}. CORRECT")
    plt.imshow(sample.reshape(28,28), cmap='gray')


plt.show()