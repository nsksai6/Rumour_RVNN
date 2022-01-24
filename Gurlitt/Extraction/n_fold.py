import os
import json 
from tqdm import tqdm 
import time
from sklearn.model_selection import train_test_split
import numpy

#dir_path = 'C:/Users/yashwanth/Desktop/all-rnr-annotated-threads/gurlitt-all-rnr-threads/' 

ids = []

def write(i,s,x) :
	with open('../nfold/RNN'+s+'Set_PHEME_'+str(i)+'.txt','w') as f :
		for things in x :
			f.write(str(things) + '\n')

def nfold(dir_path) : 
	# for dirs in os.listdir(dir_path) :
	# 	#print(dirs,'\n')
	# 	r = dir_path + dirs + '/rumours/'
	# 	nr = dir_path + dirs + '/non-rumours/'
	r = dir_path + 'rumours/'
	nr = dir_path + 'non-rumours/'
	for twts in os.listdir(r) :
		ids.append(twts)
	for twts in os.listdir(nr) :
		ids.append(twts)
	for i in list(range(0,5)) :
		x_train,x_test = train_test_split(ids,test_size = 0.2)
		write(i,'train',x_train)
		write(i,'test',x_test)

if __name__ == '__main__': 
	nfold(dir_path)





