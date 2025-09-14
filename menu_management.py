def add_menu_item(menu,item):
    menu.append(item)
    return menu
def remove_menu_item(menu,item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} is not there to remove")
    return menu
def check_menu_item(menu,item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"
inp=input("Enter space separated items: ")
initial_menu=inp.split()
add_item=input()
remove_item=input()
check_item=input()
menu=add_menu_item(initial_menu,add_item)
menu=remove_menu_item(menu,remove_item)
availability=check_menu_item(menu,check_item)
print("Updated menu:", menu)
print("Availability:", availability)