import seaborn as sns

def side_by_side_portion(df, mainVar, groupVar):
    """creates a side by side histogram showing the portion of the main variable by a listed group variable.
    IE, % vote by age would be side_by_side_portion(df, voteVar, ageVar) """
    dfT = (df[mainVar]
        .groupby(df[groupVar])
        .value_counts(normalize=True)
        .rename("portion")
        .reset_index())
    sns.barplot(data=dfT, x=mainVar, y='portion', hue=groupVar)


def side_by_side_count(df, mainVar, groupVar):
    """creates a side by side histogram showing the count of the main variable by a listed group variable.
    IE, % vote by age would be side_by_side_count(df, voteVar, ageVar) """
    sns.countplot(data=df, x=mainVar, hue=groupVar)
