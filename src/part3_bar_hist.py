'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def create_fta_barplot(pred_universe):
    """Creates a barplot based for the fta column and saves plot as a png
    
    Parameters:
    - pred_universe: the pred_universe data frame
    
    Returns:
    None"""
    plt.clf()
    pred_universe_fta_count = pred_universe.groupby(['fta']).size().reset_index(name='count')
    
    sns.barplot(data = pred_universe_fta_count,
                x = 'fta',
                y = 'count')
    plt.savefig('data/part3_plots/fta_barplot.png')


# 2. Hue the previous barplot by sex
def create_fta_barplot_hued(pred_universe):
    """Creates a barplot based for the fta column, hues by sex, and saves plot as a png
    
    Parameters:
    - pred_universe: the pred_universe data frame
    
    Returns:
    None"""
    plt.clf()
    pred_universe_fta_count = pred_universe.groupby(['fta', 'sex']).size().reset_index(name='count')
    
    sns.barplot(data = pred_universe_fta_count,
                x = 'fta',
                y = 'count',
                hue='sex')
    plt.savefig('data/part3_plots/fta_barplot_hue.png')


# 3. Plot a histogram of age_at_arrest
def create_age_at_arrest_hist(pred_universe):
    """Creates a histogram for age_at_arrest and saves plot as a png
    
    Parameters:
    - pred_universe: the pred_universe data frame
    
    Returns:
    None"""
    plt.clf()
    sns.histplot(data = pred_universe,
                 x = 'age_at_arrest')
    plt.savefig('data/part3_plots/age_at_arrest_histplot.png')


# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def create_age_at_arrest_hist_binned_age(pred_universe):
    """Creates a histogram for age_at_arrest with binned ages and saves plot as a png
    
    Parameters:
    - pred_universe: the pred_universe data frame
    
    Returns:
    None"""
    plt.clf()
    age_bins = [18, 21, 30, 40, 100]
    sns.histplot(data = pred_universe,
                 x = 'age_at_arrest',
                 bins = age_bins)
    plt.xticks(age_bins)
    plt.savefig('data/part3_plots/age_at_arrest_histplot_binned_age.png')
