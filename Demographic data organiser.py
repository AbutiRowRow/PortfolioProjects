#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = (pd.crosstab(index = df["race"],columns = "count_of_races"))

    # What is the average age of men?
    males = df["sex"] == "Male"
    male_data = df[males]
    age_to_array = np.array(male_data["age"])
    average_age_men = np.average(age_to_array)

    # What is the percentage of people who have a Bachelor's degree?
    education_organized = pd.crosstab(index = df["education"], columns = "qualification")
    education_array = np.array(education_organized["qualification"]).sum()
    bachelor_array = np.array(education_organized.loc["Bachelors"])
    percentage_bachelors= bachelor_array[0]*100/education_array

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education_holder = ((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate") )
    advanced_data = df[advanced_education_holder]
    pay_disparity = advanced_data["salary"] == ">50K"
    top_earners = advanced_data[pay_disparity]

    high_education_percent = len(top_earners)*100/len(advanced_data)
    
    # What percentage of people without advanced education make more than 50K?
    non_advanced_education_holder = ((df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate"))
    non_advanced_data = df[non_advanced_education_holder]
    pay_disparity_of_non_advanced = non_advanced_data["salary"] == ">50K"
    top_earners_non_advanced = non_advanced_data[pay_disparity_of_non_advanced]

    low_education_percent = len(top_earners_non_advanced)*100/len(non_advanced_data)
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(top_earners)
    lower_education = len(top_earners_non_advanced)

    # percentage with salary >50K
    higher_education_rich = high_education_percent
    lower_education_rich = low_education_percent

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    working_hours = df[df["salary"] == ">50K"]
    work_hours = working_hours["hours-per-week"]
    hours_array = np.array(work_hours)
    minimum_hours = np.min(hours_array)
  
    min_workers_top_earning = len(working_hours[working_hours["hours-per-week"] == minimum_hours])
    min_workers = len(df[df["hours-per-week"] == minimum_hours])
    min_work_hours = minimum_hours
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = min_workers_top_earning

    rich_percentage = num_min_workers*100/min_workers
  
    # What country has the highest percentage of people that earn >50K?
    new_frame = df[(df["salary"]==">50K")]["native-country"].value_counts()/df["native-country"].value_counts()
    max_value_in_array = np.max(new_frame)
    frame_array = np.array(new_frame).tolist()
    position = frame_array.index(max_value_in_array)
    highest_earning_country = new_frame.index[position]
    highest_earning_country_percentage = max_value_in_array*100

    # Identify the most popular occupation for those who earn >50K in India.
    rich_occupation = df[(df["salary"]==">50K") & (df["native-country"]=="India")]["occupation"].value_counts()
    rich_occupation_array = np.array(rich_occupation)
    rich_occupation_array = rich_occupation_array.tolist()
    rich_occupation_array.sort(reverse=True)
    
    
    top_IN_occupation = rich_occupation.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
demographic_data_analyzer.calculate_demographic_data()

