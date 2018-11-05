import seaborn as sns

def side_by_side_portion(df, mainVar, groupVar):
    dfT = (df[mainVar]
        .groupby(df[groupVar])
        .value_counts(normalize=True)
        .rename("portion")
        .reset_index())

    sns.barplot(data=dfT, x=mainVar, y='portion', hue=groupVar)