# -*- coding: utf-8 -*-
# @Date  : 2019/3/29 13:44
# @Software : PyCharm
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np


# 生成整数型的属性
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


# 生成字符串型的属性
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


mnist = input_data.read_data_sets('./path/to/mnist/data', dtype=tf.uint8, one_hot=True)
images = mnist.train.images

# 训练数据所对应的正确答案, 可以作为一个属性保存在TFRecord中.
labels = mnist.train.labels

# 训练数据的图像分辨率,这可以作为Example中的一个属性
pixels = images.shape[1]
num_examples = mnist.train.num_examples

# 输出TFRecord文件的地址
filename = './path/to/output.tfrecords'
# 创建一个writer来写TFRecord文件
writer = tf.python_io.TFRecordWriter(filename)
for index in range(num_examples):
    # 将图像矩阵转化成一个字符串
    image_raw = images[index].tostring()
    # 将一个样例转化为Example Protocol Buffer,并将所有的信息写入这个数据结构
    example = tf.train.Example(features=tf.train.Features(feature={
        'pixels': _int64_feature(pixels),
        'label': _int64_feature(np.argmax(labels[index])),
        'image_raw': _bytes_feature(image_raw)
    }))

    writer.write(example.SerializeToString())
writer.close()
