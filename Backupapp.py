from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import csv
import os
import numpy as np
from sklearn import tree
from flask import Flask, request, jsonify
from flask import make_response
app = Flask(__name__)
port = int(os.getenv("PORT", 9009))

#Main Declaration
@app.route('/train',methods=['POST'])
def train():
		req = request.get_json(silent=True, force=True)
		print("Request:")
		print(json.dumps(req,indent=4))
		processReq = processRequest(req)
		#input=[[115.2,115,111.1,111]]
		input = processReq
		filename_features = 'features.csv'
		features=loadCSV_features(filename_features)
		filename_label = 'label.csv'
		label = loadCSV_label(filename_label)
		X=features
		label=np.array(label)
		y=np.ravel(label)

		clf=tree.DecisionTreeClassifier()
		clf=clf.fit(features,label)
		out=clf.predict(input) #Pass the required Testing Data as a List
		result= out[0]
		#print(result)
		#return result
		res = json.dumps({"speech": result,
"displayText": result,
"data": {},
"contextOut": [],
"source": ""})# print(res)
		r = make_response(res)
		r.headers['Content-Type'] = 'application/json'
		return r

#processRequestFromChatBOT
def processRequest(req):
		if req.get("result").get("action") != "SAPAction":
			return {}
		result = req.get("result")
		parameters = result.get("parameters")
		role = parameters.get("roles")
		if(role == "fiori"):
			return [[5,5,10.1,10]]
		elif(role == "abap"):
			return [[11.2,10,5.1,5]]
		elif(role == "basis"):
			return [[15.2,10,5.1,5]]
		elif(role == "super admin"):
			return [[20.2,20,5.1,5]]
		elif(role == "security"):
			return [[10.2,10,20,20]]
		return [[20.2,20,20.1,20]]



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
    app.run(host='0.0.0.0', port=port)
