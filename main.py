from checkout import Transaction
from termcolor import colored


name = input("Input your name = ").title()  # user input the name to know who is shopping
transaction_id = input("Input your transaction id: ").lower()  # save the transaction id fot an instance object

# create an instance of Transaction with transaction id has been inputted
transaction = {transaction_id: Transaction()}

# Print the pop out welcome to the simple program
print(colored(f"\n..........Welcome {name}, Happy Shopping!.........".upper(), "blue"))
print(colored("\n...........Welcome to the SelfMart.................".upper(), "green"))
print(colored(f"\n...........This is transaction for cart id {transaction_id}.................\n".upper(), "green"))

# start with input item into cart of under the user-specified name
transaction[transaction_id].input_item()

# looping the main menu for transaction
while True:
    try:
        # Print the option
        print(colored(
            "These is self service for Check Out your order\n".title(),
            "blue"))
        print("-----" * 20)
        print(
            colored("1. Edit Item\n2. Delete Item\n3. Reset item\n4. Print Receipt\n5. Add More Item\n6. Cancel Transaction\n", "green"))
        menu = int(input(colored("Enter from the option above : ", "green").strip()))
        print("-----" * 25)

        # Here will run update_item method from kasir.py if the input above is 1
        if menu == 1:
            # Checking whether the item already inputted or not
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM TO BE UPDATED\n", "red"))
                print(colored("\nYou need to choose Add More Item\n", "blue"))

            # If the item already inputted, then will call the update_item from kasir.py
            elif transaction[transaction_id].transaction:
                transaction[transaction_id].show_cart()
                continue_update = input(colored(  # condition continue update after see in the cart
                    "\nDo you want to continue update item(s) in your cart?(y or n): ", "green")).lower()
                if continue_update == "y":
                    transaction[transaction_id].update_item()
                elif continue_update == "n":
                    pass
                else:
                    raise NameError

        # Here will run delete_item method from kasir.py if the input above is 2
        elif menu == 2:
            # Checking whether the item already inputted or not
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM TO BE DELETED\n", "red"))
                print(colored("\nYou need to choose add more item\n", "blue"))
            # If the item already inputted, then will call the delete_item method from kasir.py
            elif transaction[transaction_id].transaction:
                transaction[transaction_id].show_cart()
                continue_delete = input(colored(  # condition continue update after see in the cart
                    "\nDo you want to continue delete item(s) in your cart?(y or n): ", "green")).lower()
                if continue_delete == "y":
                    transaction[transaction_id].delete_item()
                elif continue_delete == "n":
                    pass
                else:
                    raise NameError

        # Here will run reset_order method from kasir.py if the input above is 3
        elif menu == 3:
            # Checking whether the item already inputted or not
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM IN YOUR CART\n", "red"))
                print(colored("\nYou need to choose add more item\n", "blue"))
            # If the item already inputted, then will call the reset_order method from kasir.py
            else:
                transaction[transaction_id].reset_order()
                transaction[transaction_id].show_cart()

        # Here will run receipt method from kasir.py if the input above is 4
        elif menu == 4:  # Method receipt called
            # Checking whether the item already inputted or not
            if not transaction[transaction_id].transaction:
                print(colored("\nTHERE IS NO ITEM IN YOUR CART TO BE PAID\n", "red"))
                print(colored("\nYou need to choose add more item\n", "blue"))
            # If there is any, then will call receipt method from kasir.py
            else:
                transaction[transaction_id].receipt()
                print(colored(f"Thank you for shopping {name}, we are looking forward to see you back soon", "green"))
                break

        # Here will run input_item method from kasir.py if the input above is 5 for input more item
        elif menu == 5:
            print(colored("\nIn this option you will add more item in your cart\n".upper(), "green"))
            transaction[transaction_id].show_cart()  # show the cart of transaction before add more item
            continue_add_item = input(colored(  # condition continue update after see in the cart
                "\nDo you want to continue add more item in your cart?(y or n): ", "green")).lower()
            if continue_add_item == "y":
                transaction[transaction_id].input_item()  # call input_item method from kasir.py for input more item
            elif continue_add_item == "n":
                pass
            else:
                raise NameError

        # Here will break the loop from main menu before checkout your shopping, or cancel the transaction
        elif menu == 6:
            print((colored(f"Thank you for come to SelfMart {name}, we are looking forward to see you back soon".title(),
                           "blue")))
            break

    except NameError:
        print(colored('Wrong input should be y or no', 'red'))
    except SyntaxError:
        print(colored('Wrong syntax', 'red'))
    except ValueError:
        print(colored('input by number from option', 'red'))