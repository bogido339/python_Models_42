import sys


def creaat_dect(items_list):
    inventory = {}

    for item in items_list:
        try:
            tmp = item.split(':')
            if len(tmp) != 2:
                raise ValueError
            
            name = tmp[0]
            value = int(tmp[1])

            if len(name) == 0:
              raise ValueError
            if name in inventory:
                inventory[name] += value
            else:
                inventory[name] = value

        except ValueError:
            print("Error: please enter items as name:number")
            return None

    return inventory
    
def main():
    inventory = creaat_dect(sys.argv[1:])
    if not inventory:
        return
    print("=== Inventory System Analysis ===")
    sum_of_values = sum(inventory.values())
    print(f"total items in inventory: {sum_of_values}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for item, value in inventory.items():
        x = value * 100 / sum_of_values
        print(f"{item}: {value} units ({x:.1f}%)")
    
    print("\n=== Inventory Statistics ===")
    x = max(inventory, key=inventory.get)
    y = min(inventory, key=inventory.get)
    print(f"Most abundant: {x} ({inventory[x]} units)")
    print(f"Least abundant: {y} ({inventory[y]} units)")

    print("\n=== Item Categories ===")
    moderate_items = {}
    scarce_items = {}

    for item, value in inventory.items():
        if value >= 5:
            moderate_items[item] = value
        else:
            scarce_items[item] = value
    print(f"Moderate: {moderate_items}")
    print(f"Scarce: {scarce_items}")

    print("\n=== Management Suggestions ===")
    need_restock = []
    for item, value in inventory.items():
        if value <= 1:
            need_restock.append(item)
    print(f"Restock needed: {need_restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    item = 'sword'
    print(f"Sample lookup - '{item}' in inventory: {item in inventory}")

main()