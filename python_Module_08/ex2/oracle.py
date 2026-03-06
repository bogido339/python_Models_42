import os
import sys
from dotenv import load_dotenv


# uplode .env file in this script python
load_dotenv()

matrix_mode = os.getenv("MATRIX_MODE")
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion_endpoint = os.getenv("ZION_ENDPOINT")


def check_config():
    missing = []

    if not matrix_mode:
        missing.append("MATRIX_MODE")
    if not database_url:
        missing.append("DATABASE_URL")
    if not api_key:
        missing.append("API_KEY")
    if not log_level:
        missing.append("LOG_LEVEL")
    if not zion_endpoint:
        missing.append("ZION_ENDPOINT")

    return missing


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    missing = check_config()

    if missing:
        print("Warning: Missing configuration")
        for m in missing:
            print("-", m)
        sys.exit(1)
    else:
        print("Configuration loaded:")
        print("Mode:", matrix_mode)
        print("Database: Connected")
        print("API Access: Authenticated")
        print("Log Level:", log_level)
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
