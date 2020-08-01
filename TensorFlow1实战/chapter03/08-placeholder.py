# -*- coding: utf-8 -*-
# @Date  : 2019/3/19 22:03
# @Software : PyCharm


import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 定义placeholder作为存放输入数据的地方.这里维度也不一定要定义
# 但如果维度是确定的, 那么给出维度可以降低出错的概率
x = tf.placeholder(tf.float32, shape=[3, 2], name='input')
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(y, feed_dict={x: [[0.7, 0.9], [1.0, 2], [3, 4]]}))