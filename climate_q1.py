import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

connection = sqlite3.connect(r'./climate.db')
cursor = connection.cursor()

cursor.execute("SELECT Year FROM ClimateData")
yearsResult = cursor.fetchall()
for i in yearsResult:
    years.append(i)

cursor.execute("SELECT CO2 FROM ClimateData")
co2Result = cursor.fetchall()
for i in co2Result:
    co2.append(i)

cursor.execute("SELECT Temperature FROM ClimateData")
tempResult = cursor.fetchall()
for i in tempResult:
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
plt.savefig("co2_temp_1.png") 
