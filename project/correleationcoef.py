import plotly.express as px
import csv
import numpy as np


temperature=[]
ice_cream_sales=[]
    
with open("./temperatureicecream.csv") as csv_file:
  csv_reader=csv.DictReader(csv_file)
  
  
  for row in csv_reader:
     temperature.append(float(row["Temperature"]))
     ice_cream_sales.append(float(row["Ice-cream-Sales"]))

correlation=np.corrcoef(temperature,ice_cream_sales)
print("Correlation between Temperature vs Ice cream Sales:-",correlation[0,1])

