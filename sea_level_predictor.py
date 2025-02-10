import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", alpha=0.5)
    
    # Create first line of best fit (1880 - latest year)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = range(1880, 2051)
    plt.plot(years_extended, intercept + slope * pd.Series(years_extended), 'r', label='Fit 1880-2050')
    
    # Create second line of best fit (2000 - latest year)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = range(2000, 2051)
    plt.plot(years_recent, intercept_recent + slope_recent * pd.Series(years_recent), 'g', label='Fit 2000-2050')
    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
