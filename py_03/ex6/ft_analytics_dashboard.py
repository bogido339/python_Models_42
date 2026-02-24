players = {
    "alice": {
        "score": 2300,
        "achievements": ["first_kill", "level_10", "boss_slayer"],
        "active": True,
        "region": "north"
    },
    "bob": {
        "score": 1800,
        "achievements": ["first_kill", "level_5"],
        "active": True,
        "region": "east"
    },
    "charlie": {
        "score": 2150,
        "achievements": ["level_10", "boss_slayer"],
        "active": False,
        "region": "central"
    },
    "diana": {
        "score": 2050,
        "achievements": ["first_kill", "level_10"],
        "active": True,
        "region": "north"
    }
}


def analyze_with_lists(players):
    scores = [name for name, data in players.items() if data["score"] > 2000]
    print(f"High scorers (>2000): {scores}")

    double = [p["score"] * 2 for p in players.values()]
    print(f"Scores doubled: {double}")

    active = [name for name, active in players.items() if active["active"]]
    print(f"Active players: {active}")


def analyze_with_dicts(players):
    scores = {name: score["score"] for name, score in players.items() if score["active"]}
    print(f"Player scores: {scores}")

    score_categories = {
    "high": len([p for p in players.values() if p["score"] > 2000]),
    "medium": len([p for p in players.values() if 1800 <= p["score"] <= 2000]),
    "low": len([p for p in players.values() if p["score"] < 1800])
    }
    print(f"Score categories: {score_categories}")

    counts = {name: len(d["achievements"]) for name, d in players.items() if d["active"]}
    print(f"Achievement counts: {counts}")


def analyze_with_sets(players):
    sets = {player for player in players.keys()}
    print(f"Unique players: {sets}")

    achievements = {ach for p in players.values() for ach in p["achievements"]}
    print(f"Unique achievements: {achievements}")

    regions = {r["region"] for r in players.values() if r["active"]}
    print(f"Active regions: {regions}")


def run_combined_analysis(players):
    print(f"Total players: {len(players)}")

    achievements = {ach for p in players.values() for ach in p["achievements"]}
    print(f"Total unique achievements: {len(achievements)}")

    total_score = 0
    for score in players.values():
        total_score += score["score"]
    if len(players) > 0:
        average_score = total_score / len(players)
    else:
        average_score = 0
    print(f"Average score: {average_score}")

    highest_score = max(p["score"] for p in players.values())
    for name in players.keys():
        player = players[name]
        if player["score"] == highest_score:
            top_ply = name
            break
    points = players[top_ply]["score"]
    ach = len(players[top_ply]["achievements"])
    print(f"Top performer: {top_ply} ({points} points, {ach} achievements)")


def main():
    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    analyze_with_lists(players)

    print("\n=== Dict Comprehension Examples ===")
    analyze_with_dicts(players)

    print("\n=== Set Comprehension Examples ===")
    analyze_with_sets(players)

    print("\n=== Combined Analysis ===")
    run_combined_analysis(players)

main()