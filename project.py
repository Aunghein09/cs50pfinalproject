import pandas as pd
import cv2
from pyzbar.pyzbar import decode
import sys
import re
from barcode import EAN13
from barcode.writer import ImageWriter
import random
from tabulate import tabulate

"""
This final project is an program that simulates how items are registered and stored in a shop using barcode.
The item data are store in a csv file name "inventory.csv".
The barcode type that is used here is EAN13.
With this program, a new item can be added, old ones can be restocked, chekced or sold. (with flag -a, -r, -c, -s respectively)
When a new item is added, a jpg file of a new barcode will be stored in the barcode/ directory
These jpg files can be used to mark or stick at the corresponding items and are also used to simulate the image capture from a real barcode scanner.
The items in the inventory can be accessed by barcode jpg, barcode EAN13 number or item name.
With no input, the check mode return the entire inventory table. But with item being mentioned, a table for the specific item is returned.
Restock and sales mode will update the inventory accordingly if items are available.
"""
def main():
    dataframe = pd.read_csv("inventory.csv")
    if len(sys.argv) != 2:
        sys.exit(
            "Please run the prgramm mentioning a mode python shop.py -[mode]\n mode -a for add item\t -r for restock item\t -s for sell item\t -c for check item"
        )

    elif sys.argv[1] == "-a":
        add_item(dataframe)

    elif sys.argv[1] == "-r":
        flag = "y"
        while flag == "y":
            item = input("Item to restock: ")
            amt = int(input("Amount: "))
            try:
                cost = restock(item, amt, dataframe)
            # image is not barcode, no such item in inventory
            except (IndexError, TypeError):
                print("Item does not exist")
                flag1 = input("Add item instead? Please answer y or n: ")
                if flag1 == "y":
                    add_item(dataframe)
                else:
                    sys.exit("Please come again when you want to restock")
            flag = input("Restock More Item? Please answer y or n: ")

    elif sys.argv[1] == "-s":
        total_cost = []
        flag = "y"
        while flag == "y":
            item = input("Item to sell: ")
            amt = int(input("Amount: "))
            try:
                cost = sell_item(item, amt, dataframe)
                total_cost.append(cost)
            # image is not barcode, no such item in inventory
            except (IndexError, TypeError):
                print("Item does not exist")
            flag = input("Sell More Item? Please answer y or n: ")
        print(f"Your Total: ${sum(total_cost):.2f}")

    elif sys.argv[1] == "-c":
        dataframe = pd.read_csv("inventory.csv")
        item = input("Which item do you want to check: ")
        if item:
            try:
                code = get_barcode(item,dataframe)
                df1 = dataframe[dataframe.Item_code == code]
                print(tabulate(df1,headers='keys', tablefmt = 'psql'))
            except (IndexError, TypeError):
                print("Item does not exist")
            
        else:
            print(tabulate(dataframe,headers='keys', tablefmt = 'psql'))


    else:
        sys.exit(
            "Please run the prgramm mentioning a mode python shop.py -[mode]\n mode -a for add item\t -r for restock item\t -s for sell item"
        )


def checksum(s):
    """
    Calculate checksum from 12 digits of EAN

    Args:
        s (str): first 12 digits of EAN13

    Returns:
        (int) :the last checksum number of EAN-13
    """
    odd_int = map(int, s[0::2])
    odd_sum = sum(odd_int)
    even_int = map(int, s[1::2])
    even_sum = sum(even_int) * 3
    return (10 - (odd_sum + even_sum) % 10) % 10


def make_barcode(item, df):
    """
    Produce barcode and save it in a file called barcode as jpeg files and give back the EAN 13 number

    Args:
        item (str): item name
        df (pd.dataframe) : dataframe of csv file

    Returns:
        ean13 (str): The 13 digit EAN13 number
    """
    while True:
        ean13 = ""
        # generate 12 digits
        for _ in range(12):
            ean13 += str(random.randint(0, 9))
        # get checksum and append it to be 13 digits
        ean13 += str(checksum(ean13))
        if not int(ean13) in df["Item_code"].values:
            break
    # save the barcode as an image  file in bardcode directory
    with open(f"barcode/{item}.jpg", "wb") as f:
        EAN13(ean13, writer=ImageWriter()).write(f)
    return ean13


def get_barcode(item, df):
    """
    Get the item_code or bar_code from 'inventory.csv' where data are stored

    Args:
        item (str):
            Image file name
            EAN13 code
            Item name
            (re will check for the input and handle differently)
        df (pd.dataframe) : dataframe of csv file
    Returns:
        13-digit EAN integer
    """
    # jpeg file
    if re.search(r".*\.jpg$", item):
        # loads the image file, if file not available return None
        img = cv2.imread(f"barcode/{item}")
        # decode the loaded img, will raise error if the img value is None
        barcode = decode(img)
        # return the 13 EAN digit if the img is contains a bar code, else raise indexError
        return int(barcode[0].data.decode("utf-8"))
    # 13 digit number
    elif re.search(r"\d{13}$", item):
        return int(item)
    # others item name expected, else or not exist-> index error
    else:
        return df.loc[df.Name == item, "Item_code"].values[0]


def add_item(df):
    """
    Add item/ items to the inventory.csv has built-in iteration

    Args:
        df (pd.dataframe) : dataframe of csv file

    Returns:
        No return value
    """
    flag = "y"
    while flag == "y":
        item = []
        name = input("Name: ").lower()
        item.append(name)
        item.append(make_barcode(name, df))
        while True:
            try:
                item.append(int(input("Quantity: ")))
                break
            except ValueError:
                print("please enter an integer")
        while True:
            try:
                item.append(float(input("Price: ")))
                break
            except ValueError:
                print("please enter an number")

        df.loc[len(df)] = item

        flag = input("Add More Item? Please answer y or n: ")

    df.to_csv("inventory.csv", index=False)
    print("Successfully added.")


def get_quantity(bcode, df):
    """
    Get the quantity of the specific item

    Args:
        bcode (int): EAN13 from get_barcode function
        df (pd.dataframe) : dataframe of csv file

    Returns:
        (int): quantity of item from dataframe

    """
    return df.loc[df.Item_code == bcode, "Quantity"].values[0]


def get_price(bcode, df):
    """
    Get the quantity of the specific item

    Args:
        bcode (int): EAN13 from get_barcode function
        df (pd.dataframe) : dataframe of csv file

    Returns:
        (float): price of item from dataframe

    """
    return df.loc[df.Item_code == bcode, "Price"].values[0]




def sell_item(item, amount, df):
    """
    check the availability of item, update the quantity in the table, return the cost of the item

    Args:
        item (str):
            Image file name
            EAN13 code
            Item name
            (re will check for the input and handle differently)
        amount(int): amount to sell
        df (pd.dataframe) : dataframe of csv file

    Returns:
        (float): cost of the item (price * quantity)
    """
    # expect to get type error or value error if there is no such item in the inventory
    code = get_barcode(item, df)
    items_amount = get_quantity(code, df)
    # compare the quantity
    if amount > items_amount:
        print("Not enough items left")
        return 0
    else:
        df = pd.read_csv("inventory.csv")
        df.loc[df["Item_code"] == code, "Quantity"] = items_amount - amount
        df.to_csv("inventory.csv", index=False)
        return get_price(code, df) * amount


def restock(item, amount, df):
    """
    check the availability of item, update the quantity in the table

    Args:
        item (str):
            Image file name
            EAN13 code
            Item name
            (re will check for the input and handle differently)
        amount(int): amount to restock
        df (pd.dataframe) : dataframe of csv file

    """
    # expect to get type error or value error if there is no such item in the inventory
    code = get_barcode(item, df)
    items_amount = get_quantity(code, df)

    df.loc[df["Item_code"] == code, "Quantity"] = items_amount + amount
    df.to_csv("inventory.csv", index=False)
    print("Successfully restocked")


if __name__ == "__main__":
    main()
