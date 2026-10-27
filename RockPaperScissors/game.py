pick = {'rock', 'paper', 'scissors'}

def tie(cl):
    uni = set(cl)

    if len(uni) == 1:
        return "It's a tie!"
    if len(uni) == 3:
        return "It's a tie! All three cancel each other out!"
    return "Someone won!"

print("Welcome to Rock, Paper, Scissors game!")
input("Press Enter To play")

print("1. 2 players\n2. 3 players")

while True:
    try:
        choice = int(input("Choose how many Players (1 or 2): "))
        if choice in [1, 2]:
            break
        print("Please choose 1 or 2.")
    except ValueError:
        print("Please enter a valid number.")

# Choice 1 = 2 Players
if choice == 1:
    while True:
        p = input("Enter first choice: ").lower().strip()
        q = input("Enter second choice: ").lower().strip()
        if p in pick and q in pick:
            result = tie([p, q])
            print(result)
            break
        else:
            print("Invalid choice detected! Please enter 'rock', 'paper', or 'scissors'.\n")

# Choice 2 = 3 Players
elif choice == 2:
    while True:   
        p1 = input("Enter First player choice: ").lower().strip()
        p2 = input("Enter Second player choice: ").lower().strip()
        p3 = input("Enter Third player choice: ").lower().strip()
        if p1 in pick and p2 in pick and p3 in pick:
            result = tie([p1, p2, p3])
            print(result)
            break
        else:
            print("Invalid choice detected! Please enter 'rock', 'paper', or 'scissors'.\n")