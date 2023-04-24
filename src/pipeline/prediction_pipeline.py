import sys
import pandas as pd
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Model_Trainer





class PredictPipeline:

    def __init__(self) -> None:
        pass

    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)

            return pred
        
        except Exception as e:
            logging.info("Exception has occured in prediction")
            raise CustomException(e,sys)
    

class CustomData:

    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity


    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame gathered')

            return df
           
        except Exception as e:
            logging.info('Exception occured in Prediction pipeline')
            raise CustomException(e,sys)
    

"""if __name__ == '__main__':
    obj = DataIngestion()

    train_data_path, test_data_path = obj.initiate_data_ingestion() 
    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer = Model_Trainer() # initilise the class
    model_trainer.initiate_model_training(train_arr, test_arr)
    data = CustomData(34, 32,23,23,21,45,'Fair','D','I1')
    final_new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_new_data)
    results = round(pred[0],2)
    logging.info(f"Prediction value is {results}")
    print(results)"""



