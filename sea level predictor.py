#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    years = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']
  
      # Create scatter plot
    fig,ax = plt.subplots()
    ax= plt.scatter(years,sea_level)
    

    # Create first line of best fit
    lin_output = linregress(years,sea_level)
    xfit = np.linspace(np.min(years),np.max(2050))
    yfit = xfit*lin_output[0] + lin_output[1]
    plt.plot(xfit,yfit,'r')

    # Create second line of best fit
    df_2000 = df.loc[df["Year"]>= 2000]
    years2 = df_2000["Year"]
    sea_level2 = df_2000["CSIRO Adjusted Sea Level"]
    lin_output2 = linregress(years2,sea_level2)
    xfit2 = np.linspace(2000,2050)
    yfit2 = xfit2*lin_output2[0] + lin_output2[1]
    plt.plot(xfit2,yfit2,'orange')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level(inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

sea_level_predictor.draw_plot()

