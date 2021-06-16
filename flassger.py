import pickle
import pandas as pd
from flasgger import Swagger
from flask import Flask, request

app = Flask(__name__)
swagger = Swagger(app)

pickle_in = open("cat_model.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Credit Card Lead Authentication"


@app.route('/predict', methods=["Get"])
def predict_card_authentication():
    """
    ---
    parameters:
      - name: Gender
        in: query
        type: string
        enum: ["Female","Male"]
        required: true
        default": "Female"
      - name: Age
        in: query
        type: number
        required: true
      - name: Region_Code
        in: query
        type: string
        enum: ['RG268', 'RG277', 'RG270']
        required: true
        default": "RG268"
      - name: Occupation
        in: query
        type: string
        enum: ['Other','Salaried','Self_Employed','Entrepreneur']
        required: true
        default": "Other"
      - name: Channel_Code
        in: query
        type: string
        enum: ['X3','X1','X2','X4']
        required: true
        default": "X3"
      - name: Vintage
        in: query
        type: number
        required: true
      - name: Credit_Product
        in: query
        type: string
        enum: ['No','Yes']
        required: true
        default": "No"
      - name: Avg_Account_Balance
        in: query
        type: number
        required: true
      - name: Is_Active
        in: query
        type: string
        enum: ['No','Yes']
        required: true
        default": "No"
    responses:
       200:
          description: The output values
     """
    Gender = request.args.get("Gender")
    Age = request.args.get("Age")
    Region_Code = request.args.get("Region_Code")
    Occupation = request.args.get("Occupation")
    Channel_Code = request.args.get("Channel_Code")
    Vintage = request.args.get("Vintage")
    Credit_Product = request.args.get("Credit_Product")
    Avg_Account_Balance = request.args.get("Avg_Account_Balance")
    Is_Active = request.args.get("Is_Active")

    prediction = classifier.predict([[Gender, Age, Occupation, Channel_Code,Vintage,Credit_Product,Avg_Account_Balance,Is_Active]])
    print(prediction)
    return "Hello The answer is" + str(prediction)


@app.route('/predict_file', methods=["POST"])
def predict_card_authentication_file():
    """
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values

    """
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction = classifier.predict(df_test)

    return str(list(prediction))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
