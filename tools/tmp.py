#-*- encoding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = open('all_keywords.txt')
out = open('all_keywords_norepeat.txt','w')
lines = data.readlines( )
for line in lines:
	words = line.split(':')[-1]
	word = words.split(',')
	for tmp in word:
		out.write(tmp+'\n')
		print(tmp)
data.close()
out.close()