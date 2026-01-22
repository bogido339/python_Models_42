import sys

x = sys.argv
len_x = len(x)
list_data = []


print("=== Player Score Analytics ===")


y = x[1:]
for arg in y:
    try:
        list_data.append(int(arg))
    except ValueError:
        print(f"'{arg}' is not valid number ...")

if len(list_data) > 0:
    print(f"Scores processed: {list_data}")
    print(f"Total players: {len(list_data)}")
    print(f"Total score: {sum(list_data)}")
    print(f"Average score: {sum(list_data) / len(list_data)}")
    print(f"High score: {max(list_data)}")
    print(f"Low score: {min(list_data)}")
    print(f"Score range: {max(list_data) - min(list_data)}")
elif len_x == 1:
    print("No scores provided. Usage: python3" \
            " ft_score_analytics.py <score1> <score2> ...")
else:
    print("dont fiwnd valid argiment try again ...")
