import pandas as pd
import statsmodels.api as sm
import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
import matplotlib.pyplot as plt
import calendar
df = pd.read_csv('USA_KS_Topeka-Forbes.AFB.724565_TMY3_BASE.csv', usecols = ['Electricity:Facility [kW](Hourly)'])
dti = pd.date_range("2022-01-01", periods=8760, freq="H")
df['Datetime'] = dti
df.index = df['Datetime']


df['month'] = pd.to_datetime(df.index).month
df['month'] = df['month'].apply(lambda x: calendar.month_abbr[x])
df['hour'] = pd.to_datetime(df.index).hour

sns.lineplot(x='hour',
             y='Electricity:Facility [kW](Hourly)',
             hue='month',
             data=df,
             style = 'month',
             markers=True,
             sizes = [13,8],
             legend = 'auto')
plt.savefig('seaborn-plot.png', dpi=300)