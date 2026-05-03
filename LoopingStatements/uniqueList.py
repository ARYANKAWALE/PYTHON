cars = ["lamborghini","subaru","mitsubishi","aston martin","subaru","lamborghini"]
uniquie_car = set()
for vehicle in cars:
    if vehicle in uniquie_car:
        print("Duplicate:",vehicle)
        break
    uniquie_car.add(vehicle)