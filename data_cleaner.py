

class Cleaner:

    def num_year(self, data,column):
            self.data=data
            self.column=column
            
            self.year_in_num=self.data[self.data[self.column].str.isnumeric()]
            return self.year_in_num


    def int_year(self,data,column):
        self.data=data
        self.column=column

        self.data[self.column]=self.data[self.column].astype(int)
        return self.data

    

    def drop_non_int_in_price(self,data,column):
        self.data=data
        self.column=column

        self.data=self.data[self.data[self.column]!='Ask For Price']
        return self.data


    def conv_str_to_int_in_price(self,data,column):
        self.data=data
        self.column=column

        self.data[self.column]=self.data[self.column].str.replace(',','').astype(int)
        return self.data
        

    def formatting_km_driven(self,data,column):
        self.data=data
        self.column=column

        self.data[self.column]=self.data[self.column].str.split().str.get(0).str.replace(',','')
        return self.data


    def conv_str_to_int_in_km_driven(self,data,column):
        self.data=data
        self.column=column

        self.data=self.data[self.data[self.column].str.isnumeric()]
        return self.data

    def removing_na_in_fuel_type(self,data,column):
        self.data=data
        self.column=column

        self.data=self.data[~self.data[self.column].isna()]
        return self.data

    def fixing_name(self,data,column):
        self.data=data
        self.column=column

        self.data[self.column]=self.data[self.column].str.split().str.slice(start=0,stop=3).str.join(' ')
        return self.data


    def new_index(self,data):
        self.data=data

        self.indexs=self.data.reset_index(drop=True)
        return self.indexs


    def new_csv(self,data):
        self.data=data

        self.cleaned_data=self.data.to_csv('Cleaned_car_datassssssssss.csv')
        return self.cleaned_data