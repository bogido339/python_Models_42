import sys

x = sys.argv
len_x = len(x)

print("=== Command Quest ===")
if len_x == 1:
    print("No arguments provided!")
print(f"Program name: {x[0]}")
if len_x > 1:
    print(f"Arguments received: {len_x - 1}")
    i = 1
    y = x[1:]
    for arg in y:
        print(f"Argument {i}: {arg}")
        i += 1
print(f"Total arguments: {len_x}")
