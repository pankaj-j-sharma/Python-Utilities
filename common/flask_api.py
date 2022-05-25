# command to test this api type below on cmd prompt
#cURL -d @data.json http://127.0.0.1:12345/predict --header "Content-Type:application/json"
#  -d @data.json =>          define data file path with @<filepath> or define the data in quoted string '{key1:value1}' 
#  http://127.0.0.1:12345 => url of the API we need to test where /predict is the route in API
#  /predict				  => since we want to hit the predict method we add this in URL		
#  -- header content-type => defines the type of data we are passing to the URL

# sample command and output
# C:\Suven\AdvML>curl -d @data.json http://127.0.0.1:12345/predict --header "Content-Type:application/json"
# {
  # "prediction": "[0, 1, 0, 0]"
# }

# -- sample data.json file ---
#{"content":
	# [{"Age": 85, "Sex": "male", "Embarked": "S"},
	# {"Age": 24, "Sex": "female", "Embarked": "C"},
	# {"Age": 3, "Sex": "male", "Embarked": "C"},
	# {"Age": 21, "Sex": "male", "Embarked": "S"}]}

#------------------------------------------------------------------------------------------
#cURL(client URL),lightweight,cmd-line tool for making HTTP requests without a web browser. 
#It lets you try out various API requests via the cmd in Windows or Terminal in macOS. 
# without need to build a working web application just to try out the APIs.
#cURL makes HTTP requests just like a web browser. 
#To request a web page from the command line, type curl followed by the site's URL:
#------------------------------------------------------------------------------------------

# Your api.py should look like this:
# This file needs to be run from command line 
# after running we can see it has hosted the flask app 
# on a given url which we can see on the cmd 
#e.g.  http://127.0.0.1:12345/

# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route("/")
def index():
    return "HI I am there!"

@app.route('/predict', methods=['POST'])
def predict():
    
    if lr:
        try:
            json_ = request.get_json()
            #return jsonify({'prediction1': str(json_)})
            #print(json_,type(json_['content']))
            #print(pd.read_json(json_))
            query = pd.get_dummies(pd.DataFrame(json_['content']))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except Exception as e:

            return jsonify({str(e)+'Error': 'Seems input is incomplete or not in JSON'})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    lr = joblib.load("model.pickle") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pickle") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)
    # this will host the app on the given port 
    # can be typically accessed at http://127.0.0.1:12345/
