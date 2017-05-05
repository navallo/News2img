#-*- encoding:utf-8 -*-

import os.path
import re
import sys
try:
	reload(sys)
	sys.setdefaultencoding('utf-8')
except:
	pass
import os


def main(argv):
	for root, dirs, files in os.walk(str(argv[1]), topdown=False):
		for name in files:
			print name
			txt_dir = (os.path.join(str(argv[1]),name))
			with open(txt_dir,'r') as r:
				lines=r.read()
			r.close()
			with open(txt_dir,'w') as w:
				w.write(lines.replace(lines.split('\t')[0],''))
			w.close()

'''
			lines = codecs.open(txt_dir, 'r', 'utf-8').readlines()
			for line in lines:
				word = line.split('\t')[2]
				print(word)
'''		

if __name__ == '__main__':
	main(sys.argv)