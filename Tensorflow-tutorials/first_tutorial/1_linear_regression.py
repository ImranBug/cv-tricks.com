import tensorflow as tf
import numpy as np

trainX = np.linspace(-1, 1, 101)
trainY = 3 * trainX + np.random.randn(*trainX.shape) * 0.33

X = tf.placeholder("float")
Y = tf.placeholder("float")

w = tf.Variable(0.0, name="weights")
init = tf.initialize_all_variables()
#init= tf.global_variables_initializer() for new tf
y_model = tf.mul(X, w)

cost = (tf.pow(Y-y_model, 2))

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)



with tf.Session() as sess:
    sess.run(init)
    for i in range(100):
        for (x, y) in zip(trainX, trainY):
            sess.run(train_op, feed_dict={X: x, Y: y})
    print(sess.run(w))
