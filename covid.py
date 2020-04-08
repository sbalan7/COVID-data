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

colors = ["#00FF00", "#0000FF"]
sns.set_palette(sns.color_palette(colors))

def process_file(file_dest):

    with open(file_dest, "r") as f:
            the_reader=csv.reader(f,delimiter=",")
            contents=[]
            for row in the_reader:
                contents.append(row)
    
    del contents[0]  #deletes header row
    return contents

def make_ind_df(contents, summary=False):
    
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
    if summary:
        df.info()

    return df

def make_ita_df(contents, summary=False):
    
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
    if summary:
        df.info()

    return df  

def make_usa_df(contents, summary=False):
    
    infected=[]
    recovered=[]
    deceased=[]
    dates=[]
    x = len(contents)
    
    for i in range(len(contents)):
      
        dates.insert(0, x)
        x-=1
        infected.insert(0, int(contents[i][2]))
        if (contents[i][14]==''):
            contents[i][14] = 0
        if (contents[i][11]==''):
            contents[i][11] = 0
        deceased.insert(0, int(contents[i][14]))
        recovered.insert(0, int(contents[i][11]))

    
    usa_dict={'Days since first infection':dates, 'Infected':infected, 'Dead':deceased, 'Recovered':recovered}
    
    df = pd.DataFrame(usa_dict)
    if summary:
        df.info()

    return df  

def make_kor_df(contents, summary=False):
    
    infected=[]
    recovered=[]
    deceased=[]
    dates=[]
    x = 0
    
    for i in range(len(contents)):
      
        dates.append(x)
        x+=1
        infected.append(int(contents[i][-3]))
        deceased.append(int(contents[i][-1]))
        recovered.append(int(contents[i][-2]))

    
    kor_dict={'Days since first infection':dates, 'Infected':infected, 'Dead':deceased, 'Recovered':recovered}
    
    df = pd.DataFrame(kor_dict)
    
    if summary:
        df.info()

    return df  

def singlelineplot(prop, df, color, label):
    sns.lineplot(x='Days since first infection', y=prop, data=df, color=color, label=label)
    sns.despine()

def compareproperties(prop, df1, df1_name, df2, df2_name):
        
    plt.figure()
    sns.set(style='darkgrid')
    
    singlelineplot(prop, df1, "#00ff00", label=df1_name)
    singlelineplot(prop, df2, "#009900", label=df2_name)

    plt.title(prop)
    plt.show()


ind_df = make_ind_df(process_file("covid_19_india.csv"))
ita_df = make_ita_df(process_file("covid19_italy_region.csv"))
usa_df = make_usa_df(process_file("us_covid19_daily.csv"))
kor_df = make_kor_df(process_file("covid19_korea.csv"))

compareproperties("Infected", ind_df, "India", kor_df, "Korea")
compareproperties("Infected", ita_df, "Italy", usa_df, "USA")


'''
plt.figure()
x_col="Days since first infection"
y_col="Infected"
sns.lineplot(x=x_col, y=y_col, data=ind_df, color="green")
sns.lineplot(x=x_col, y=y_col, data=kor_df, color="blue")
#sns.pointplot(x=x_col, y=y_col, data=ita_df, color="red")


''
f, ax = plt.subplots(1, 1, figsize=figsize)
x_col='date'
y_col = 'count'
sns.pointplot(ax=ax,x=x_col,y=y_col,data=df_1,color='blue')
sns.pointplot(ax=ax,x=x_col,y=y_col,data=df_2,color='green')
sns.pointplot(ax=ax,x=x_col,y=y_col,data=df_3,color='red')
df_1['region'] = 'A'
df_2['region'] = 'B'
df_3['region'] = 'C'
df = pd.concat([df_1,df_2,df_3])
sns.pointplot(ax=ax,x=x_col,y=y_col,data=df,hue='region')
'''
