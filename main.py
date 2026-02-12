# Perfomrance Task

# manages the menu telling loop and user interation
def run_coffee_menu(coffee_menu):
    active = True
    # determines whether loops stays open and running or not
    while active: 
        # if empty list, no menu to show
        if not coffee_menu:
            print("Sorry, we don't carry that.")
            break

print(f"We do carry these drinks though: {coffee_menu}")
# displays what drink coffee shop has to offer
choice = input("Would you like to order anything? If not, type 'no' :").strip().lower()
# gives user the option of ordering something off the menu

if choice == 'no'
# loop is exited
    active = False
    break

elif choice in coffee_menu:
    # checls if users choice is availibe in the menu
    if choice == "Iced latte"
    tell_customer("Ok, we can do that!")
elif choice == "Americano"
    tell_customer("Ok, we can do that!")
elif choice == "Cappuccino"
    tell_customer("Ok, we can do that")

    def tell_customer(setup, punchline)

