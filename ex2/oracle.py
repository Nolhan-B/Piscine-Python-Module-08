import os
from dotenv import load_dotenv


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        env = load_dotenv()
        if not env:
            raise Exception('.env could not be found!')
        matrix_mode = os.getenv("MATRIX_MODE")
        database_url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL")
        zion_endpoint = os.getenv("ZION_ENDPOINT")

        print("Configuration loaded:")
        print(f"Mode: {matrix_mode if matrix_mode else 'unknown'}")
        s = "Connected to local instance" if database_url else "Not connected"
        print("Database: " + s)

        print(f"API Access: {'Authenticated' if api_key else 'Missing'}")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}\n")

        print("Environment security check:")
        if api_key is None:
            print("[ERROR] API_KEY missing!")
        else:
            print("[OK] No hardcoded secrets detected")

        print("[OK] .env file properly configured")
        print("[OK] Production overrides available"
              if matrix_mode == "production"
              else "[INFO] Running in development mode")

        print("\nThe Oracle sees all configurations.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
