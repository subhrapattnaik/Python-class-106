import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        
        fig = px.scatter(df,x="SizeofTV", y="AveragetimespentwatchingTVinaweekhours")
        fig.show()

def getDataSource(data_path):
    size_of_tv = []
    average_time_spent_watching_TVina_weekhours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["SizeofTV"]))
            average_time_spent_watching_TVina_weekhours.append(float(row["AveragetimespentwatchingTVinaweekhours"]))

    return {"x" : size_of_tv, "y": average_time_spent_watching_TVina_weekhours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of Tv and Average Time Spent watching Tv :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./106/project/sizeoftvvstimespentwatching.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
