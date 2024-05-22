import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    fig = plt.scatter(data=df,x='Year',y='CSIRO Adjusted Sea Level',label='Original Data')
    
    # Create first line of best fit
    first_reg=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(1880,2051)
    plt.plot(x1,(first_reg.slope*x1 + first_reg.intercept),'r', label='First Regress')

    # Create second line of best fit
    second_reg_mask= df['Year'] >= 2000
    second_reg=linregress(df[second_reg_mask].Year,df[second_reg_mask].get('CSIRO Adjusted Sea Level'))
    x2 = np.arange(2000,2051)
    plt.plot(x2,(second_reg.slope*x2 + second_reg.intercept),'g', label='Second Regress')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()