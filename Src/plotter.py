import pandas as pd
import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
import matplotlib.pyplot as plt
import calendar
import datetime
from openpyxl import load_workbook

def plot(filename, column, output_fig, x_axis, y_axis, year, timezone):
    if filename.endswith('.csv'):
        df = pd.read_csv(filename, usecols = column, nrows=8760)
    if filename.endswith('.xlsx'):
        wb = load_workbook(filename)
        sheet = wb.active
        all_data = [sheet[f"A{str(i)}"].value for i in range (2,8762)]
        df = pd.DataFrame(all_data,columns = column)
    dti = pd.date_range(pd.to_datetime(datetime.datetime(year,1,1)), periods=8760, freq="H", tz = timezone)
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
                 ci= None)
    plt.savefig(output_fig, dpi=300)


if __name__ == "__main__":
    filename = 'SPP_North.xlsx'
    column = ['SPP North Hub']
    output_fig = 'seaborn-plot.png'
    x_axis = 'hour'
    y_axis = column[0]
    year = 2022
    timezone = 'US/Central'
    plot(filename, column, output_fig, x_axis, y_axis, year, timezone)
