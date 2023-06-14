num=int(input("enter a number category:"))
dict={}
for i in range(num):
    category=input("enter a category :")
    product=input("enter a product :")
    vendor=input("enter a vendor:")
    qty=int(input("enetr a qut:"))
    if category in dict:
        if product in dict[category]:
            if vendor in dict[category][product]:
                old_qty = dict[category][product][vendor]['qty']
                print('old_qty',qty)
                dict.update({category:{product:{vendor:{"qty":old_qty+qty}}}})
            else:
                dict[category][product].update({vendor:{'qty':qty}})
                print(".......else.....",dict)
        else:
            dict[category].update({product:{vendor:{'qty':qty}}})
            print("product.....else",dict)
    else:
        dict.update({category:{product:{vendor:{'qty':qty}}}})
    print(dict)
print(".................")
customer=(input("enter a number customer:"))
category=input("enter a category type:")
product=input("enter a product name:")
vendor=input("enter a vendor name:")
qty=int(input("enetr a quantity you want to bay:"))
if category in dict:
    if product in dict[category]:
        if vendor in dict[category][product]:
            available_q=dict[category][product][vendor]['qty']
            print("available_q",qty)
            dict.update({category:{product:{vendor:{'qty':available_q-qty}}}})
            print(dict)
        else:
            print("vendor name is not available...")
    else:
        print("product name is not available...")
else:
    print("category name is not availabel....")