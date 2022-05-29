from calendar import week, weekday
from flask import Flask , render_template , request
from graphviz import render
# import jsonify
import requests
import joblib
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)
#The given .pkl file is empty!
# model = pickle.load(open('randomforestclassifier.pkl','rb'))

app.static_folder = 'static'

model = joblib.load(r"Engage-main\forest.h5")

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        twilight_night = request.form.get('Astronomical_Twilight_Night')
        side_r = request.form.get('Side_R')
        timezone_us_east = request.form.get('Timezone_US/Eastern')
        timezone_us_mountain = request.form.get('Timezone_US/Mountain')
        timezone_us_pacific = request.form.get('Timezone_US/Pacific')
        station = request.form.get('Station')
        stop = request.form.get('Stop')
        traffic_signal = request.form.get('Traffic_Signal')
        rain = request.form.get('Rain')
        hwy = request.form.get('Hwy')
        Minute_Freq = request.form.get('Minute_Freq')
        Population_County_log = request.form.get('Population_County_log')
        Street_Freq = request.form.get('Street_Freq')
        State_Freq = request.form.get('State_Freq')
        Pressure_bc = request.form.get('Pressure_bc')

        int_features= [twilight_night, side_r, timezone_us_east, timezone_us_mountain, timezone_us_pacific, station, stop, traffic_signal, rain, hwy, Minute_Freq, Population_County_log, Street_Freq, State_Freq, Pressure_bc]
        final=[np.array(int_features)]
        prediction= model.predict(final)

        if prediction==1:
            pred = 'Accident is severe'
        else:
            pred = 'Accident is not severe'
        return render_template('result.html', pred=pred)


if __name__=='__main__':
    app.run(debug=True)
    
        
        
        
    