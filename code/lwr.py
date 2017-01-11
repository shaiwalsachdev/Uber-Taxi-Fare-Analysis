#Locally Weighted Regression fro Input is of > 1 dimension
import numpy as np

def gaussian_kernel(x, x0, c, a=1.0):
    """
    Gaussian kernel.

    :Parameters:
      - `x`: nearby datapoint we are looking at.
      - `x0`: data point we are trying to estimate.
      - `c`, `a`: kernel parameters.
    """
    # Euclidian distance
    diff = x - x0
    dot_product = diff * diff.T
    return a * np.exp(dot_product / (-2.0 * c**2))


def get_weights(training_inputs, datapoint, c=1.0):
    """
    Function that calculates weight matrix for a given data point and training
    data.

    :Parameters:
      - `training_inputs`: training data set the weights should be assigned to.
      - `datapoint`: data point we are trying to predict.
      - `c`: kernel function parameter

    :Returns:
      NxN weight matrix, there N is the size of the `training_inputs`.
    """
    x = np.mat(training_inputs)
    n_rows = x.shape[0]
    # Create diagonal weight matrix from identity matrix
    weights = np.mat(np.eye(n_rows))
    for i in xrange(n_rows):
        weights[i, i] = gaussian_kernel(datapoint, x[i], c)

    return weights


def lwr_predict(training_inputs, training_outputs, datapoint, c=1.0):
    """
    Predict a data point by fitting local regression.

    :Parameters:
      - `training_inputs`: training input data.
      - `training_outputs`: training outputs.
      - `datapoint`: data point we want to predict.
      - `c`: kernel parameter.

    :Returns:
      Estimated value at `datapoint`.
    """
    weights = get_weights(training_inputs, datapoint, c=c)

    x = np.mat(training_inputs)
    y = np.mat(training_outputs).T
    print weights
    xt = x.T * (weights * x)
    betas = xt.I * (x.T * (weights * y))

    return datapoint * betas

x= []
x.append((1,0))
x.append((3,1))
x.append((6,0))
x.append((7,0))
y = []
y.append(9)
y.append(8)
y.append(1)
y.append(4)

print lwr_predict(x,y,8)