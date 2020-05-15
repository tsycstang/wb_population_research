import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def population_pyramid(country_code, year, raw_data=None, save_path=None, data_path='hnp_stats_csv/HNP_StatsData.csv'):
    if type(raw_data) == type(None):
        raw_data = pd.read_csv(data_path)
    pop_indicator_m = ['SP.POP.0004.MA.5Y', 'SP.POP.0509.MA.5Y', 'SP.POP.1014.MA.5Y', 'SP.POP.1519.MA.5Y', 'SP.POP.2024.MA.5Y', 'SP.POP.2529.MA.5Y', 
                       'SP.POP.3034.MA.5Y', 'SP.POP.3539.MA.5Y', 'SP.POP.4044.MA.5Y', 'SP.POP.4549.MA.5Y', 'SP.POP.5054.MA.5Y', 'SP.POP.5559.MA.5Y', 
                       'SP.POP.6064.MA.5Y', 'SP.POP.6569.MA.5Y', 'SP.POP.7074.MA.5Y', 'SP.POP.7579.MA.5Y', 'SP.POP.80UP.MA.5Y']
    pop_indicator_f = ['SP.POP.0004.FE.5Y', 'SP.POP.0509.FE.5Y', 'SP.POP.1014.FE.5Y', 'SP.POP.1519.FE.5Y', 'SP.POP.2024.FE.5Y', 'SP.POP.2529.FE.5Y',
                       'SP.POP.3034.FE.5Y', 'SP.POP.3539.FE.5Y', 'SP.POP.4044.FE.5Y', 'SP.POP.4549.FE.5Y', 'SP.POP.5054.FE.5Y', 'SP.POP.5559.FE.5Y', 
                       'SP.POP.6064.FE.5Y', 'SP.POP.6569.FE.5Y', 'SP.POP.7074.FE.5Y', 'SP.POP.7579.FE.5Y', 'SP.POP.80UP.FE.5Y']
    df_pop_m = raw_data[(raw_data['Country Code'] == country_code) & (raw_data['Indicator Code'].isin(pop_indicator_m))].reset_index(drop=True)
    df_pop_f = raw_data[(raw_data['Country Code'] == country_code) & (raw_data['Indicator Code'].isin(pop_indicator_f))].reset_index(drop=True)
    plt.cla()
    year = str(year)
    df_mf = pd.DataFrame(data={'Age': ['00-04', '05-09', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', 
                                       '60-64', '65-69', '70-74', '75-79', '80-up']}, index=range(17), columns=['Age', 'M', 'F'])
    df_mf['M'] = df_pop_m.loc[:,[year]]
    df_mf['F'] = df_pop_f.loc[:,[year]] * -1
    sns.set_style('white')
    bar_plot = sns.barplot(y = 'Age', x = 'F', color = 'red', data = df_mf, 
                           order = ['80-up', '70-74', '75-79', '65-69', '60-64',
                                    '55-59', '50-54', '45-49', '40-44', '35-39',
                                    '30-34', '25-29', '20-24', '15-19', '10-14',
                                    '05-09', '00-04'])
    bar_plot = sns.barplot(y = 'Age', x = 'M', color = 'blue', data = df_mf, 
                           order = ['80-up', '70-74', '75-79', '65-69', '60-64',
                                    '55-59', '50-54', '45-49', '40-44', '35-39',
                                    '30-34', '25-29', '20-24', '15-19', '10-14',
                                    '05-09', '00-04'])
    bar_plot.set(xlabel='Percentage (red: female; blue: male)', 
                 ylabel='Age Group', 
                 title = 'Population Pyramid - '+country_code+' - ' + year)
    if save_path != None:
        plt.savefig('pop_prmd_'+country_code+'_'+year+'.png')
        