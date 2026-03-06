import sys
import os
import site


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def display_env_info():
    python_path = sys.executable
    env_path = sys.prefix
    env_name = os.path.basename(env_path)

    if is_venv():
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")


display_env_info()

if is_venv():
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")

    print("\nPackage installation path:")
    print(site.getusersitepackages())
else:
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate   # On Windows")

    print("\nThen run this program again.")
