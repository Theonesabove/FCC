import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv("/workspace/boilerplate-medical-data-visualizer/medical_examination.csv")

# 2. Add 'overweight' column
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (bmi > 25).astype(int)

# 3. Normalize cholesterol and glucose
for col in ['cholesterol', 'gluc']:
    df[col] = (df[col] > 1).astype(int)

# 4. Draw Categorical Plot
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # 8
    fig.savefig('catplot.png')
    return fig

# 9. Draw Heat Map
def draw_heat_map():
    # 10. Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
               (df['height'] >= df['height'].quantile(0.025)) &
               (df['height'] <= df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(0.025)) &
               (df['weight'] <= df['weight'].quantile(0.975))]

    # 11. Calculate correlation matrix
    corr = df_heat.corr()

    # 12. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # 14. Draw the heatmap
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, cmap='coolwarm', center=0, linewidths=0.5, cbar_kws={'shrink': 0.5})

    # 15. Save the figure
    fig.savefig('heatmap.png')
    
    return fig
