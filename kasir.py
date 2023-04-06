import pandas as pd
from termcolor import colored


class Transaction:

    def __init__(self):  # initiation of instance class
        self.transaction = dict()  # Define the empty dict within class Transaction

    # Input_item is method for add item in empty dict of class Transaction
    def input_item(self):
        # show the error from input_item method
        try:
            # Looping the input while True, break with yes or no condition
            while True:
                keys = input("Input item name you want to buy: ").title()  # user input for items as keys in dict
                qty_item = int(input(
                    "Input amount of item you want to buy: ").strip())  # user input for quantity as values in dict
                price_item = int(input(
                    "Input price of item you want to buy : ").strip())  # user input for price as values in dict
                # check whether keys in dict of self.transaction or not
                if keys in self.transaction:
                    # if keys in dict of self.transaction will be executed print
                    print(colored(
                        "\nError! Item already in your order, try to input another items", "red"))
                # if keys not in dict of slf.transaction will be input as new keys and values in dict
                else:
                    self.transaction[keys] = [qty_item, price_item]
                    condition = input(
                        "Do you want to input another items to your cart?(y/n): ").lower()  # break condition "y" or "n"
                    if condition == "n":  # will be printed cart in dataframe and break the method
                        df = pd.DataFrame.from_dict(self.transaction, orient='index',
                                                    columns=['Quantity', 'Price List (Rp)'])
                        print(df.rename_axis('Item(s)').to_markdown())
                        print(colored
                              ("\nYour shopping item(s) have been successfully added to the cart!\n".upper(), "green"))
                        break
                    elif condition == "y":
                        continue
                    else:
                        print(colored("wrong input! please input y or n", "red"))
                        print(colored("\nchoose the add item to input more item to the cart\n", "green"))
                        break
        except ValueError:
            print('You should input as in the instruction')
        except NameError:
            print('only input with number from option')
        except SyntaxError:
            print('wrong syntax')

    # Delete_item is method for delete item in dict of class Transaction as keys input
    def delete_item(self):
        # Looping the input while True, break with yes or no condition
        while True:
            keys = input(
                "Input item name that you want to delete from cart: ").title()  # input for keys that will be deleted
            condition = input(
                "Do you want to delete another item in your cart(y/n): ").lower()  # break condition
            self.transaction.pop(keys)
            if condition == "n":
                df = pd.DataFrame.from_dict(self.transaction, orient='index', columns=['Quantity', 'Price List (Rp)'])
                print(df.rename_axis('Item(s)').to_markdown())
                print(colored("\nYour shopping item(s) have been successfully deleted in the cart!\n".upper(), "green"))
                break
            else:
                continue

    # Update_item is method for updating item in dict of class Transaction as keys input for the mark
    def update_item(self):
        # Looping the input while True, break with yes or no condition
        while True:
            print("Choose from this option\n1. Items\n2. Quantity\n3. Price List\n  Write the number on input below!\n")
            condition = int(input("What do you want to update from your cart: "))
            if condition == 1:
                nama_item_lama = input("Input the item name you want to change: ").title()
                if nama_item_lama in self.transaction:
                    nama_item_baru = input("Input the new item name to be updated: ").title()
                    self.transaction[nama_item_baru] = self.transaction.pop(nama_item_lama)
                else:
                    print(colored("Item(s) not found in your cart", "red"))
            elif condition == 2:
                nama_item = input("Input the item name which you want to change the quantity: ").title()
                if nama_item in self.transaction:
                    jumlah_item_baru = int(input("Input the new quantity to be updated: ").strip())
                    harga_item = self.transaction[nama_item][1]
                    self.transaction[nama_item] = [jumlah_item_baru, harga_item]
                else:
                    print(colored("Item(s) not found in your cart", "red"))
            elif condition == 3:
                nama_item = input("Input the item name which you want to change the price: ").title()
                if nama_item in self.transaction:
                    harga_item_baru = int(input("Input the new price to be updated: ").strip())
                    jumlah_item = self.transaction[nama_item][0]
                    self.transaction[nama_item] = [jumlah_item, harga_item_baru]
                else:
                    print(colored("Item(s) not found in your cart", "red"))
            else:
                print(colored("Invalid, please choose some numbers from the first sentence!", "red"))
            condition_2 = input("Do you still want to update your cart? (y/n): ")
            if condition_2 == "n":
                print(colored("\nYour shopping item(s) have been successfully updated in the cart!\n".upper(), "green"))
                break
            else:
                continue

    # Show_cart is method for show cart as dataframe
    def show_cart(self):
        # convert transaction dictionary to pandas dataframe
        df = pd.DataFrame.from_dict(self.transaction, orient='index', columns=['Quantity', 'Price List/item (Rp)'])

        # calculate total harga for each item
        df['Total Price (Rp)'] = df['Quantity'] * df['Price List/item (Rp)']

        print(df.rename_axis('Item(s)').to_markdown())

    # Reset_order is method for reset all cart in dict of class Transaction
    def reset_order(self):
        self.transaction.clear()
        print(colored("\nAll item have been reset, your cart is empty now!\n".upper(), "green"))
        return

    # Receipt is method for print the receipt of Transaction
    def receipt(self):
        self.show_cart()  # Recall the check_order function

        # calculate total payment
        total_payment = 0  # Define the variable that will be added next in for loop
        # Looping for every keys in dict Transaction to print the total payment
        for key in self.transaction.keys():
            total_payment = total_payment + self.transaction[key][0] * self.transaction[key][1]

        if total_payment >= 200_000:
            worth_more = "more than Rp. 200.000"
            get_disc = "5% discount"
            total_payment = total_payment - round(0.05 * total_payment, 2)
        elif total_payment >= 300_000:
            worth_more = "more than Rp. 300.000"
            get_disc = "8% discount"
            total_payment = total_payment - round(0.08 * total_payment, 2)
        elif total_payment >= 500_000:
            worth_more = "more than Rp. 500.000"
            get_disc = "10% discount"
            total_payment = total_payment - round(0.1 * total_payment, 2)
        else:
            worth_more = "less than Rp 200.000"
            get_disc = "no discount"
            total_payment = total_payment

        print(colored(
            f'\nTotal of your purchase that you need to pay is Rp.{total_payment:,.2f}, because you\'ve got {get_disc} '
            f'for transaction {worth_more}', 'green'))
        print("-----" * 25)