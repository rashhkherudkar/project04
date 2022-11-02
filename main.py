

from flask import Flask, jsonify, render_template, request
from models.utils import CarPrice
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Car Price Prediction")
    return render_template("index.html")

@app.route('/predict_charges', methods = ["POST"])
def get_car_charges():

    if request.method == "POST":
        print("We are using POST Method")
    
        make=request.form.get("make")
        symboling=int(request.form.get("symboling"))
        fuel_type=request.form.get("fuel_type")
        aspiration=request.form.get("aspiration")
        num_of_doors=request.form.get("num_of_doors")
        body_style=request.form.get("body_style")
        drive_wheels=request.form.get("drive_wheels")
        engine_location=request.form.get("engine_location")
        number_of_cylinders=request.form.get("number_of_cylinders")
        horsepower=int(request.form.get("horsepower"))


        print('make,symboling,fuel_type,aspiration,num_of_doors,body_style, drive_wheels,engine_location,number_of_cylinders,horsepower',
             make,symboling,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,number_of_cylinders,horsepower)

        car_cost=CarPrice(make,symboling,fuel_type,aspiration,num_of_doors,body_style,
                        drive_wheels,engine_location,number_of_cylinders,horsepower)
        charges = car_cost.get_predicted_price()
        return render_template("index.html", prediction =abs(charges))

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=config.PORT_NUMBER, debug=True)