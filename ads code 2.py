# -*- coding: utf-8 -*-
"""
Created on Sat May 13 03:48:03 2023

@author: MOIN
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot


# Input path globally for file.
#Initialising the data for different economies
global_dframe=pd.read_csv("C:\\Moin"\\WorldBankClimateChange.csv")

#Initial rows of the dataset
global_dframe.head()

#Transpose dataset format
global_dframe.T

countries_1 = ['United States', 'United Kingdom', 'Germany']
countries_2 = ['United States', 'United Kingdom', 'Germany', 'Belgium', 'Bolivia', 'Georgia', 'Libya']
countries_3 = ['United States', 'United Kingdom', 'Germany', 'Belgium', 'Bolivia']


def read_file(input_file):
    first_data_filtered = pd.read_csv(input_file, skiprows=4)
    first_data_filtered = first_data_filtered.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    first_data_filtered = first_data_filtered.dropna(how='all')
    second_data_filtered = first_data_filtered.set_index('Country Name')
    

    return first_data_filtered, second_data_filtered


# two dataframes returning from function.
first_data_filtered, second_data_filtered = read_file(input_path)
print(first_data_filtered.loc[countries_1, '2014'].describe())

sns.boxplot(x='Country Name', y='2016', data=first_data_filtered.loc[countries_1].reset_index(), color="blue")
plt.ylabel('CO2 emissions per capita (metric tons)')
plt.show()


first_data_filtered.loc[countries_2, '2005':].plot()
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.show()
plt.legend()

sns.boxplot(x='Country Name', y='2007', data=first_data_filtered.loc[countries_3].reset_index(), color="blue")
first_data_filtered.loc[countries_3, '2007':].plot()
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.show()
plt.legend()