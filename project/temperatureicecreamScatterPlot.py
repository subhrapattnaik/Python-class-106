import plotly_express as px
import csv
#data is highly corelated. when the temp increaes ,the sale of ice-cream goes up
with open("./106/project/temperatureicecream.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Temperature", y="Ice-cream-Sales")
    fig.show()


#where as, temp vs sale of warm clothes in a store are inversely corelated

