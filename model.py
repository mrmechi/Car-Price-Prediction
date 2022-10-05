import data_cleaner
import data_loader
import pre_processing
import pandas as pd

class Clean_model:

    """
          change the variable as per requirements as in jupyter notebook
          therefore we created a new varible as year_data and passed year_data as argument 
          like car['year'] in jupyter notebook
    """


    data=data_loader.Data_Getter().get_data()

    data=data_cleaner.Cleaner().num_year(data,'year')

    data=data_cleaner.Cleaner().int_year(data,'year')

    data=data_cleaner.Cleaner().drop_non_int_in_price(data,'Price')

    data=data_cleaner.Cleaner().conv_str_to_int_in_price(data,'Price')

    data=data_cleaner.Cleaner().formatting_km_driven(data,'kms_driven')

    data=data_cleaner.Cleaner().conv_str_to_int_in_km_driven(data,'kms_driven')

    data=data_cleaner.Cleaner().removing_na_in_fuel_type(data,'fuel_type')

    data=data_cleaner.Cleaner().fixing_name(data,'name')

    data=data_cleaner.Cleaner().index(data)

    data=data_cleaner.Cleaner().csv(data)



    ''' Now following the preprocessing steps to create our ML model'''

    ndata=pre_processing.Preprocessor().finding_unique(data)

    print(ndata,'My Preciousss  b b')



