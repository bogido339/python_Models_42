def ft_ancient_text() -> None:
    """
    Recovers and displays data from the 'ancient_fragment.txt' storage vault.
    """

    try:
        f = open("ancient_fragment.txt")
        print(f"Accessing Storage Vault: {f.name}")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        print(f.read())

        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


def main() -> None:
    """
    Main entry point for the Data Recovery System.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    ft_ancient_text()


if __name__ == "__main__":
    main()
