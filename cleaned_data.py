import data_cleaner
import data_loader


class Clean_model:

    """
       Calling the required methods from the data_cleaner
    """

    data=data_loader.Data_Getter().get_data()

    clean_data=data_cleaner.Cleaner().num_year(data,'year')

    clean_data=data_cleaner.Cleaner().int_year(clean_data,'year')

    clean_data=data_cleaner.Cleaner().drop_non_int_in_price(clean_data,'Price')

    clean_data=data_cleaner.Cleaner().conv_str_to_int_in_price(clean_data,'Price')

    clean_data=data_cleaner.Cleaner().formatting_km_driven(clean_data,'kms_driven')

    clean_data=data_cleaner.Cleaner().conv_str_to_int_in_km_driven(clean_data,'kms_driven')

    clean_data=data_cleaner.Cleaner().removing_na_in_fuel_type(clean_data,'fuel_type')

    data=data_cleaner.Cleaner().fixing_name(clean_data,'name')

    clean_data=data_cleaner.Cleaner().new_index(clean_data)

    clean_data=data_cleaner.Cleaner().new_csv(clean_data)

    print(clean_data)



