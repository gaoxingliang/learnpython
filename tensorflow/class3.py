# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:36:51 2018

@author: gaoxi
"""

import tensorflow as tf
w = tf.Variable([[0.5, 1.0]])
print(w)
x = tf.Variable([[2.0], [1.0]])
y = tf.matmul(w,x)
print(y)

init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(y.eval())