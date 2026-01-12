# A simple daily routine decision 

while True:
    print("\n=== Daily Routine Decision ===")


    #ask daily routine question
    sleep_hours = int(input("How many hours did you sleep last night? (Enter a number): "))
    had_breakfast = input("Did you eat breakfast today? (yes/no): ").lower()
    exercised = input("Did you exercise today? (yes/no): ").lower()


    # Decision making logic
    if sleep_hours >= 8 and had_breakfast == "yes" and exercised == "yes":
        print("You're off to a great start today! Keep it up!")
    elif sleep_hours < 6 and had_breakfast == "no":
        print("You should consider getting more sleep and grab something to eat to recharge.")
    elif exercised == "no":
        print("Try to fit in some exercise today for better health!")
    else:
        print("You're doing okay, but there's always room for improvement! ")

    
    # Ask to continue or exit
    again = input("\nWould you like to evaluate another day? (yes/no): ").lower()
    if again != "yes":
        print("Take care and have a great day!")
        break