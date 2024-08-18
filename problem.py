# medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
# from urllib.request import urlretrieve
# urlretrieve(medical_charges_url, 'medical.csv')
import pandas as pd

medical_df = pd.read_csv('medical-charges.csv')
print(medical_df)

# checking the data types of the information
medical_df.info()

print(medical_df.describe())