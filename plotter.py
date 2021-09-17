import pandas as pd
import statsmodels.api as sm
import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
import matplotlib.pyplot as plt
import calendar
import datetime


def plot(filename, column, output_fig, x_axis, y_axis, year):
    df = pd.read_csv(filename, usecols = column, nrows = 8760)
    dti = pd.date_range(pd.to_datetime(datetime.datetime(year,1,1)), periods=8760, freq="H")
    df['Datetime'] = dti
    df.index = df['Datetime']
    df['month'] = pd.to_datetime(df.index).month
    df['month'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    df['hour'] = pd.to_datetime(df.index).hour
    
    sns.lineplot(x=x_axis,
                 y=y_axis,
                 hue='month',
                 data=df,
                 style = 'month',
                 markers=True,
                 sizes = [13,8],
                 legend = 'auto',
                 ci = None)
    plt.savefig(output_fig, dpi=300)


if __name__ == "__main__":
    filename = 'XXXXXX.csv'
    column = ['XXXXX']
    output_fig = 'seaborn-plot.png'
    x_axis = 'hour'
    y_axis = column[0]
    year = 2022
    plot(filename, column, output_fig, x_axis, y_axis, year)
