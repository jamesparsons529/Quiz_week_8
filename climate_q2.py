import matplotlib.pyplot as plt
import pandas as pd

climate = pd.read_csv("./climate.csv")

years = []
co2 = []
temp = []

yearsExtract = climate['Year']
for i in yearsExtract:
    years.append(i)
co2Extract = climate['CO2']
for i in co2Extract:
    co2.append(i)
tempExtract = climate['Temperature']
for i in tempExtract:
    temp.append(i)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

