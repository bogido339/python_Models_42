def ft_crisis_response(file_name: str) -> None:
    """
    Standardizes crisis handling for various file access
            failures within the storage matrix.
    """
    try:
        with open(file_name, "r") as f:
            content = f.read()

        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    """
    Main entry point for the Crisis Response System simulation.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    ft_crisis_response("lost_archive.txt")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    ft_crisis_response("classified_vault.txt")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    ft_crisis_response("standard_archive")


if __name__ == "__main__":
    main()
