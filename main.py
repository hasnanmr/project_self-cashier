from kasir import Transaction
from termcolor import colored

name = input("Input your name = ").title()
transaction_id = input("Input your transaction id: ").lower()  # make an instance object with user input

# create an instance of Transaction and save it under the user-specified name
transaction = {transaction_id: Transaction()}

# Print the pop out welcome to the simple program
print(colored(f"\n..........Welcome {name}, Happy Shopping!.........", "blue"))
print(colored("\n...........Welcome to the SelfMart.................", "green"))
print(colored(f"\n...........This is cart for {transaction_id}.................\n", "green"))

# start with input item into cart
transaction[transaction_id].input_item()

while True:
    try:
        # Print the option
        print(colored(
            "These are self service for Check Out your order\n ",
            "blue"))
        print("-----" * 20)
        print(
            colored("1. Edit Item\n2. Delete Item\n3. Reset item\n4. Print Receipt\n5. Add More Item\n6. Cancel Transaction\n", "green"))
        menu = int(input(colored("Input a number based on the option above: ", "green").strip()))
        print("-----" * 25)

        # Main if, running the functions from store.py based on the user input
        if menu == 1:
            # Checking whether the item already inputted or not
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM TO BE UPDATED\n", "red"))
                print(colored("\nYou need to choose Add More Item\n", "blue"))

            # If the item already inputted, we run the function update_item
            else:
                transaction[transaction_id].show_cart()
                transaction[transaction_id].update_item()

        elif menu == 2:
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM TO BE DELETED\n", "red"))
                print(colored("\nYou need to choose add more item\n", "blue"))

            # If the item already inputted, we run the function update_item
            else:
                transaction[transaction_id].delete_item()

        elif menu == 3:
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM IN YOUR CART\n", "red"))
                print(colored("\nYou need to choose add more item\n", "blue"))
            # If the item already inputted, we run the function update_item
            else:
                transaction[transaction_id].reset_order()
                transaction[transaction_id].show_cart()

        elif menu == 4:  # Method receipt called
            # Check if there is any order in cart
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM IN YOUR CART TO BE PAID\n", "red"))
                print(colored("\nYou need to choose add more item\n", "blue"))
            # If there is any, we can called receipt method
            else:
                transaction[transaction_id].receipt()
                print(colored(f"Thank you for shopping {name}, we are looking forward to see you back soon", "green"))
                break

        elif menu == 5:
            print(colored("\nIn this option you will add more item in your cart\n".upper(), "green"))
            transaction[transaction_id].show_cart()
            transaction[transaction_id].input_item()

        elif menu == 6:
            print((colored(f"Thank you for shopping {name}, we are looking forward to see you back soon".title(),
                           "blue")))
            break

    except NameError:
        print('only input with number from option')
    except SyntaxError:
        print('wrong syntax')
    except ValueError:
        print('input by number from option')
