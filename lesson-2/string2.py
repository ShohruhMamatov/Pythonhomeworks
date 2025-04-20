from collections import Counter


txt = 'LMaasleitbtui'
car_names = ['Tesla', 'BMW', 'Audi', 'Toyota', 'Mazda', 'Lamborghini', 'Mercedes']


txt_counter = Counter(txt.lower())


found_cars = []
for car in car_names:
    car_counter = Counter(car.lower())
    if all(txt_counter[char] >= count for char, count in car_counter.items()):
        found_cars.append(car)

if found_cars:
    print("Cars found:", ', '.join(found_cars))
else:
    print("No car names found.")
