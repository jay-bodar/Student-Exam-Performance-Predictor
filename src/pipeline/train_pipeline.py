import sys

from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainer

from src.components.data_ingestion import DataIngestion

from src.exception import CustomException


class TrainingPipeline:
    def __init__(self):
        pass

    def train(self):
        try:
            obj = DataIngestion()
            test_data,train_data=obj.initial_data_ingestion()

            data_transformation=DataTransformation()
            train_data,test_data,_=data_transformation.initiate_data_transformation(train_data,test_data)

            modelTrainer = ModelTrainer()
            print(modelTrainer.initiate_model_trainer(train_data,test_data))

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    training = TrainingPipeline()
    training.train()