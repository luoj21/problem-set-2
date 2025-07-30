'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import matplotlib.pyplot as plt
import seaborn as sns

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes



##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def create_charge_type_catplot_felony(pred_universe_with_fel_charge):
    """Creates catplot where categories are charge type and y-axis is prediction for felony arrest
    
    Parameters:
    - pred_universe_with_fel_charge: the pred universe data frame with the new column has_felony_charge
    
    Returns:
    None"""
    plt.clf()
    catplot = sns.catplot(data=pred_universe_with_fel_charge,
                x='has_felony_charge',
                y='prediction_felony', 
                kind='bar')
    catplot.set_xticklabels(['Felony', 'Non-felony (Misdemeanor)'])
    plt.savefig('data/part4_plots/catplot_charge_type_felony_arrest.png')

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def create_charge_type_catplot_nonfelony(pred_universe_with_fel_charge):
    """Creates catplot where categories are charge type and y-axis is prediction for non-felony arrest
    
    Parameters:
    - pred_universe_with_fel_charge: the pred universe data frame with the new column has_felony_charge
    
    Returns:
    None"""
    plt.clf()
    catplot = sns.catplot(data=pred_universe_with_fel_charge,
                x='has_felony_charge',
                y='prediction_nonfelony', 
                kind='bar')
    catplot.set_xticklabels(['Felony', 'Non-felony (Misdemeanor)'])
    plt.savefig('data/part4_plots/catplot_charge_type_nonfelony_arrest.png')
    print("Part 4 Q2 Answer: The difference in the plots could be due to that those who already have a felony are less likely to commit" \
    "another one, but may be more likely to commit less severe crimes")
# In a print statement, answer the following question: What might explain the difference between the plots?



# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
#

def create_charge_type_catplot_felony_hue(pred_universe_with_fel_charge):
    """Creates catplot where categories are charge type and y-axis is prediction for felony arrest, hued by whether
    or not the person actually got arrested for a felony crime
    
    Parameters:
    - pred_universe_with_fel_charge: the pred universe data frame with the new column has_felony_charge
    
    Returns:
    None"""
    plt.clf()
    catplot = sns.catplot(data=pred_universe_with_fel_charge,
                x='has_felony_charge',
                y='prediction_felony', 
                kind='bar',
                hue='y_felony')
    catplot.set_xticklabels(['Felony', 'Non-felony (Misdemeanor)'])
    plt.savefig('data/part4_plots/catplot_charge_type_felony_arrest_hue.png')
    print("Part 4 Q3 Answer: This means the prediction puts more weight on whether or not you already had a felon charge or not to begin with")
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?