from flask import Flask, request 
import pandas as pd 

df = pd.read_csv('data/utilization2019csv.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'Time to get some encounter count!!!..... I Hope.....'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(25)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/county_code/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['county_code'] == value]
    return filtered.to_json(orient="records")

#504
@app.route('/filter/<value>', methods=['GET'])
def member_months(value):
    print('value: ', value)
    filtered = df[df['member_months'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

#504
@app.route('/filter/<value>/payer/<value2>', methods=['GET'])
def member_months2(value, value2):
    filtered = df[df['member_months'] == value]
    filtered2 = filtered[filtered['payer'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records") 

if __name__ == '__main__':
    app.run(debug=True)
