# CS50P Final Project (Inventory)
#### Video Demo:  <URL https://l.facebook.com/l.php?u=https%3A%2F%2Fyoutu.be%2Fx4FRpwIUt80&h=AT1bofBzco3-uA7pUDswxzm0yyAA3iHmMYnSXpbavOqfaX_vP7EV30mE-2glu9F47AxTu1Y_5iwJMMh3caKJNkYBunaa4C-f3176kcCs_0sZ1nHSpvNHkmNjQzh3PnlbsjZ2&s=1>

**Author: "Kyar-Hsing Ma"**

**Date: 2022/08/27**

## **CS50P Final Project (Inventory)**
#### Project Description
This final project is a demo program that simulates how items are registered, stored and updated in a shop in association with barcodes.

The item data are store in a csv file name "inventory.csv".

The barcode type that is used here is EAN13.

With this program, new items can be added, old ones can be restocked, checked or sold. (with flag -a, -r, -c, -s respectively).

When a new item is added, a jpg file of a new barcode will be stored in the barcode/ directory.

The items in the inventory can be accessed by  barcode EAN13 number or item name, barcode jpg. The latter is used to simulate the real barcode scanner.

With no input, the check mode return the entire inventory table. But with item being mentioned, a table for the specific item is returned.

Restock and Sale mode will update the inventory accordingly if items are available.

## project.**main**

<p class="func-header">
    <i>def</i> project.<b>main</b>(<i></i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L24">[source]</a>
</p>

## Example codes
Cmd Input
```

python projec.py

```
Output:
```

Welcome to the Inventory        (CS50P Porject by Kyar-Hsing Ma)
Please run the prgramm mentioning a mode python project.py -[mode]
 mode -a for add item    -r for restock item     -s for sell item        -c for check item

```
Without flag the prgram will not run and prompt the user to include a flag
### Check Mode
```
python project.py -c

```
Output:
```
Which item do you want to check:
+----+--------+---------------+------------+---------+
|    | Name   |     Item_code |   Quantity |   Price |
|----+--------+---------------+------------+---------|
|  0 | sample | 5005154439282 |         10 |     100 |
+----+--------+---------------+------------+---------+
```
Without specific item mentioned, the prgram will return all the items in the inventory.

### Add Mode
```
python project.py -a
```

Output:

```
Welcome to the Inventory        (CS50P Porject by Kyar-Hsing Ma)
Name: apple
Quantity: 50
Price: 2
Add More Item? Please answer y or n: y
Name: orange
Quantity: 20
Price: 1.5
Add More Item? Please answer y or n: n
Successfully added.
```

```
python project.py -c
```
Output:

```
Welcome to the Inventory        (CS50P Porject by Kyar-Hsing Ma)
Which item do you want to check:
+----+--------+---------------+------------+---------+
|    | Name   |     Item_code |   Quantity |   Price |
|----+--------+---------------+------------+---------|
|  0 | sample | 5005154439282 |         10 |   100   |
|  1 | apple  | 8780654645339 |         50 |     2   |
|  2 | orange | 1768047085266 |         20 |     1.5 |
+----+--------+---------------+------------+---------+
```

### Restock Mode

'''
python project.py -r
'''

Output:

```
Welcome to the Inventory        (CS50P Porject by Kyar-Hsing Ma)
Item to restock: apple
Amount: 100
Successfully restocked
Restock More Item? Please answer y or n: n
```

```
python project.py -c
```
Output:

```
Welcome to the Inventory        (CS50P Porject by Kyar-Hsing Ma)
Which item do you want to check:
+----+--------+---------------+------------+---------+
|    | Name   |     Item_code |   Quantity |   Price |
|----+--------+---------------+------------+---------|
|  0 | sample | 5005154439282 |         10 |   100   |
|  1 | apple  | 8780654645339 |        150 |     2   |
|  2 | orange | 1768047085266 |         20 |     1.5 |
+----+--------+---------------+------------+---------+
```
Apple is updated.

### Sell Mode

```
python project.py -s
```

Output:

```
Welcome to the Inventory        (CS50P Porject by Kyar-Hsing Ma)
Item to sell: apple
Amount: 20
Sell More Item? Please answer y or n: y
Item to sell: orange.jpg
Amount: 10
Sell More Item? Please answer y or n: n
Your Total: $55.00
```
Return the total cost and update the values

```
python project.py -c
```
Output:

```
Welcome to the Inventory        (CS50P Porject by Kyar-Hsing Ma)
Which item do you want to check:
+----+--------+---------------+------------+---------+
|    | Name   |     Item_code |   Quantity |   Price |
|----+--------+---------------+------------+---------|
|  0 | sample | 5005154439282 |         10 |   100   |
|  1 | apple  | 8780654645339 |        130 |     2   |
|  2 | orange | 1768047085266 |         10 |     1.5 |
+----+--------+---------------+------------+---------+
```

The following are some description of the functions in this program.
## project.**checksum**

<p class="func-header">
    <i>def</i> project.<b>checksum</b>(<i>s</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L87">[source]</a>
</p>

Calculate checksum from 12 digits of EAN

Args:

    s (str): first 12 digits of EAN13

Returns:

    (int) :the last checksum number of EAN-13


## project.**make_barcode**

<p class="func-header">
    <i>def</i> project.<b>make_barcode</b>(<i>item, df</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L104">[source]</a>
</p>

Produce barcode and save it in a file called barcode as jpg files and give back the EAN 13 number

Args:

    item (str): item name
    df (pd.dataframe) : dataframe of csv file

Returns:

    ean13 (str): The 13 digit EAN13 number

## project.**get_barcode**

<p class="func-header">
    <i>def</i> project.<b>get_barcode</b>(<i>item, df</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L130">[source]</a>
</p>

Get the item_code or bar_code from 'inventory.csv' where data are stored

Args:

    item (str):
        Image file name(.jpg)
        EAN13 code(13-digit code)
        Item name
        (re will check for the input and handle differently)
    df (pd.dataframe) : dataframe of csv file
Returns:

    (int) 13-digit EAN integer

## project.**add_item**

<p class="func-header">
    <i>def</i> project.<b>add_item</b>(<i>df</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L160">[source]</a>
</p>

Add item/ items to the inventory.csv has built-in iteration

Args:

    df (pd.dataframe) : dataframe of csv file

Returns:

    None

## project.**get_quantity**

<p class="func-header">
    <i>def</i> project.<b>get_quantity</b>(<i>bcode, df</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L197">[source]</a>
</p>

Get the quantity of the specific item

Args:

    bcode (int): EAN13 from get_barcode function
    df (pd.dataframe) : dataframe of csv file

Returns:

    (int): quantity of item from dataframe




## project.**get_price**

<p class="func-header">
    <i>def</i> project.<b>get_price</b>(<i>bcode, df</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L212">[source]</a>
</p>

Get the quantity of the specific item

Args:

    bcode (int): EAN13 from get_barcode function
    df (pd.dataframe) : dataframe of csv file

Returns:

    (float): price of item from dataframe

## project.**sell_item**

<p class="func-header">
    <i>def</i> project.<b>sell_item</b>(<i>item, amount, df</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L229">[source]</a>
</p>

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

    (float): cost of the item: price * quantity

## project.**restock**

<p class="func-header">
    <i>def</i> project.<b>restock</b>(<i>item, amount, df</i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L259">[source]</a>
</p>

check the availability of item, update the quantity in the table

Args:

    item (str):
        Image file name
        EAN13 code
        Item name
        (re will check for the input and handle differently)
        amount(int): amount to restock
        df (pd.dataframe) : dataframe of csv file

Returns:

    None
