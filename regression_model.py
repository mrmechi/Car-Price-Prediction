
import pre_processing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import pickle


class MLmodel:

    """ This class shall be used to create the Machine Learning Model """

    def __init__(self,data):
        """ This init method shall be used to store the aspects of the model into the variables """

        self.data=data

        self.X=self.data[['name','company','year','kms_driven','fuel_type']]
        self.Y=self.data['Price']

        self.OHE=OneHotEncoder(handle_unknown='ignore')

        self.LR=LinearRegression()

        self.column_trans=make_column_transformer((OneHotEncoder(categories=self.OHE.categories),['name','company','fuel_type']),remainder='passthrough')


        X_train, X_test, Y_train, Y_test =train_test_split(self.X,self.Y,test_size=0.2)
        self.X_train=X_train
        self.X_test=X_test
        self.Y_train=Y_train
        self.Y_test=Y_test


    def one_hot_incoder(self):
        """
            Method Name: one_hot_incoder
            Description: It creates the OHE for the selected column type.    
            Output: It returns OHE.
            On Failure: Raise Exception
        """

        encoder=self.OHE.fit(self.X[['name','company','fuel_type']])
        return encoder

        

    def pipeline(self):
        """
            Method Name: pipeline
            Description: It creates the pipeline which is fitted on the training dataset to predict the r2score later, dumped into pickle.    
            Output: It returns an LinearRegressionModel.
            On Failure: Raise Exception
        """
        try:    
            self.pipe=make_pipeline(self.column_trans,self.LR)
            self.pipe.fit(self.X_train,self.Y_train)
            self.y_pred=self.pipe.predict(self.X_test)
            self.r2=r2_score(self.y_test,self.y_pred)
            self.pickle=pickle.dump(self.pipe,open('LinearRegressionModel.pkl','wb'))
            return self.pickle
        except:
            print("Error in the Pipeline")


 

data=pre_processing.Preprocessor().new_data()

model=MLmodel(data)

model=MLmodel(data).one_hot_incoder()

model=MLmodel(data).pipeline()
