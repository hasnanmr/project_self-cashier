import pandas as pd
from termcolor import colored

class Transaction:

    def __init__(self):  # initiation of instance class
        self.transaction = dict()

    # Function 1: Input the item in cart for the first time or add more item in dict
    # noinspection PyBroadException
    def input_item(self):
        try:
            while True:
                keys = input("Masukkan nama item yang anda beli: ").title()  # here i have taken keys as strings
                qty_item = int(
                    input("Masukkan jumlah item yang anda beli: ").strip())  # here i have taken values as integers
                price_item = int(input(
                    "Masukkan harga item yang anda beli: ").strip())  # input the price to multiplied with jumlah_item
                if keys in self.transaction:
                    print(
                        "\nError! Item already in your order, coba kembali masukkan dengan nama yang lain jika barangnya"
                        " hampir sama")
                else:
                    self.transaction[keys] = [qty_item, price_item]
                    condition = input(
                        "Apakah anda ingin memasukkan item belanja lagi? (y/n): ").lower()  # break condition if "n" and "y" for continue
                    if condition == "n":
                        df = pd.DataFrame.from_dict(self.transaction, orient='index',
                                                    columns=['Quantity', 'Price List (Rp)'])
                        print(df.rename_axis('Item(s)').to_markdown())
                        print("\nYour shopping item(s) have been successfully added to the cart!\n")
                        break
                    elif condition == "y":
                        continue
                    else:
                        print("wrong input! please input y or n")
                        print("\nchoose the add item to input more item to the cart\n")
                        break
        except:
            print('You should input as in the instruction')

    # Function 2: Delete item already input
    def delete_item(self):
        while True:
            keys = input("Masukkan nama item yang ingin dihapus: ").title()  # input for keys that will be deleted
            condition = input(
                "Apakah anda ingin menghapus item belanja lagi (y/n): ").lower()  # break condition if "n" and "y" for continue
            self.transaction.pop(keys)
            if condition == "n":
                df = pd.DataFrame.from_dict(self.transaction, orient='index', columns=['Quantity', 'Price List (Rp)'])
                print(df.rename_axis('Item(s)').to_markdown())
                print("\nYour shopping item(s) have been successfully deleted in the cart!\n")
                break
            else:
                continue

    # Function 3: Edit or update item already input
    def update_item(self):
        while True:
            print("Choose from this option\n1. Items\n2. Quantity\n3. Price List\n  Write the number on input below!\n")
            condition = int(input("What do you want to update: "))
            if condition == 1:
                nama_item_lama = input("Input the item name you want to change: ").title()
                if nama_item_lama in self.transaction:
                    nama_item_baru = input("Input the new item name to be updated: ").title()
                    self.transaction[nama_item_baru] = self.transaction.pop(nama_item_lama)
                else:
                    print("Item tidak ditemukan dalam transaksi")
            elif condition == 2:
                nama_item = input("Input the item name which you want to change the quantity: ").title()
                if nama_item in self.transaction:
                    jumlah_item_baru = int(input("Input the new quantity to be updated: ").strip())
                    harga_item = self.transaction[nama_item][1]
                    self.transaction[nama_item] = [jumlah_item_baru, harga_item]
                else:
                    print("Item tidak ditemukan dalam transaksi")
            elif condition == 3:
                nama_item = input("Input the item name which you want to change the prize: ").title()
                if nama_item in self.transaction:
                    harga_item_baru = int(input("Input the new prize to be updated: ").strip())
                    jumlah_item = self.transaction[nama_item][0]
                    self.transaction[nama_item] = [jumlah_item, harga_item_baru]
                else:
                    print("Item tidak ditemukan dalam transaksi")
            else:
                print("Invalid, please choose some numbers from the first sentence!")
            condition_2 = input("Apakah masih ingin update(y/n): ")
            if condition_2 == "n":
                print("\nYour shopping item(s) have been successfully updated in the cart!\n")
                break
            else:
                continue

    # Function 4: Check the order in cart dictionary
    def show_cart(self):
        # convert transaction dictionary to pandas dataframe
        df = pd.DataFrame.from_dict(self.transaction, orient='index', columns=['Quantity', 'Price List/item (Rp)'])

        # calculate total harga for each item
        df['Total Price (Rp)'] = df['Quantity'] * df['Price List/item (Rp)']

        print(df.rename_axis('Item(s)').to_markdown())

    # Function 5: Reset all order in cart
    def reset_order(self):
        self.transaction.clear()
        return ("\nAll item have been reset, your cart is empty now!\n")

    # Function6: Print receipt in cart or for check out the order
    def receipt(self):
        self.show_cart()  # Recall the check_order function

        # calculate total payment
        total_payment = 0
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
            f'\nTotal of your purchase is Rp.{total_payment:,.2f}, because you\'ve got {get_disc} for transaction {worth_more}', 'green'))

        print("-----" * 25)