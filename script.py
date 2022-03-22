import tensorflow as tf

w = tf.Variable([[1.], [2.]])
x = tf.constant([[3., 4.]])
print(tf.matmul(w, x))