temperature = [[-8,-14,-19,-18],[25,28,26,20],[11,18,20,25]]
two_day_temperatures=[]
for station in temperature:
    two_day_temperatures.append(station[1])
print("Показания термометров за 2-ой день:",two_day_temperatures)