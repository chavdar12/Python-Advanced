def stock_availability(inventory, action, *args):
    inventory = list(inventory)
    if action == "delivery":
        return inventory + list(args)
    if not args:
        return inventory[1:]
    if isinstance(args[0], int):
        return inventory[args[0]:]
    return [box for box in inventory if box not in args]


if __name__ == "__main__":
    print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
    print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
