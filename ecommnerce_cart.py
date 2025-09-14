def totalPrice(my_dict):
    total=0
    for keys, values in my_dict.items():
        total+=values
    return total
inp=input()
my_dict=eval(inp)
cartValue=totalPrice(my_dict)
print(cartValue)