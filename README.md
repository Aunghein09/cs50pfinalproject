---
Title: "CS50P Final Project"
Author: "Kyar-Hsing Ma"
Date: 2022/08/27
---

# CS50P Final Project
## Project Description
This final project is a demo program that simulates how items are registered, stored and updated in a shop in association with barcodes.

The item data are store in a csv file name "inventory.csv".

The barcode type that is used here is EAN13.

With this program, new items can be added, old ones can be restocked, checked or sold. (with flag -a, -r, -c, -s respectively).

When a new item is added, a jpg file of a new barcode will be stored in the barcode/ directory.

The items in the inventory can be accessed by  barcode EAN13 number or item name, barcode jpg. The latter is used to simulate the real barcode scanner.

With no input, the check mode return the entire inventory table. But with item being mentioned, a table for the specific item is returned.

Restock and Sale mode will update the inventory accordingly if items are available.

##project.**main**

<p class="func-header">
    <i>def</i> project.<b>main</b>(<i></i>) <a class="src-href" target="_blank" href="https://github.com/Aunghein09/cs50pfinalproject/blob/main/project.py#L24">[source]</a>
</p>
