import os

def weather():
    while True:
        try:  
            distance = int(input("How many miles are you traveling? "))
            if distance < 0:
                print("Distance cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter numbers only!")

    while True:
        rain = input("Is it raining?\nYes\nNo\n> ").lower().strip()
        if rain in ["yes", "no"]:
            break
        print("Please type 'yes' or 'no'!")
        
    while True:
        try:
            tran = int(input("How are you traveling?\n1. On Foot\n2. Bike\n3. Car / Ride-Share\n> "))
            if tran in [1, 2, 3]:
                break
            print("Please choose 1, 2, or 3!")
        except ValueError:
            print("Please enter a valid number (1, 2, or 3)!")

    return {
        "rain": rain,
        "distance": distance,
        "tran": tran
    }


def checking(trip):
    if trip["distance"] == 0:
        print("You don't need to travel anywhere!")
        return

    if trip["tran"] == 3:
        print("You can go out!")
    elif trip["distance"] <= 1 and trip["rain"] == "no":
        print("You can go out!")
    elif 1 < trip["distance"] <= 6 and trip["tran"] == 2 and trip["rain"] == "no":
        print("You can go out!")
    else:
        print("You cannot go out!")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TRAVEL WEATHER PLANNER ===")
    trip = weather()
    print("\n--- Result ---")
    checking(trip)
    print("--------------\n")

    input("Press Enter to test another trip...")