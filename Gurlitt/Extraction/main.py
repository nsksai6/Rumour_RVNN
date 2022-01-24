import os
import json 
from tqdm import tqdm 
import time
import extra
import label
import n_fold

dir_path = '../../all-rnr-annotated-threads/gurlitt-all-rnr-threads/' 

dic = {}
index = {}
index_count = {}
count = {}

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

def writing(r_d,r_path) :
	for twts in r_d :
		twt_path = r_path + twts + '/'
		parent , indx,p_count,degree = extra.extract(twt_path)
		with open ('../resource/abcd_TD.txt','a') as f_TD , open ('../resource/abcd_BU.txt','a') as f_BU: 
			for k,v in parent.items() : 
				temp = ''
				#print (twts , " ",index[k]," ",index[v])
				if ( v not in indx.keys()) :
					continue

				for key,value in index_count[k].items() :
					temp = temp + str(index[key]) + ':' + str(value) + ' '

				line1 = str(twts) + '\t' + str(indx[v]) + '\t' + str(indx[k]) + '\t' + str(p_count) + '\t'+ str(count[twts]) +'\t' + temp +'\n'
				line2 = str(twts) + '\t' + str(indx[v]) + '\t' + str(indx[k]) + '\t' + str(degree) + '\t'+ str(count[twts]) +'\t' + temp +'\n'
				f_TD.write(line1)
				f_BU.write(line2)

def parse(path,maxi) :
	for files in os.listdir(path) :
		f = files.split('.')[0]
		temp = {}
		file_path = path + files
		with open (file_path,'r',encoding="cp437", errors='ignore') as twt :
			data = json.loads(twt.read())
		if "text" in data.keys() :
			line = data["text"]
			count = 0
			for word in line.split() :
				count = count + 1
				if word not in dic.keys() : 
					dic[word] = 1
				if word not in temp.keys() :
					temp[word] = 1
				else :
					temp[word] = temp[word] + 1
			maxi = max(maxi,count)
			index_count[f] = temp
	return maxi

def labeling(r_d,r_path,d) :
	folder = d.split('-')[0]
	for twts in r_d : 
		twt_path = r_path + twts + '/'
		labels = label.extract(twt_path)
		with open('../resource/label.txt','a') as f :
			for k,v in labels.items() :
				line = str(v) + '\t' + folder + '\t' + str(k) + '\n'
				f.write(line)


if __name__ == '__main__': 

	j = 1
	maxi = -1

	print("Creating train and test data sets ...")
	n_fold.nfold(dir_path)
	print("... Creation over \n")

	d =  'ebola-essien-all-rnr-threads'
	dirs = directories(dir_path)

	print("parsing the tweets \n")

	# for d in tqdm(dirs) :
	# 	r_path = dir_path + d + '/' + 'rumours' +'/'
	# 	nr_path = dir_path + d + '/' + 'non-rumours' + '/'

	r_path = dir_path + 'rumours' +'/'
	nr_path = dir_path + 'non-rumours' + '/'
	r_d = directories(r_path)
	nr_d = directories(nr_path)

	for twts in tqdm(r_d) :
		stwt_path = r_path + twts + '/source-tweets/'
		rtwt_path = r_path + twts + '/reactions/'
		maxi = parse(stwt_path,maxi)
		maxi = parse(rtwt_path,maxi)
		count[twts] = maxi
		maxi = -1

	for twts in tqdm(nr_d) :
		stwt_path = nr_path + twts + '/source-tweets/'
		rtwt_path = nr_path + twts + '/reactions/'
		maxi = parse(stwt_path,maxi)
		maxi = parse(rtwt_path,maxi)
		count[twts] = maxi
		maxi = -1

	print("\nParsing Done\n")
	print("Creating a vocabulary ... ")

	for k,v in dic.items(): 
		index[k] = j
		j = j + 1

	print("Saving the Vocabulary into indices.json ...")

	with open ('../indices.json','w') as outfile :
		json.dump(index,outfile)

	print("... Created and Saved \n")
	print("Labelling and Creating Top-down and Bottom-up trees ")

	# for d in tqdm(dirs) :
	# 	r_path = dir_path + d + '/' + 'rumours' +'/'
	# 	nr_path = dir_path + d + '/' + 'non-rumours' + '/'

	writing(r_d,r_path)
	writing(nr_d,nr_path)
	labeling(r_d,r_path,d)
	labeling(nr_d,nr_path,d)

	print("..... Done")
	print("\nPre-processing Over ... ! \n")
	    	
