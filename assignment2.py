#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:11:48 2022

@author: bilalnazir
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data_frames(filename,countries,indicator):
    '''
    This function returns two dataframes one with countries as column and other one years as column.
    It tanspose the dataframe and converts rows into column and column into rows of specific column and rows.
    It takes three arguments defined as below. 

    Parameters
    ----------
    filename : Text
        Name of the file to read data.
    countries : List
        List of countries to filter the data.
    indicator : Text
        Indicator Code to filter the data.

    Returns
    -------
    df_countries : DATAFRAME
        This dataframe contains countries in rows and years as column.
    df_years : DATAFRAME
        This dataframe contains years in rows and countries as column..

    '''
    # Read data using pandas in a dataframe.
    df = pd.read_csv(filename, skiprows=(4), index_col=False)
    # Get datafarme information.
    df.info()
    # To clean data we need to remove unnamed column.
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # To filter data by countries
    df = df.loc[df['Country Name'].isin(countries)]
    # To filter data by indicator code.
    df = df.loc[df['Indicator Code'].eq(indicator)]
    
    # Using melt function to convert all the years column into rows as one column
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name',
                           'Indicator Code'], var_name='Years')
    # Deleting country code column.
    del df2['Country Code']
    # Using pivot table function to convert countries from rows to separate 
    # column for each country.   
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],
                          'Country Name').reset_index()
    
    df_countries = df
    df_years = df2
    
    # Cleaning data droping nan values.
    df_countries.dropna()
    df_years.dropna()
    
    return df_countries, df_years

# List of countries 
countries = ['Germany','Australia','United States','China','United Kingdom']
# calling functions to get dataframes and use for plotting graphs.
df_c, df_y = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv',countries,'AG.LND.FRST.ZS')


#==============================================================================
# Bar Chart for Forest area (% of land area)
#==============================================================================
num= np.arange(5)
width= 0.2
# Select specific years data 
df_y = df_y.loc[df_y['Years'].isin(['2000','2001','2002','2003','2004'])]
years = df_y['Years'].tolist() 

# Plotting data on bar chart
plt.figure(dpi=144)
plt.title('Forest area (% of land area)')
plt.bar(num,df_y['Germany'], width, label='Germany')
plt.bar(num+0.2, df_y['Australia'], width, label='Australia')
plt.bar(num-0.2, df_y['United States'], width, label='United States')
plt.bar(num-0.4, df_y['China'], width, label='China')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% of land area')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

#==============================================================================
# Bar Chart for Agricultural land (% of land area)
#==============================================================================
df_c, df_y = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv',countries,'AG.LND.AGRI.ZS')
num= np.arange(5)
width= 0.2
# Select specific years data 
df_y = df_y.loc[df_y['Years'].isin(['2000','2001','2002','2003','2004'])]
years = df_y['Years'].tolist() 

#Ploting data on bar chart  
plt.figure(dpi=144)
plt.title('Agricultural land (% of land area)')
plt.bar(num,df_y['Germany'], width, label='Germany')
plt.bar(num+0.2, df_y['Australia'], width, label='Australia')
plt.bar(num-0.2, df_y['United States'], width, label='United States')
plt.bar(num-0.4, df_y['China'], width, label='China')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% of land area')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


#==============================================================================
# Pie chart for Population growth (annual %)
#==============================================================================
df_c, df_y = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv',countries,'SP.POP.GROW')

# calculating data for pie chart
aus = np.sum(df_y['Australia'])
usa = np.sum(df_y['United States'])
chi = np.sum(df_y['China'])
uk = np.sum(df_y["United Kingdom"])
ger = np.sum(df_y["Germany"])

total = aus + usa + chi + ger

australia = aus / total*100
united_states = usa / total*100
china = chi/ total*100
united_kingdom = uk / total*100
germany = ger / total*100

population_list = np.array([germany,australia,united_states,china,united_kingdom])
explode=(0.2,0.0,0.0,0.0,0.1)

# Plotting pie charts
plt.figure(dpi=144)
plt.pie(population_list,labels=countries,explode=explode,autopct=('%1.1f%%'))
plt.title("Population growth (annual %)")
plt.show()

#==============================================================================
# Pie chart for CO2 emissions (metric tons per capita)
#==============================================================================
df_c, df_y = get_data_frames('API_19_DS2_en_csv_v2_4700503.csv',countries,'EN.ATM.CO2E.PC')

# calculating data for pie chart
aus1 = np.sum(df_y['Australia'])
usa1 = np.sum(df_y['United States'])
uk1 = np.sum(df_y["United Kingdom"])
ger1 = np.sum(df_y["Germany"])
chi1 = np.sum(df_y['China'])

total1 = aus1 + usa1 + chi1 + ger1

australia1 = aus1 / total1*100
united_states1 = usa / total1*100
china1 = chi1 / total1*100
united_kingdom1 = uk1 / total1*100
germany1 = ger1 / total1*100
poverty_list = np.array([germany1,australia1,united_states1,china1,united_kingdom1])
explode=(0.0,0.0,0.2,0.1,0.0) 

# Plotting pie charts
plt.figure(dpi=144)
plt.pie(poverty_list,labels=countries,explode=explode,autopct=('%1.1f%%'))
plt.title("CO2 emissions (metric tons per capita)")
plt.show()

#==============================================================================





