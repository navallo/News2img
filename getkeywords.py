#-*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import re
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
#import tarfile
import os

import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence


#usage: (tensorflow2) navallo@navallo-P65xRP:~/Documents/CODE/news2img$ python getkeywords.py /home/navallo/Documents/DATA/formalCompetition4/News_info_validate/


def main(argv):
	all_keywords = open('./data/text_keywords.txt', 'w')
	count = 0

	for root, dirs, files in os.walk(str(argv[1]), topdown=False):
		for name in files:
			txt_dir = (os.path.join(str(argv[1]), name))

			text = codecs.open(txt_dir, 'r', 'utf-8').read()
			tr4w = TextRank4Keyword()

			tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

			count = count + 1
			print(count, end=' :')
			print(name+',', end='')
			all_keywords.write(name+';')
			weight_sum = 0
			for item in tr4w.get_keywords(20, word_min_len=1):
				if len(item.word.encode('utf-8')) != 3:
					print(item.word.encode('utf-8'), end=',')
					weight_sum = weight_sum + item.weight

					all_keywords.write(item.word.encode('utf-8')+',')
					all_keywords.write(str(item.weight).encode('utf-8')+';')
			all_keywords.write(str(weight_sum).encode('utf-8'))
##			print( '关键词：' )
##			for item in tr4w.get_keywords(20, word_min_len=1):
##				print(item.word.encode('utf-8'), item.weight)
			print()
			all_keywords.write('\n')

	all_keywords.close()
	
if __name__ == '__main__':
	main(sys.argv)