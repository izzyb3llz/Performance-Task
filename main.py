# Performance Task

# manages the menu telling loop and user interation
def coffee_menu(menu):
    if not menu:
        print("Sorry, we don't carry anything right now.")
        return None

    print(f"We do carry these drinks: {menu}")
    # displays what drink coffee shop has to offer
    choice = input("What would you like to order? (type 'no' to exit): ").strip().lower()
    # gives user the option of ordering something off the menu
    if choice == "no":
    # loop is exited
        print("Okay, goodbye!")
        return None
    
    return choice


def tell_customer(menu, choice, get_rating):
    if choice.capitalize() in menu:
    # checks if users choice is availibe in the menu
        print("Ok, we can do that!")
    else:
        print("Sorry, we don't carry that.")
        return

    remove_choice = input("Is there a drink you'd like removed from the menu? ").lower()
    # askes user if theres a menu option they would not like.
    if remove_choice in menu:
    #removes existing menu option
        menu.remove(remove_choice)
        print(f"Okay, {remove_choice} removed. Updated menu: {menu}")
    else:
        print("Sorry, that item isn't on the menu.")
    # Tells customer what they want isn't a menu option.
    
    get_rating()
   # calls the function for user feedback
    another = input("Would you like something else? (yes/no): ").lower()
    if another == "yes":
        print("Okay, let's continue.")
    else:
        print("Okay, bye bye!")
        return
    remove_choice = input("Is there a drink you'd like removed from the menu? ").lower()

    if remove_choice in menu:
    # removes existing menu option
        menu.remove(remove_choice)
        print(f"Okay, {remove_choice} removed. Updated menu: {menu}")
    else:
        print("Sorry, that item isn't on the menu.")
   # Tells customer what they want isn't a menu option

def get_rating():
    rating = input("How was your experience today (1–5)? ")
    print(f"Thanks for rating us {rating}!")


# Example usage:
menu = ["Iced latte", "Americano", "Cappuccino"]
choice = coffee_menu(menu)

if choice:
    tell_customer(menu, choice, get_rating)
# tells customer menu/choices.
