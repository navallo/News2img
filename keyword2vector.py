#-*- encoding:utf-8 -*-
from gensim.models import Word2Vec
from sklearn import preprocessing

import tensorflow as tf
import numpy
import os.path
import re
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass


#usage: navallo@navallo-P65xRP:~/Documents/word2vec_zh-master$ python keyword2vector.py 
model = Word2Vec.load('./data/my.model')
def v(target):
    try:
        vector = model.wv[target]
#        print(model['target'])
        return vector
    except:
        return -1

if __name__ == '__main__':
    all_keywords = open('./data/text_keywords.txt', 'r')
    all_vectors = open('./data/text_vectors.txt', 'w')
    lines = all_keywords.readlines()
    for line in lines:
        vector_sum = 0
        for item in line.split(';')[1:-1]:
            word = item.split(',')[0]
            weight = float(item.split(',')[1])

            if type(v(word)) != int:
                vector_sum = vector_sum + (v(word) * weight)
            else:
                vector_sum = vector_sum + numpy.zeros(250, dtype = float)

        vector_sum_normalized = preprocessing.normalize(vector_sum.reshape(1, -1), norm='l2')
#        vector_sum_normalized2 = tf.nn.l2_normalize(vector_sum,0)
##        print(line.split(';')[0])
#        print(vector_sum_normalized)
#        sess = tf.Session()
#        print(sess.run([vector_sum_normalized2]))
#        print(vector_sum_normalized - sess.run([vector_sum_normalized2]))
#        os._exit(0)
        all_vectors.write(line.split(';')[0].split('.')[0]+',')

        for tmp in vector_sum_normalized:
            for temp in tmp:
                all_vectors.write(str(temp)+',')
        all_vectors.write('\n')
#        os._exit(0)