import sys


def main() -> None:
    """
    Manages communication channels using standard input,
            output, and error streams.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        rchivist_ID = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")

        if len(rchivist_ID) == 0 or len(status_report) == 0:
            raise ValueError

        print(f"\n[STANDARD] Archive status from "
              f"{rchivist_ID}: {status_report}")

        print("[ALERT] System diagnostic: Communication "
              "channels verified", file=sys.stderr)

        print("[STANDARD] Data transmission complete\n")
        print("Three-channel communication test successful.")

    except ValueError:
        print("\narchivist ID or status report not fawnd try again ...")


if __name__ == "__main__":
    main()
