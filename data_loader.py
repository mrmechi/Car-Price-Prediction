import pandas as pd

class Data_Getter:
    """ This class shall  be used for obtaining the data from the source for training. """

    
    def __init__(self):
        """ This method shall be used to store the data in the variable """

        self.training_file='cardata.csv'


    def get_data(self):
        """
            Method Name: get_data
            Description: It method shall be used to load the raw data.    
            Output: It loads the raw dataset
            On Failure: Raise Exception
        """
        try:
            data=pd.read_csv(self.training_file)
            return data 
        except:
            print("Unable to load the raw dataset")
