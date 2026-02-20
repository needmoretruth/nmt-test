import os
import sys
import time


def get_version():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                return lines[-1].strip()
    except Exception:
        return ""
    return ""


def menu():
    version = get_version()
    while True:
        try:
            width = os.get_terminal_size().columns - 5
        except Exception:
            width = 40

        print("\n" + "=" * width)
        title = f"NMT Test {version}".center(width)
        print(title)
        print("-" * width)
        print(" 1. run")
        print(" 2. setting")
        print(" 3. debug")
        print(" 4. exit")
        print("=" * width)

        choice = input("select option >> ").strip()

        if not choice:
            print("please enter number")
            time.sleep(1)
            continue

        if choice == "1":
            run()
        elif choice == "2":
            setting()
        elif choice == "3":
            debug()
        elif choice == "4":
            print("bye bye")
            sys.exit()
        else:
            print(f"'{choice}' is wrong please try other number")
            time.sleep(1)


def run():
    while True:
        print("\n--- run menu ---")
        print(" 1. random generation")
        print(" 2. sum")
        print(" 3. odd even")
        print(" 4. power")
        print(" 5. back")

        choice = input("select run option >> ").strip()

        if choice == "1":
            print("comming soon")
        elif choice == "2":
            print("comming soon")
        elif choice == "3":
            print("comming soon")
        elif choice == "4":
            print("comming soon")
        elif choice == "5":
            break
        else:
            print("wrong choice")


def setting():
    print("\ncomming soon")
    input("\npress enter to go back")


def debug():
    print("\ncomming soon")
    input("\npress enter to go back")


if __name__ == "__main__":
    print("welcome to nmt-test")
    time.sleep(1)
    menu()
