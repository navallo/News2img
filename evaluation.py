#coding=utf-8

from sklearn import preprocessing
import numpy as np
import os

def predict_list(text_vec):
	prediction_dict = {}
	for img_id in img_vec_dict:
		cos_dis = sum(text_vec * img_vec_dict[img_id])
		prediction_dict[img_id] = cos_dis
	return sorted(prediction_dict.items(), key=lambda x:x[1], reverse = True)

if __name__ == '__main__':

	#read img vecs
	img_vectors = open('./data/img_vectors_1000.txt', 'r')
	print('img_vectors opened')
	img_lines = img_vectors.readlines()
	img_vec_dict = {}
	for img_line in img_lines:
		id = img_line.split(':')[0].split('.')[0]################ATTENTION!!!!!!!!!
		img_vec = np.array(img_line.split(':')[1].split(',')[0:-1],dtype=float)
		if(len(img_vec) != 250):
			print('len != 250, id = %s'%id)
			continue
		img_vec = preprocessing.normalize(img_vec.reshape((1, -1)), norm='l2')[0]
		img_vec_dict[id] = img_vec
	img_vectors.close()
	print('img_vec_dict established')
	
	#read text vecs
	all_vectors = open('./data/all_vectors_1000.txt', 'r')
	print('all_vectors opened')
	text_lines = all_vectors.readlines()


	count_1 = 0
	count_10 = 0
	count_100 = 0
	count_1000 = 0
	count_not_in_1000 = 0

	count_file = 1
	for text_line in text_lines:
		id = text_line.split(',')[0]
		text_vec = np.array(text_line.split(',')[1:-1],dtype=float)
		text_vec = preprocessing.normalize(text_vec.reshape((1, -1)), norm='l2')[0]
		pred = predict_list(text_vec)
		pred_len = float(len(pred))
		meet = 1
		for tmp in pred:
			if tmp[0] == id:
				break
			meet = meet + 1
		print('Predicted %s texts'%count_file)
		count_file = count_file + 1


		if meet <= 1:
			count_1 = count_1 + 1
		elif meet <= 10 :
			count_10 = count_10 + 1
		elif meet <= 100 :
			count_100 = count_100 + 1
		elif meet <= 1000 :
			count_1000 = count_1000 + 1
		else:
			count_not_in_1000 = count_not_in_1000 + 1

	print('In 1 st: %s, precentage: %s'%(count_1,count_1/pred_len))
	print('In top 10: %s, precentage: %s'%(count_10,count_10/pred_len))
	print('In top 100: %s, precentage: %s'%(count_100,count_100/pred_len))
	print('In top 1000: %s, precentage: %s'%(count_1000,count_1000/pred_len))
	print('Not in top 1000: %s, precentage: %s'%(count_not_in_1000,count_not_in_1000/pred_len))