import csv
import os
import numpy as np
from sklearn import tree
from flask import Flask, request, jsonify
app = Flask(__name__)

#Main Declaration
@app.route('/train',methods=['GET'])
def train():
		filename_features = 'features.csv'
		features=loadCSV_features(filename_features)
		filename_label = 'label.csv'
		label = loadCSV_label(filename_label)
		X=features
		label=np.array(label)
		y=np.ravel(label)

		clf=tree.DecisionTreeClassifier()
		clf=clf.fit(features,label)
		input=[[115.2,115,111.1,111]]
		out=clf.predict(input) #Pass the required Testing Data as a List
		result= out[0]
		#print(result)
		#return result
		return {
			"speech": result,
			"displayText": result,
			# "data": data,
			# "contextOut": [],
			"source": "apiai-weather-webhook-sample"
			}

#Load Features Dataset
def loadCSV_features(filename_features):
	lines = csv.reader(open(filename_features, "r"))
	dataset_features = list(lines)
	for i in range(len(dataset_features)):
		dataset_features[i] = [(x) for x in dataset_features[i]]
	return dataset_features

#Load Label Dataset
def loadCSV_label(filename_label):
	lines = csv.reader(open(filename_label, "r"))
	dataset_label = list(lines)
	for i in range(len(dataset_label)):
		dataset_label[i] = [(x) for x in dataset_label[i]]
	return dataset_label 



if __name__ == '__main__':
	app.run(debug=True)
