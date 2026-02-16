import random
import time

current_guess = 0
target_number = random.randint(1, 1000000)
count = 0
current_round = 0
total_attempts = 0
total = 0
average_time = 0
bb = 0
avg_attempts = 0
choice = 0


def menu():
    width = 40

    print("=" * width)
    print("Random Time".center(width))
    print("-" * width)
    print(" 1. run")
    print(" 2. exit")
    print(" 3. debug")
    print("=" * width)

    choice = input("select option (1-3): ")
    if choice == "1":
        run()
    elif choice == "2":
        ex()
    elif choice == "3":
        debug()
    else:
        print("1 or 2 or 3")
        menu()
    return choice


def rt():
    global count, current_guess, total_attempts, target_number, total
    start_time = time.perf_counter()
    current_guess = 0

    while current_guess != target_number:
        current_guess = random.randint(1, 1000000)
        count += 1
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"time: {execution_time:}s, {count}")
    total += execution_time
    total_attempts += count
    count = 0


def ex():
    print("bye bye")
    exit()


def debug():
    print("this is debug mode")
    print(f"target number: {target_number}")
    input("press enter to continue")
    menu()


def run():
    global current_round, total, total_attempts, average_time, avg_attempts
    current_round = 0
    total = 0
    total_attempts = 0
    total_rounds = int(input("how many: "))
    if total_rounds == 0:
        print("no")
        exit()
    while current_round != total_rounds:
        rt()
        current_round += 1
    average_time = total / total_rounds
    avg_attempts = total_attempts / total_rounds
    print(f"total time: {total}s, {total_attempts}")
    print(f"average time: {average_time}s, {avg_attempts}")
    input("press enter to continue")
    menu()


menu()
