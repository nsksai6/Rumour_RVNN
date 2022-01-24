
import os
import json 
from tqdm import tqdm 
import time

file_Path = 'C:/Users/yashwanth/Desktop/all-rnr-annotated-threads/ottawashooting-all-rnr-threads/rumours/524949339131904000/'


def my_write(data,parent) : 
	values = []
	for k,v in data.items() : 
		if isinstance(v,dict) and v != None :
			ret_val = my_write(v,parent)
			for x in ret_val : 
				parent[x] = k
		values.append(k)
	return values




def extract (filePath) :
	parent = {}
	index = {} 
	sept = set({})
	parent_count = {}
	degree = 0
	root = filePath.split('/')[-2]
	#print(root,"\n")
	filePath = filePath + 'structure' + '.json'  
	with open (filePath,'r',encoding="cp437", errors='ignore') as root_twt : 
		data = json.loads(root_twt.read())
		data = data[root]
	if isinstance(data,dict) :
		im_child = my_write(data,parent)
		for tweets in im_child :
			parent[tweets] = root
	parent[root] = "None" 
	index["None"] = "None"
	j = 1
	for k,v in parent.items() :
		index[k] = j
		j = j + 1
		sept.add(v)
		if v in parent_count.keys() :
			parent_count[v] = parent_count[v] + 1
		else : 
			parent_count[v] = 1
	for k,v in parent_count.items() :
		degree = max(degree,v)
	# 	print (k , " ", v ,"\n") 
	# for k,v in index.items() : 
	# 	print ('id : ',k, " ","index : ",v)
	# for k,v in parent.items() : 
	# 	print (index[v] ,'\t',index[k],'\n')
	# print(degree)
	return (parent,index,len(sept),degree)

if __name__ == '__main__': 
	extract(file_Path)

