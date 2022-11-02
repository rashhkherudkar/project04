import pandas as pd
import numpy as np
import pickle
import json
import config

class CarPrice():
    def __init__(self,make,symboling,fuel_type,aspiration,num_of_doors,body_style,
                 drive_wheels,engine_location,number_of_cylinders,horsepower):

                self.make='make_'+ make
                self.symboling=symboling
                self.fuel_type=fuel_type
                self.aspiration=aspiration
                self.num_of_doors=num_of_doors
                self.body_style='body-style_'+body_style
                self.drive_wheels=drive_wheels
                self.engine_location=engine_location
                self.number_of_cylinders=number_of_cylinders
                self.horsepower=horsepower


    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_price(self):
    
        self.load_model()

        array=np.zeros(len(self.json_data['columns']))

        make_val=self.json_data['columns'].index(self.make)

        bodystyle_val=self.json_data['columns'].index(self.make)

        array[make_val]=1
        array[0]=self.symboling
        array[2]=self.json_data['fuel_type'][self.fuel_type]
        array[3]=self.json_data['aspiration'][self.aspiration]
        array[4]=self.json_data['num_of_doors'][self.num_of_doors]
        array[bodystyle_val]=1
        array[5]=self.json_data['drive_wheels'][self.drive_wheels]
        array[6]=self.json_data['engine_location'][self.engine_location]
        array[7]=self.json_data['number_of_cylinders'][self.number_of_cylinders]
        array[17]=self.horsepower
        
        print(array)

        predicted_price=self.model.predict([array])[0]
        print("predicted_charges",abs(predicted_price))
        return round(predicted_price,2)

        

if __name__ == "__main__":
    # user inputs value

    make='jaguar'
    symboling=3
    fuel_type='gas'
    aspiration="std"
    num_of_doors='four'
    body_style='sedan'
    drive_wheels="rwd"
    engine_location='front'
    number_of_cylinders='five'
    horsepower=111

    car_cost = CarPrice(make,symboling,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,number_of_cylinders,horsepower)
    charges = car_cost.get_predicted_price()
    print("predicted_price is",'$',abs(charges),'/-')
    # print("predicted_price is",'$',abs(charges))
        


