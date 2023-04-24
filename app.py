from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
from src.logger import logging


application  = Flask(__name__)

app = application

@app.route('/anil', methods = ['POST'])
def home_page1():
    return "Anil"
    

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])

def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        ) # initialise the CustomData class with object 'data'


        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0],2)
        print(results)
        logging.info(f"Output value is : {results}")

        return render_template('results.html', final_result = results)
    





if __name__ == '__main__':
    app.run(host = '127.0.0.1', port= 8000, debug=True)