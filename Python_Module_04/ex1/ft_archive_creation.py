def ft_archive_creation(file_name: str, data: str) -> None:
    """
    Initializes a new storage unit using exclusive creation mode to
                prevent overwriting.
    """
    try:
        f = open(file_name, "x")
        print(f"Initializing new storage unit: {f.name}")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        f.write(data)
        print(data)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{f.name}' ready for long-term preservation.")

    except FileExistsError:
        print("Error: The file already exists.")


def main() -> None:
    """
    Main entry point for the Preservation System.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    data = ("[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee")

    ft_archive_creation("new_discovery.txt", data)


if __name__ == "__main__":
    main()
