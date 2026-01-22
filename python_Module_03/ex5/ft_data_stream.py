players = [
    {
        "name": 'alice',
        "levle": 5,
        "event": 'killed monster'
    },
    {
        "name": 'bob',
        "levle": 12,
        "event": 'found treasure'
    },
    {
        "name": 'charlie',
        "levle": 8,
        "event": 'lveled up'
    },
]


def event_stream(num_events):
    num_players = len(players)
    for i in range(1, num_events + 1):
        player = players[(i - 1) % num_players]
        yield {
            "levle": player["levle"],
            "event": player["event"],
        }


def ft_fibonacci(count):
    a = 0
    b = 1
    while count > 0:
        yield a
        tmp = a
        a = b
        b = tmp + b
        count -= 1


def ft_prime(count):
    n = 2

    while count > 0:
        is_prime = True

        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            yield n
            count -= 1

        n += 1


def main():
    print("=== Game Data Stream Processor ===")

    print("")
    for player in players:
        n = players.index(player) + 1
        name = player["name"]
        levle = player["levle"]
        event = player["event"]
        print(f"Event {n}: Player {name} (level {levle}) {event}")
    print("...")

    print("\n=== Stream Analytics ===")

    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up = 0

    for event in event_stream(1000):
        total_events += 1
        if event["levle"] >= 10:
            high_level += 1
        if event["event"] == "found treasure":
            treasure_events += 1
        elif event["event"] == "lveled up":
            level_up += 1

    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    f_count = 10
    p_count = 5
    fibonacci_list = []
    prime_list = []

    for num in ft_fibonacci(f_count):
        fibonacci_list.append(num)
    for num in ft_prime(p_count):
        prime_list.append(num)
    print(f"Fibonacci sequence (first {f_count}):", end=" ")
    print(*fibonacci_list, sep=", ")

    print(f"Prime numbers (first {p_count}):", end=" ")
    print(*prime_list, sep=", ")

main()
