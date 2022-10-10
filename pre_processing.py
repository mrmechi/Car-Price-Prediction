import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Preprocessor:

    """ This class shall be used to do the preprocessing of the cleaned data """


    def __init__(self):
        """ This method shall be used to store the cleaned data in the variable """

        self.newtraining_file='Cleaned_car_data.csv'


    def new_data(self):
        """
            Method Name: new_data
            Description: It method shall be used to load the cleaned data.    
            Output: It loads the cleaned dataset
            On Failure: Raise Exception
        """
        try:
            clean_data=pd.read_csv(self.newtraining_file)
            return clean_data 
        except:
            print("Unable to load the dataset")



    def finding_unique(self,data):
        """
            Method Name: finding_unique
            Description: It method shall be used to find the uniques values in the "company".    
            Output: It returns unique values of the column "company".
            On Failure: Raise Exception
        """
        self.data=data
        try:
            self.unique=self.data['company'].unique()
            return self.unique
        except:
            print("Error while finding unique Companies")



    def outliers_in_price(self,data,columns):
        """
            Method Name: outliers_in_price
            Description: It method shall be used to remove the outliers in "price" column.    
            Output: It returns the "price" column with no outliers.
            On Failure: Raise Exception
        """
        self.data=data
        self.columns=columns
        try:
            self.data[self.data[self.columns]<6000000]
            return self.data
        except:
            print("No outliers found")



    def boxplot_company_price(self,data,column1,column2):
        """
            Method Name: boxplot_company_price
            Description: It method shall be used to plot the boxplot for "company" and "Price" column.
            Output: It returns "Boxplot for Company and Price".png
            On Failure: Raise Exception
        """
        self.data=data
        self.column1=column1
        self.column2=column2

        try:
            self.a=plt.subplots(figsize=(10,5))
            self.b=ax=sns.boxplot(x=self.column1,y=self.column2,data=self.data)
            self.c=ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
            self.d=plt.savefig('Boxplot_for_Company_and_Price')
            return self.d
        except:
            print('Unable to plot Boxplot of Company vs Price')



    def swarmplot_year_price(self,data,column1,column2):
        """
            Method Name: swarmplot_year_price
            Description: It method shall be used to plot the swarmplot for "year" and "Price" column.
            Output: It returns "Swarmplot for Year and Price".png
            On Failure: Raise Exception
        """
        self.data=data
        self.column1=column1
        self.column2=column2
        try:
            self.a=plt.subplots(figsize=(10,5))
            self.b=ax=sns.swarmplot(x=self.column1,y=self.column2,data=self.data)
            self.c=ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
            self.d=plt.savefig('Swarmplot_for_Year_and_Price')
            return self.d
        except:
            print("Error while ploting swarmplot of Year vs Price")



    def relational_plot_kmdriven_price(self,data,column1,column2):
        """
            Method Name: relational_plot_kmdriven_price
            Description: It method shall be used to plot the relational plot for "kms_driven" and "Price" column.
            Output: It returns "Relational plot for Year and Price".png
            On Failure: Raise Exception
        """
        self.data=data
        self.column1=column1
        self.column2=column2
        try:
            self.a=sns.relplot(x=self.column1,y=self.column2,data=self.data,height=7,aspect=1.5)
            self.c=plt.savefig('Relational_plot_for_Year_and_Price')
            return self.c
        except:
            print("Error while ploting relational plot of Kmdriven vs Price ")



    def boxplot_Fueltype_Price(self,data,column1,column2):
        """
            Method Name: boxplot_Fueltype_Price
            Description: It method shall be used to plot the box plot for "Fueltype" and "Price" column.
            Output: It returns "Boxplot for Fueltype and Price".png
            On Failure: Raise Exception
        """
        self.data=data
        self.column1=column1
        self.column2=column2
        try:
            self.a=plt.subplots(figsize=(10,5))
            self.b=sns.boxplot(x=self.column1,y=self.column2,data=self.data)
            self.c=plt.savefig('Boxplot_for_Fueltype_and_Price')
            return self.c
        except:
            print("Error while ploting box plot of Fueltype vs Price ")



    def multirelation_plot_for_Price(self,data,column1,column2,column3,column4):
        """
            Method Name: multirelation_plot_for_Price
            Description: It method shall be used to plot the box plot for multipe columns with respect to the "Price" column.
            Output: It returns "Multiple Boxplot for Price".png
            On Failure: Raise Exception
        """
        self.data=data
        self.column1=column1
        self.column2=column2
        self.column3=column3
        self.column4=column4

        try:
            self.a=sns.relplot(x=self.column1,y=self.column2,data=self.data,hue=self.column3,size=self.column4,height=7,aspect=2)
            self.a.set_xticklabels(rotation=40,ha='right')
            self.b=plt.savefig('Multiple_Boxplot_for_Price')
            return self.b
        except:
            print("Error while plotting multiple relation of Price")


