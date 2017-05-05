#coding=utf-8

from sklearn import preprocessing
import numpy as np
import os

#Usage: navallo@navallo-P65xRP:~/Documents/CODE/news2img$ python final_prediction.py 
def predict_list(text_vec):
	prediction_dict = {}
	for img_id in img_vec_dict:
		cos_dis = sum(text_vec * img_vec_dict[img_id])
		prediction_dict[img_id] = cos_dis
	return sorted(prediction_dict.items(), key=lambda x:x[1], reverse = True)

if __name__ == '__main__':

	#read img vecs
	img_vectors = open('./data/img_vectors.txt', 'r')
	print('img_vectors opened')
	img_lines = img_vectors.readlines()
	img_vec_dict = {}
	img_name_dict = {}

	for img_line in img_lines:
		name = img_line.split(':')[0]
		id = name.split('.')[0]
		img_vec = np.array(img_line.split(':')[1].split(',')[0:-1],dtype=float)
		if(len(img_vec) != 250):
			print('len != 250, id = %s'%id)
			continue
		img_vec = preprocessing.normalize(img_vec.reshape((1, -1)), norm='l2')[0]
		img_vec_dict[id] = img_vec
		img_name_dict[id] = name
	img_vectors.close()
	print('img_dict established')
	

	#read text vecs
	all_vectors = open('./data/text_vectors.txt', 'r')
	final_prediction = open('./data/final_prediction.txt', 'w')
	print('text_vectors opened')
	text_lines = all_vectors.readlines()

	count_file = 1
	for text_line in text_lines:
		id = text_line.split(',')[0]
		final_prediction.write(str(id)+'.txt')
		text_vec = np.array(text_line.split(',')[1:-1],dtype=float)
		text_vec = preprocessing.normalize(text_vec.reshape((1, -1)), norm='l2')[0]
		predction = predict_list(text_vec)
		for pred in predction[0:10]:
			final_prediction.write(',')
			final_prediction.write(img_name_dict[pred[0]])
#			print(pred[0])
#		if count_file > 3:
#			break
		final_prediction.write('\n')
		print('Predicted %s texts'%count_file)
		count_file = count_file + 1

	all_vectors.close()
	final_prediction.close()