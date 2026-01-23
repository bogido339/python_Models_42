# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# res = [num for num in a if num % 2 == 0]
# print(res)

# l = []
# t = [l.append(i) for i in range(1, 10)]
# print(l)

# key = [1, 2, 3, 4, 5]
# value = ["mohamed", "bougajdi", "student", "in", "1337"]

# dic = {a: b for a, b in zip(key, value) if a == 3 if b == "student"}
# print(dic)

#   high = 0
#     medium = 0
#     low = 0
#     categories = {x["score"] for x in players.values() if x["score"] > 2000: high += 1 elif x["score"] > 1800: medium += 1 else: low += 1}

raw_names = ["Alice", "Bob", "Alice", "Charlie", "bob"]

# The comprehension processes all 5 items, but only keeps unique ones
unique_names = {name for name in raw_names}

print(unique_names)
# Output: {'Alice', 'Bob', 'Charlie'}


players = {
    "p1": {"name": "Alice", "achievements": ["Winner", "MVP"]},
    "p2": {"name": "Bob",   "achievements": ["Runner-up", "MVP"]}, # MVP is repeated here
    "p3": {"name": "Charlie", "achievements": ["Winner"]}          # Winner is repeated here
}

# The Logic:
# 1. Loop through players.values() -> get player dict
# 2. Loop through player["achievements"] -> get individual achievement
# 3. Store in set -> automatically removes duplicates ("MVP", "Winner")

unique_achievements = {ach for p in players.values() for ach in p["achievements"]}

print(unique_achievements)
# Output: {'Winner', 'MVP', 'Runner-up'}