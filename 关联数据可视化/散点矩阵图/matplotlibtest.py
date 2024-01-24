import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

crime = pd.read_csv("../data/crimeRatesByState2005.csv")
crime2 = crime[crime.state != "United States"]
crime2 = crime2[crime2.state != "District of Columbia"]
crime2 = crime2.drop(['state'],axis=1)
crime2 = crime2.drop(['population'],axis=1)
g = sns.pairplot(crime2,diag_kind="kde",kind="reg")

plt.show()