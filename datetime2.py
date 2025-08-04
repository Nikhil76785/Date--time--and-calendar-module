def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if ("New York" == city):
        return 183
    elif ("Tampa" == city):
        return 220
    elif ("Texas" == city):
        return 222
    elif ("Los Angeles" == city):
        return 475

def rent_car_cost(days):
    if (days >= 7):
        return 40 * days - 50
    elif (days >= 3):
        return 40 * days - 20
    else:
        return 40 * days
    
def trip_cost(city, days, spending_money):
    return rent_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of the car rent: ", rent_car_cost(6))
print("Cast of the plane ride: ", plane_ride_cost("Los Angeles"))
print("Cost of hotel room: ", hotel_cost(6))
print("Total cost of trip: ", trip_cost("Los Angeles", 6, 7500))
print(trip_cost("Tampa", 6, 6500))