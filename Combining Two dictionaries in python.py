#Combining Two dictionaries in python

race_cars={"Ferrarri Roma":247310,"Porsche":106100}
electric_cars={"Tesla model 3":41000,"BMW i4":53000,"Nissan Leaf":28000}

#looping using 2 for loops (not ideal)
cars={}

for car,price in race_cars.items():
    cars[car]=price

for car,price in electric_cars.items():
    cars[car]=price

print(cars)

#another way is to use update() function instead 
cars={}
#this function inserts all of the keys from dictionary into a new one thus avoiding use of loops
cars.update(race_cars)
cars.update(electric_cars)
print(cars)


#If u are using python 3.9 ownwards u can use pipe operator '|'

cars={}
cars=race_cars | electric_cars
print(cars)
