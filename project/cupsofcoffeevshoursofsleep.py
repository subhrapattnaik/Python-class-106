import plotly_express as px
import csv
#falling graph,data is still colse to the central straight line
with open("./106/project/cupsofcoffeevshoursofsleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
    fig.show()