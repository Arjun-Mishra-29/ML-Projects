import os
import sys
from ..exception import customexception
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # used to create class variables

from src.componenets.data_transformation import DataTransformation,DataTransformationConfig

@dataclass
class DaatIngestionConfig:
    # these all are the inputs that is given to  DataIngestion Component that make sur, where to dave train,
    # test,raw path
 
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DaatIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Enter the data ingestio method or component')

        try:
            df=pd.read_csv(r"notebook\data\stud.csv")
            logging.info("Read the dataset as Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise customexception(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_tranformation=DataTransformation()
    data_tranformation.initiate_data_transformation(train_data,test_data)



