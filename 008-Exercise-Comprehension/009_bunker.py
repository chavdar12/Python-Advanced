def supplies_for_the_bunker(inventory_list):
    for _ in range(number_of_entries):
        category, item_name, other_information = input().split(" - ")
        if item_name not in bunker_inventory[category]["Name"]:
            bunker_inventory[category]["Name"].append(item_name)

        quantity_data, quality_data = other_information.split(";")
        quantity = int(quantity_data.split(":")[1])
        quality = int(quality_data.split(":")[1])

        bunker_inventory[category]["Quantity"] += quantity
        bunker_inventory[category]["Quality"] += quality

    return inventory_list


def print_result(inventory_list):
    items_count = sum([name_quantity_quality['Quantity'] for category, name_quantity_quality in inventory_list.items()])
    print(f"Count of items: {items_count}")

    sum_quality = sum([name_quantity_quality['Quality'] for category, name_quantity_quality in inventory_list.items()])
    average_quality = sum_quality / len(inventory_list)
    print(f"Average quality: {average_quality:.2f}")

    for category, name_quantity_quality in inventory_list.items():
        print(f"{category} -> ", end="")
        print(*name_quantity_quality['Name'], sep=", ")


categories = input().split(", ")
number_of_entries = int(input())
bunker_inventory = {
    category: {"Name": [],
               "Quantity": 0,
               "Quality": 0}
    for category in categories
}
supplies_for_the_bunker(bunker_inventory)
print_result(bunker_inventory)
