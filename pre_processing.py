import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Preprocessor:

    def __init__(self):
        self.newtraining_file='Cleaned_car_data.csv'


#  loading the clean data set 

    def new_data(self):
        try:
            clean_data=pd.read_csv(self.newtraining_file)
            return clean_data 
        except:
            print("Unable to load the dataset")



    def finding_unique(self,data):
        self.data=data
        try:
            self.unique=self.data['company'].unique()
            return self.unique
        except:
            print("Error while finding unique Companies")



# removing outliers in price column 

    def outliers_in_price(self,data,columns):
        self.data=data
        self.columns=columns
        try:
            self.data[self.data[self.columns]<6000000]
            return self.data
        except:
            print("No outliers found")



    #  Checking relationship of Company with Price

    def boxplot_company_price(self,data,column1,column2):
        self.data=data
        self.column1=column1
        self.column2=column2

        try:
            self.a=plt.subplots(figsize=(10,5))
            self.b=ax=sns.boxplot(x=self.column1,y=self.column2,data=self.data)
            self.c=ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
            self.d=plt.show()
            # self.e=plt.savefig('Boxplot for Company and Price')
            return self.e
        except:
            print('Unable to plot Boxplot of Company vs Price')



    # Checking relationship of Year with Price

    def swarmplot_year_price(self,data,column1,column2):
        self.data=data
        self.column1=column1
        self.column2=column2
        try:
            self.a=plt.subplots(figsize=(10,5))
            self.b=ax=sns.swarmplot(x=self.column1,y=self.column2,data=self.data)
            self.c=ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha='right')
            # self.d=plt.show()
            self.e=plt.savefig('Swarmplot for Year and Price')
            return self.e
        except:
            print("Error while ploting swarmplot of Year vs Price")



    # Checking relationship of kms_driven with Price

    def relational_plot_kmdriven_price(self,data,column1,column2):
        self.data=data
        self.column1=column1
        self.column2=column2
        try:
            self.a=sns.relplot(x=self.column1,y=self.column2,data=self.data,height=7,aspect=1.5)
            # self.b=plt.show()
            self.c=plt.savefig('Relational plot for Year and Price')
            return self.c
        except:
            print("Error while ploting relational plot of Kmdriven vs Price ")


    
    # Checking relationship of Fuel Type with Price

    def boxplot_Fueltype_Price(self,data,column1,column2):
        self.data=data
        self.column1=column1
        self.column2=column2
        try:
            self.a=plt.subplots(figsize=(10,5))
            self.b=sns.boxplot(x=self.column1,y=self.column2,data=self.data)
            # self.c=plt.show()
            self.d=plt.savefig('Boxplot for Fueltype and Price')
            return self.d
        except:
            print("Error while ploting box plot of Fueltype vs Price ")



    # Relationship of Price with FuelType, Year and Company mixed

    def multirelation_plot_for_Price(self,data,column1,column2,column3,column4):
        self.data=data
        self.column1=column1
        self.column2=column2
        self.column3=column3
        self.column4=column4

        try:
            self.a=sns.relplot(x=self.column1,y=self.column2,data=self.data,hue=self.column3,size=self.column4,height=7,aspect=2)
            self.a.set_xticklabels(rotation=40,ha='right')
            self.c=plt.show()
            # d=plt.savefig('Multiple Boxplot for Price')
            return self.c
        except:
            print("Error while plotting multiple relation of Price")









clean_data=Preprocessor().new_data()

clean_data=Preprocessor().finding_unique(clean_data)

clean_data=Preprocessor().outliers_in_price(clean_data,'Price')

clean_data=Preprocessor().boxplot_company_price(clean_data,'company','Price')

clean_data=Preprocessor().swarmplot_year_price(clean_data,'year','Price')

clean_data=Preprocessor().relational_plot_kmdriven_price(clean_data,'kms_driven','Price')

clean_data=Preprocessor().boxplot_Fueltype_Price(clean_data,'fuel_type','Price')

clean_data=Preprocessor().multirelation_plot_for_Price(clean_data,'company','Price','fuel_type','year')




print(clean_data)

