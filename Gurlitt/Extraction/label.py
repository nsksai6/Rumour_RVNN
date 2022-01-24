import os
import json
from tqdm import tqdm
import time
filePath = 'C:/Users/yashwanth/Desktop/all-rnr-annotated-threads/putinmissing-all-rnr-threads/rumours/576319105965359105/'


def convert(annotation, string = True):
    if 'misinformation' in annotation.keys() and 'true'in annotation.keys():
        if int(annotation['misinformation'])==0 and int(annotation['true'])==0:
            if string:
                label = "unverified"
            else:
                label = 2
        elif int(annotation['misinformation'])==0 and int(annotation['true'])==1 :
            if string:
                label = "true"
            else:
                label = 1
        elif int(annotation['misinformation'])==1 and int(annotation['true'])==0 :
            if string:
                label = "false"
            else:
                label = 0
        elif int(annotation['misinformation'])==1 and int(annotation['true'])==1:
            # print ("OMG! They both are 1!")
            # print(annotation['misinformation'])
            # print(annotation['true'])
            label = None
            
    elif 'misinformation' in annotation.keys() and 'true' not in annotation.keys():
        if int(annotation['misinformation'])==0:
            if string:
                label = "unverified"
            else:
                label = 2
        elif int(annotation['misinformation'])==1:
            if string:
                label = "false"
            else:
                label = 0
                
    elif 'true' in annotation.keys() and 'misinformation' not in annotation.keys():
        # print ('Has true not misinformation')
        label = None
    else:
        # print('No annotations')
        label = None
           
    return label




def extract (filePath) :
	label = {}
	filePath = filePath + 'annotation' + '.json'  
	with open (filePath,'r',encoding="cp437", errors='ignore') as root_twt : 
		data = json.loads(root_twt.read())
	root = filePath.split('/')[-2]
	folder = (filePath.split('/')[-4]).split('-')[0]
	if(data["is_rumour"] == "nonrumour") :
		label[root] = "non-rumour"
	else : 
		label[root] = convert(data)
	# for k,v in label.items() : 
	# 	print(v,"\t",folder,"\t",k,"\n")
	return label

if __name__ == '__main__': 
	extract(filePath)
