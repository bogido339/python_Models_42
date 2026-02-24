import math


def create_position(x, y, z):
   return (x, y, z)


def calculate_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    return round(distance, 2)


def parse_coordinates(coord_string):
    try:
        list_data = coord_string.split(',')

        x = int(list_data[0])
        y = int(list_data[1])
        z = int(list_data[2])

        print(f'Parsing coordinates: "{coord_string}"')
        return (x, y, z)
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{coord_string}"')

        print(f"Error parsing coordinates: {e}")

        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def unpack_position(position):

    x, y, z = position

    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
    

def main():

    print("=== Game Coordinate System ===")

    pos1 = create_position(10, 20, 50)

    print(f"\nPosition created: {pos1}")

    origin = (0, 0, 0)
    distance = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {distance}")

    print("")
    pos2 = parse_coordinates("1,2,4")

    print(f"Parsed position: {pos2}")
    dist = calculate_distance(origin, pos2)
    print(f"Distance between {origin} and {pos2}: {dist}")

    print("")
    parse_coordinates("abc,def,ghi")

    print("")
    print("Unpacking demonstration:")
    unpack_position(pos2)


main()