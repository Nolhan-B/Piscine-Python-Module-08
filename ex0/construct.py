import sys
import os
import site


def main() -> None:
    env_path = os.environ.get("VIRTUAL_ENV")
    current_py = sys.executable

    if env_path:
        current_env = os.path.basename(env_path)
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {current_py}")
        print(f"Virtual Environment: {current_env}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(f"{site.getsitepackages()[0]}")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current_py}")
        print("Virtual Environnement: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # on Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
