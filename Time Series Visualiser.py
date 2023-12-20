#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = [0])
df.set_index('date', inplace = True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.9725))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (15, 5))
    ax.plot(df,'r')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title(f'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month']).mean()

    df_bar = df_bar.unstack()
    df_bar.columns = df_bar.columns.droplevel()

    # Draw bar plot

    fig, ax = plt.subplots(figsize = (15, 5))
    fig = df_bar.plot(kind = 'bar').figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'],loc = 'upper left',title = 'Months',fontsize = 'small')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['year'] = pd.Categorical(df_box['year'], ordered = True)
    fig, (axYear,axMonth) = plt.subplots(1,2, figsize = (15, 5))
    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = axYear, hue = 'year',legend = False,flierprops = {'marker' : 'D'})
    axYear.set_xlabel('Month')
    axYear.set_ylabel('Page Views')
    axYear.set_title('Year-wise Box Plot (Trend)')
    df_box['month'] = pd.Categorical(df_box['month'], ordered = True, categories = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    sns.boxplot(x = 'month', y = 'value', data = df_box, ax = axMonth,hue = 'month',flierprops = {'marker' : 'D'})
    axMonth.set_xlabel('Year')
    axMonth.set_ylabel('Page Views')
    axMonth.set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

