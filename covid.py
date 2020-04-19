# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:43:15 2020

@author: Aalaap Nair & Shanmugha Balan
            
"""

import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import imageio as io


# Get the lines from the file to a processed list
def process_file(file_dest):

    with open(file_dest, "r") as f:
            the_reader=csv.reader(f,delimiter=",")
            contents=[]
            for row in the_reader:
                contents.append(row)
    
    del contents[0]  #deletes header row
    return contents

# A specific DataFrame maker for the covid_19_india.csv
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
    
    # The data is made cumulative in this loop
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

# A specific DataFrame maker for the covid19_italy_region.csv 
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
    
    # The data is made cumulative in this loop
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

# A specific DataFrame maker for the us_covid19_daily.csv
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

# A specific DataFrame maker for the covid19_korea.csv
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

# A simple despined line plot  
def singlelineplot(prop, df, color, label):
    sns.lineplot(x='Days since first infection', y=prop, data=df, color=color, label=label)
    sns.despine()

# A comparative line plot between two countries
def compareproperties(prop, df1, df1_name, df2, df2_name):
        
    plt.figure()
    sns.set(style='darkgrid')
    
    singlelineplot(prop, df1, "#00ff00", label=df1_name)
    singlelineplot(prop, df2, "#009900", label=df2_name)

    plt.title(prop)
    plt.show()

# A graph of the infected, dead and recovered in a country
def countrysituation(df, country):
    
    plt.figure()
    sns.set(style='dark')
    
    singlelineplot("Infected", df, "#da4272", "Infected")
    singlelineplot("Dead", df, "#000000", "Dead")
    singlelineplot("Recovered", df, "#10d260", "Recovered")
    
    plt.title(country)
    plt.show()

# Generates a plot with every progressing day
# Primarily, a feeder function for gifize()
def animate(df, prop, country):
    
    pics = []
    rows = df.size/4
    y_limit = max(df[prop]) 
    title = str(prop + " in " + country)
    for i in range(1, int(rows)):
        plt.figure(figsize=(10,6))
        plt.title(title, fontsize=20)
        plt.xlim(0, rows)
        plt.ylim(0, y_limit)
        plt.xlabel('Days since first infection', fontsize=15)
        plt.ylabel(prop, fontsize=15)    
        data = df.iloc[:i]
        sns.lineplot(x="Days since first infection", y=data[prop], data=data)
        filename = str(str(prop) + "/" + str(i) + ".png")
        plt.savefig(filename)
        pics.append(filename)
    return pics
    
# Converts the pictures to a gif
def gifize(pics):
    
    images = []
    for img in pics:
        images.append(io.imread(img))
    io.mimsave("covid.gif", images)
        
   
# Invoking the functions to build the DataFrames
ind_df = make_ind_df(process_file("covid_19_india.csv"))
ita_df = make_ita_df(process_file("covid19_italy_region.csv"))
usa_df = make_usa_df(process_file("us_covid19_daily.csv"))
kor_df = make_kor_df(process_file("covid19_korea.csv"))

# Comparing stats in two countries
compareproperties("Infected", ind_df, "India", kor_df, "Korea")
compareproperties("Dead", ita_df, "Italy", usa_df, "USA")

# Comparing the infected of all 4 countries
prop = 'Infected'
plt.figure()
sns.set(style='darkgrid')

singlelineplot(prop, ind_df, "#173367", label='India')
singlelineplot(prop, kor_df, "#f67bad", label='Korea')
singlelineplot(prop, usa_df, "#00ff00", label='USA')
singlelineplot(prop, ita_df, "#26c0e5", label='Italy')

plt.title(prop)
plt.show()

# Plotting the infected, dead and recovered in India
countrysituation(ind_df, 'India')

# Generating the increase of infected in Italy
gifize(animate(ita_df, "Infected", "Italy"))

