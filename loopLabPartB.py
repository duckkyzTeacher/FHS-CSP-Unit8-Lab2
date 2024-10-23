parking_time = 10  # 10 minutes remaining on the meter

coin_inserted = False

print("Parking meter started. Time remaining:")

while parking_time >= 0:
    print(f"{parking_time} minutes left.")

    if parking_time % 2 == 0:
        parking_time += 1    

    if coin_inserted:
        parking_time += 5  # Add 5 more minutes if a coin is inserted
        coin_inserted = False  # Reset after coin is used

print("Parking time expired. Please insert more coins.")
