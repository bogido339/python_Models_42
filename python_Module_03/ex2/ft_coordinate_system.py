import sys


def calculate_distance(pos1: tuple, pos2: tuple) -> float:
    """
    Calculates 3D distance using the Euclidean formula without math import.
    """
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
    return round(float(distance), 2)


def parse_coordinates(coord_string: str) -> None:
    """
    Parses a string into a tuple while handling numeric errors gracefully
    """
    try:
        list_data = coord_string.split(',')
        x = int(list_data[0])
        y = int(list_data[1])
        z = int(list_data[2])

        print(f'Parsing coordinates: "{coord_string}"')
        return (x, y, z)
    except Exception:
        print("inter jast one argement the format (x,y,z)")


def unpack_position(position: tuple) -> None:
    """
    Shows off tuple unpacking magic to display coordinates
    """
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    """
    Demonstrates the coordinate system logic including distance and parsing.
    """
    print("=== Game Coordinate System ===")
    data = [(10, 20, 5)]


    origin = (0, 0, 0)

    for pos in data :
        print(f"\nPosition created: {pos}")
        print(
            f"Distance between {origin} and {pos}: "
            f"{calculate_distance(origin, pos)}"
        )

    print("")
    if len(sys.argv) < 2 :
        pos2 = parse_coordinates("3,4,0")
    elif len(sys.argv) == 2:
        pos2 = parse_coordinates(sys.argv[1])
    else:
        print("inter jast one argement the format (x,y,z)")
    if pos2:
        print(f"Parsed position: {pos2}")
        print(
            f"Distance between {origin} and {pos2}: "
            f"{calculate_distance(origin, pos2)}"
        )

    print("")
    parse_coordinates("1, 2, 3")

    print("\nUnpacking demonstration:")
    if pos2:
        unpack_position(pos2)


if __name__ == "__main__":
    main()
