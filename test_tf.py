import tensorflow as tf

# b = tf.constant(3.0, tf.float32)
# a = tf.constant(4.0)

# c = a*b

# sess = tf.Session()
# File_Writer = tf.summary.FileWriter('./tf_graph',sess.graph)

# print(sess.run(c))
# sess.close()

# ----------------------------------------
# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)

# c = a+b

# with tf.Session() as sess:
	# print(sess.run(c,{a:[1,2],b:[3,4]}))

# ----------------------------------------

import tensorflow as tf

#model
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

#inps and outs
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

linear_model = W*x+b

sess = tf.Session()

#loss
squared_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_delta)


init = tf.global_variables_initializer()

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

session = tf.Session()

sess.run(init)

for i in range(1000):
	sess.run(train, {x:[1,2,3,4],y:[0,-1,-2,-3]})

print(sess.run([W,b]))
# print(sess.run(linear_model, {x:[1,2,3,4],y:[0,-1,-2,-3]}))