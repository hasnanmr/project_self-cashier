# Super Cashier Self Service System
Simple Program Using **Python Language Program** for self checkout supermarket

## Background Projects:
Make a self-service for check out in the supermarket. The customer should input the item quantity and the price by themself for their transaction. The goal is wherever the customer is,  still be able to do their shopping at the supermarket. 

## Requirements Features:
1. Class of Transaction 
2. Some Methods in class: add items, delete an item, reset the order, update an item, show the cart from the order, check out the order and print receipts, and cancel the transaction.
3. Dictionary to save the items from transaction class with transaction ID input
4. Discount when the total transaction is meet the terms and conditions

## Tools:
1. Jupyter Notebook 
2. PyCharm

## Library:
Already available in the **requirement.txt** file


## Flowchart of the program:
![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/1.png "Flowchart")


## Methods Explanation:
1. **add_item**
* input item in cart for every keys as item and values as price and quantity for dict in class Transaction
* could be use multiple times until the meet no condition
2. **delete_item**
* delete item for item already input in a cart of transaction, could be useful when to cancel one of the item already input into the cart 
* could be use multiple times until the meet no condition
3. **update_item**
* update item for item already input in a cart of transaction, could be useful when wrong input the item, price, or quantity.
* could be use multiple times until the meet no condition
4. **show_cart**
* to show the cart in every function that need to be shown
5. **reset_order**
* reset all items that already input in a cart of transaction
6. **receipt**
* final checkout for the transactions for the total payment
 

## Step to run the programme:
1. Clone the repository
2. Deploy your IDE will be the best outcome
3. Install Python minimum 3.7
4. Make sure you install the virtual environment from the requirement.txt file
5. run the python main.py

## Test case
1. **After running the main.py**

![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/1A_.png "Welcome Program")

2. **Add item after input name and transaction ID**

![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/2.png "Add Item into the cart")

3. **If you want to delete item choose option 2**

![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/3.png "delete item from the cart")

4. **If you want to reset the cart of transaction coose option 3**

![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/4.png "reset all item in cart")

5. **If you want to add more item in your cart just after think about the item choose option 5**

![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/5.png "add more item in cart")

6. **If you already finished shopping, go option 4 for checkout your cart**

![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/6.png "checkout print receipt")

7. **If you're not ready for shopping and want to cancel it you can go option 6**

![alt text](https://github.com/hasnanmr/project_self-cashier/blob/main/pictures/7.png "Flowchart")


## Conclusion Suggestion for Future Work
1. Super cashier simple program is build for transaction that input the items, qauntity and price all by the users who is shopping
2. Super cashier simple program is saved with dictionary in it with items as keys and quanitty and price as values
3. For future update, maybe all the item should save in dict, items as keys and price as values so the users only call the keys and input the quantity want to be checkedout
4. For a future update, it may be helpful to include the date of the shopping transaction and save it on local computer with the name and transaction ID that have been inputted on the first run of the program
