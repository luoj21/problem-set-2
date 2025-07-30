'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 

def create_scatterpot_predfelony_prednonfelony(pred_universe_with_fel_charge):
    """Creates scatter plot where x-axis is the prediction for felony and y-axis is axis for non-felony, hued by whether or not a person already has a felony charge
    
    Parameters:
    - pred_universe_with_fel_charge: the pred universe data frame with the new column has_felony_charge
    
    Returns:
    None"""
    sns.lmplot(data=pred_universe_with_fel_charge, 
               x='prediction_felony', 
               y='prediction_nonfelony',
               hue='has_felony_charge',
               fit_reg=False)
    plt.savefig('./data/part5_plots/predfelony_prednonfelony_hue_scatterplot.png')
    print("Part 5 Q1 Answer: The group of dots on the right side of the plot are those who have a felony current charge and would likely " \
    "commit another felony again")
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.

def create_scatterpot_predfelonyrearrest_actuallyrearrest(pred_universe_with_fel_charge):
    """Creates scatter plot where x-axis is the prediction for felony rearrest and y-axis wheher the person was actually rearrested
    
    Parameters:
    - pred_universe_with_fel_charge: the pred universe data frame with the new column has_felony_charge
    
    Returns:
    None"""
    sns.lmplot(data=pred_universe_with_fel_charge, 
               x='prediction_felony', 
               y='y_felony',
               fit_reg=False)
    plt.savefig('./data/part5_plots/predfelonyrearrest_actuallyrearrest__scatterplot.png')
    print("The model is not well calibrated as the values take extreme values only (0 or 1)")
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?