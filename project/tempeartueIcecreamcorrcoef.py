#find the correlation coefficient
#corrcoef() function in numpy library
#pip3 install numpy
#convert temperature data and ice-cream sales data into arrays
#convert each data set to float values (by default each data set is string)
#use corrcoef() function and pass two datasets to it
#store the output in a variable.
#print the correlation coefficient on the screen


import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    temperature=[]
    ice_cream_sales=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream-Sales"]))

    return {"x":temperature,"y":ice_cream_sales}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between Temperature vs Ice cream Sales:-",correlation[0,1])

def setup():
    data_path="./106/project/temperatureicecream.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()