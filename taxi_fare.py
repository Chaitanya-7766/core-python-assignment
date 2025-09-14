def distance_fare(trip):
    return trip*10
base_fare=50
trips=[5,10,3]
for i in range(len(trips)):
    print(f"Trip {i+1}: $"+f"{distance_fare(trips[i])+base_fare}")