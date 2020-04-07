# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:43:15 2020

@author: Aalaap Nair & Shanmugha Balan

@description: 1) Reads the .csv dataset and generates a dictionary output with date strings as keys, national infected 
                 numbers as data
            
"""

import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def process_file(file_dest):

    with open(file_dest, "r") as f:
            the_reader=csv.reader(f,delimiter=",")
            contents=[]
            for row in the_reader:
                contents.append(row)
    
    del contents[0]  #deletes header row
    return contents

def make_ind_df(contents):
    
    infected=[]
    recovered=[]
    deceased=[]

    date_str=contents[0][1]  #start date
    
    day_count=0
    rec_count=0
    death_count=0

    dates=[]
    x = 0
    
    for i in range(len(contents)):
        
        if contents[i][1]==date_str:
            
            day_count+=int(contents[i][-1])
            death_count+=int(contents[i][-2])
            rec_count+=int(contents[i][-3])
            
        else:
            
            dates.append(x)
            x+=1
            date_str=contents[i][1]
            
            infected.append(day_count)
            deceased.append(death_count)
            recovered.append(rec_count)
            
            day_count=int(contents[i][-1])
            death_count=int(contents[i][-2])
            rec_count=int(contents[i][-3])
    
    
    infected.append(day_count)
    deceased.append(death_count)
    recovered.append(rec_count)
    dates.append(x)
   
    ind_dict={'Days since first infection':dates, 'Infected':infected, 'Dead':deceased, 'Recovered':recovered}
    
    df = pd.DataFrame(ind_dict)
    df.info()

    return df

def make_ita_df(contents):
    
    infected=[]
    recovered=[]
    deceased=[]

    date_str=contents[0][1]  #start date
    
    inf_count=0
    rec_count=0
    death_count=0

    dates=[]
    x = 0
    
    for i in range(len(contents)):
        
        if contents[i][1]==date_str:
            
            inf_count+=int(contents[i][-2])
            death_count+=int(contents[i][-3])
            rec_count+=int(contents[i][-4])
            
        else:
            
            dates.append(x)
            x+=1
            date_str=contents[i][1]
            
            infected.append(inf_count)
            deceased.append(death_count)
            recovered.append(rec_count)
            
            inf_count=int(contents[i][-2])
            death_count=int(contents[i][-3])
            rec_count=int(contents[i][-4])
    
    
    infected.append(inf_count)
    deceased.append(death_count)
    recovered.append(rec_count)
    dates.append(x)

    ita_dict={'Days since first infection':dates, 'Infected':infected, 'Dead':deceased, 'Recovered':recovered}
    
    df = pd.DataFrame(ita_dict)
    df.info()

    return df  

def make_usa_df(contents):
    
    infected=[]
    recovered=[]
    deceased=[]
    dates=[]
    x = len(contents)
    
    for i in range(len(contents)):
      
        dates.append(x)
        x-=1
        infected.append(int(contents[i][2]))
        if (contents[i][14]==''):
            contents[i][14] = 0
        if (contents[i][11]==''):
            contents[i][11] = 0
        deceased.append(int(contents[i][14]))
        recovered.append(int(contents[i][11]))

    
    usa_dict={'Days since first infection':dates, 'Infected':infected, 'Dead':deceased, 'Recovered':recovered}
    
    df = pd.DataFrame(usa_dict)
    df.info()

    return df  


ind_df = make_ind_df(process_file("covid_19_india.csv"))
ita_df = make_ita_df(process_file("covid19_italy_region.csv"))
usa_df = make_usa_df(process_file("us_covid19_daily.csv"))
'''
data = {'Days since infection':ind_df['Days since first infection'], 
        'India':ind_df['Infected'], 
        'Italy':ita_df['Infected']
        }

df = pd.DataFrame(data)

plt.plot('Days since infection', 'India', data=df, marker='', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=2)
plt.plot('Days since infection', 'Italy', data=df, marker='', color='olive', linewidth=2)
#plt.plot('Days since infection', 'USA', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
plt.legend()


sns.lineplot(x='Days since infection',
             y='India',
             data=df,
             markers=['o','<','>'],
             legend="brief"
             )



sns.lmplot(x='Days since first infection', y='Infected', data=ind_df, fit_reg=False)
sns.despine()

sns.lmplot(x='Days since first infection', y='Infected', data=ita_df, fit_reg=False)
sns.despine()
'''
sns.lmplot(x='Days since first infection', y='Infected', data=usa_df, fit_reg=False)
sns.despine()

