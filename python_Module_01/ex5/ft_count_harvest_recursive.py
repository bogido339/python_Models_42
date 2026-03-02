def ft_count_harvest_recursive(a=1, b=None):
    if b is None:
        b = int(input("Days until harvest: "))
    print(f"Day {a}")
    if a < b:
        ft_count_harvest_recursive(a + 1, b)
    if a is b:
        print("Harvest time!")
