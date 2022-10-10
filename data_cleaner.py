class Cleaner:
    """  
    This class shall be used to clean the raw dataset
    
    """

    def num_year(self,data,column): 
            
            """
            Method Name: num_year
            Description: This method shall be used to list out the non-year values of the "year" column.    
            Output: It gives only the year values in the "year" column
            On Failure: Raise Exception

        """  
            self.data=data
            self.column=column

            try:
                self.year_in_num=self.data[self.data[self.column].str.isnumeric()]
                return self.year_in_num
            except:
                print("Non-year values in the year column is excists")


    def int_year(self,data,column):
        """
            Method Name: int_year
            Description: This method shall be used to change the object into integer in the "year" column.  
            Output: It returns the int values in the "year" column.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:
            self.data[self.column]=self.data[self.column].astype(int)
            return self.data
        except:
            print("Unable to convert the objects into integers in the year column")

    

    def drop_non_int_in_price(self,data,column):
        """
            Method Name: drop_non_int_in_price
            Description: This method shall be used to drop the non integer values in the "Price" column.  
            Output: It returns the int values in the "Price" column.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:
            self.data=self.data[self.data[self.column]!='Ask For Price']
            return self.data
        except:
            print("Unable to drop the string values in the Price column")


    def conv_str_to_int_in_price(self,data,column):
        """
            Method Name: conv_str_to_int_in_price
            Description: This method shall be used to convert the string into integers in the "Price" column.  
            Output: It returns the int values in the "Price" column.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:
            self.data[self.column]=self.data[self.column].str.replace(',','').astype(int)
            return self.data
        except:
            print("Unable to convert strings to integers in the Price column")
        

    def formatting_km_driven(self,data,column):
        """
            Method Name: formatting_km_driven
            Description: This method shall be used to format the "Price" column.  
            Output: It returns the formatted values in the "Price" column.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:
            self.data[self.column]=self.data[self.column].str.split().str.get(0).str.replace(',','')
            return self.data
        except:
            print("Error while formatting the Price column")


    def conv_str_to_int_in_km_driven(self,data,column):
        """
            Method Name: conv_str_to_int_in_km_driven
            Description: This method shall be used to convert strings to integers in "km_driven" column.  
            Output: It returns the formatted values in the "Price" column.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:
            self.data=self.data[self.data[self.column].str.isnumeric()]
            return self.data
        except:
            print("unable to convert strings to integers in km_driven column")

    def removing_na_in_fuel_type(self,data,column):
        """
            Method Name: removing_na_in_fuel_type
            Description: This method shall be used to remove the null values in the "fuel_type" column.  
            Output: It returns the non null values in the "fuel_type" column.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:
            self.data=self.data[~self.data[self.column].isna()]
            return self.data
        except:
            print("Null values excists in the fuel_type column")

    def fixing_name(self,data,column):
        """
            Method Name: fixing_name
            Description: This method shall be used to snip strings in the "name" column.  
            Output: It returns the snipped strings in the "name" column.
            On Failure: Raise Exception
        """
        self.data=data
        self.column=column
        try:

            self.data[self.column]=self.data[self.column].str.split().str.slice(start=0,stop=3).str.join(' ')
            return self.data
        except:
            print("Unable to snip the strings in the name column")


    def new_index(self,data):
        """
            Method Name: new_index
            Description: This method shall be used to reset the index of the dataset.  
            Output: It returns the data with the new index.
            On Failure: Raise Exception
        """
        self.data=data
        try:
            self.indexs=self.data.reset_index(drop=True)
            return self.indexs
        except:
            print("Unbale to reset the index")


    def new_csv(self,data):
        """
            Method Name: new_csv
            Description: This method shall be used to save the cleaned dateset as a csv file 
            Output: It returns the "Cleaned_car_data.csv
            On Failure: Raise Exception
        """
        self.data=data
        try:
            self.cleaned_data=self.data.to_csv('Cleaned_car_datashbihbh.csv')
            return self.cleaned_data
        except:
            print("New csv file cannot be created")