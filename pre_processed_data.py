
import pre_processing


class Preprocessed_data:

    """ 
    Calling the required methods from the pre_processing
    
    """

    clean_data=pre_processing.Preprocessor().new_data()

    clean_data=pre_processing.Preprocessor().finding_unique(clean_data)

    clean_data=pre_processing.Preprocessor().outliers_in_price(clean_data,'Price')

    clean_data=pre_processing.Preprocessor().boxplot_company_price(clean_data,'company','Price')

    clean_data=pre_processing.Preprocessor().swarmplot_year_price(clean_data,'year','Price')

    clean_data=pre_processing.Preprocessor().relational_plot_kmdriven_price(clean_data,'kms_driven','Price')

    clean_data=pre_processing.Preprocessor().boxplot_Fueltype_Price(clean_data,'fuel_type','Price')

    clean_data=pre_processing.Preprocessor().multirelation_plot_for_Price(clean_data,'company','Price','fuel_type','year')

    print(clean_data)

