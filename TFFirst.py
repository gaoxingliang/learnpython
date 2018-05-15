import math
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows=10
pd.options.display.float_format = '{:.1f}'.format

housedf = pd.read_csv("/Users/edward.gao/work/tensorflow/california_housing_train.csv")

housedf = housedf.reindex(np.random.permutation(housedf.index))
housedf["median_house_value"]/=1000.0
housedf.describe()

print("Describe finished.....")

my_eatures = housedf[["total_rooms"]]
feature_cols = [tf.feature_column.numeric_column("total_rooms")]

targets = housedf["median_house_value"]

optimzer = tf.train.GradientDescentOptimizer(learning_rate=0.000001)
optimzer = tf.contrib.estimator.clip_gradients_by_norm(optimzer, 5.0)

line_regressor = tf.estimator.LinearRegressor(
    feature_columns=feature_cols,
    optimizer=optimzer
)


def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    features = {key:np.array(value) for key,value in dict(features).items()}
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)
    features,labels = ds.make_one_shot_iterator().get_next()
    return features, labels


_ = line_regressor.train(input_fn=lambda :my_input_fn(my_eatures, targets),
                         steps=100)


pred_input_fn = lambda : my_input_fn(my_eatures, targets, num_epochs=1, shuffle=False)

preds = line_regressor.predict(input_fn=pred_input_fn)
preds = np.array([item["predictions"][0] for item in preds])
mean_square_error = metrics.mean_squared_error(preds, targets)
root_mean = math.sqrt(mean_square_error)
print("Mean squared error (on training data):" + str(mean_square_error))
