'''
- You will run Problem Set 2 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5
import pandas as pd


def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    felony_charge = part1.create_felony_charge_df(arrest_events)
    pred_universe_with_fel_charge = pd.merge(pred_universe, felony_charge, on = 'arrest_id', how = 'outer')

    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)


    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##
    # 1
    part3.create_fta_barplot(pred_universe)

    # 2
    part3.create_fta_barplot_hued(pred_universe)

    # 3
    part3.create_age_at_arrest_hist(pred_universe)

    # 4
    part3.create_age_at_arrest_hist_binned_age(pred_universe)

    ##  PART 4: CATEGORICAL PLOTS  ##
    # 1
    part4.create_charge_type_catplot_felony(pred_universe_with_fel_charge)
    
    # 2
    part4.create_charge_type_catplot_nonfelony(pred_universe_with_fel_charge)

    # 3
    part4.create_charge_type_catplot_felony_hue(pred_universe_with_fel_charge)

    ##  PART 5: SCATTERPLOTS  ##
    # 1
    part5.create_scatterpot_predfelony_prednonfelony(pred_universe_with_fel_charge)
    # 2
    part5.create_scatterpot_predfelonyrearrest_actuallyrearrest(pred_universe_with_fel_charge)



if __name__ == "__main__":
    main()
