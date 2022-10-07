import pandas as pd

class Data_Getter:
    """ This class shall  be used for obtaining the data from the source for training. """

    
    def __init__(self):
        self.training_file='cardata.csv'


    def get_data(self):
        try:
            data=pd.read_csv(self.training_file)
            return data 
        except:
            print("Unable to load the dataset")
