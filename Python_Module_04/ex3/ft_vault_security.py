def main() -> None:

    filename = "file.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")

    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"CRITICAL ERROR: {filename} not found! Extraction failed.")

    data = ("[CLASSIFIED] New security protocols archived\n"
            "Vault automatically sealed upon completion")

    print("\nSECURE PRESERVATION:")

    try:
        with open(filename, "w") as f:
            f.write(data)
            print(data)
    except Exception as e:
        print(f"CRITICAL ERROR: Could not write to vault. {e}")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
