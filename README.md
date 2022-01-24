# paper : 
Jing Ma, Wei Gao, Kam-Fai Wong. Rumor Detection on Twitter with Tree-structured Recursive Neural Networks. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, ACL 2018.

#Datasets : 
Datasets used in the experiment were based on publically available PHEME_9 dataset.

Note : extract the all-rnr-annotated-threads.rar file before running the code

Main folder contains the model,Extraction(pre-processing) code, and the pre-processed datasets in resource and nfold directories and a vocabulary file. 

Gurlitt folder contains the same directories and files but which are compatible to the Gurlitt-rnr-thread dataset in PHEME. 

The difference in both the directories being the word_dimension in the model which is data-set dependent and the pre-processing scripts in Gurlitt parses only gurlitt-rnr-threads while the scripts in the Main directory parses all 9 of the datasets in all-rnr-threads into a single dataset.

In the 'resource' folder we provide the pre-processed data files used for the experiments. The raw datasets can be downloaded from https://figshare.com/articles/dataset/PHEME_dataset_for_Rumour_Detection_and_Veracity_Classification/6392078

The data file(abcd_TD/abcd_BU) is in a tab seperated coloumn format where each row corresponds to a tweet. consecutive tweets corresponds to the following piece of information : 
1: root-id : tweet-id of the root 
2: index-of-parent-tweet : an index number of the parent of the current tweet
3: index-of-current-tweet : an index number of the current tweet 
4: parent-number(in case of TD tree) : the total number of parent nodes in the tree that the current tweet belongs to
4: max-degree(in case of BU tree) : the maximum of degree of all nodes when the edges are reversed with respect to TD tree
5: text-length : the maximum length of all texts from the tree that the current tweet belongs to 
6: list-of-index-and-counts : rest of the line contains space sperated index(global)-count(local) pairs of the words/terms used in the tweet current tweet

# dependencies: 
numpy version 1.11.2
theano version 0.8.2

# pre-process the raw data 
Run the script "Extraction/main.py" to dump the pre-processed files directly into resource and nfold folders for both Top-down and Bottom-up trees.Also the vocabulary file is saved in the directory.

# reproduce the experimental results 
Run script "model/Main_BU_RvNN.py" for bottom-up recursive model or "model/Main_TD_RvNN.py" for up-down recursive model.Alternatively, you can change the "fold" parameter to set the dataset and each fold.
