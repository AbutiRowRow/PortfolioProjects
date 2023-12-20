#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df["height"] = df["height"]/100
df["overweight"] = df["weight"]/(df["height"]*df["height"])
bmi_checker = (df["overweight"] > 25)
my_list = [int(i) for i in bmi_checker]
df["overweight"] = my_list
# normalisation of of cholesterol and glucose
cholesterol_checker = df["cholesterol"] > 1
glucose_checker = df["gluc"] > 1
df["cholesterol"] = [int(i) for i in cholesterol_checker]
df["gluc"] = [int(i) for i in glucose_checker]


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df, id_vars=['cardio'],value_vars = ['cholesterol','gluc','smoke','active','overweight','alco'])
  figure1 = sns.catplot(x = "variable",kind = "count",hue = "value",data = df_cat, col = "cardio")
  figure1.set_axis_labels("variable","total")


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
  fig = figure1


    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    pressure_boolean =(df['ap_lo'] <= df['ap_hi'])
    df_corrected = df[pressure_boolean]
    df_c2 = df_corrected[df_corrected['height'] >= df_corrected['height'].quantile(0.025)]
    df_c3 = df_c2[df_c2['height'] <= df_c2['height'].quantile(0.975)]
    df_4 = df_c3[(df_c3['weight']>=df_c3['weight'].quantile(0.025)) & (df_c3['weight']<=df_c3['weight'].quantile(0.975))]
    df_heat = df_4
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

  

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10,10))
    
    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask = mask, annot = True, vmin = 0, vmax = 0.3 ,fmt = '.1f', square = True, linewidth = 1, cbar_kws = {'shrink': .5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

