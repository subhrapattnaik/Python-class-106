import plotly.express as px
import csv

with open("./106/project/sizeoftvvstimespentwatching.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="SizeofTV",y="AveragetimespentwatchingTVinaweekhours")
    fig.show()