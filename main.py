import random
import time

ran = 0
num = random.randint(0, 1000000)
a = 0
b = 0
c = 0
total = 0
totall = 0
bb = 0
cc = 0
choice = 0

if num == 0:
    print("wow 0.000001 chance! num is zero!")
    print("but num is need change")
    num = random.randint(1, 1000000)


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
    global a, b, c, ran, num, total
    start_time = time.perf_counter()
    ran = 0

    while ran != num:
        ran = random.randint(0, 1000000)
        a += 1
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"time: {execution_time:}s, {a}")
    total += execution_time
    c += a
    a = 0


def ex():
    print("bye bye")
    exit()


def debug():
    print("this is debug mode")
    print(f"num: {num}")
    input("press enter to continue")
    menu()


def run():
    global b, total, c, totall, cc
    answer = int(input("how many: "))
    if answer == 0:
        print("no")
        exit()
    while b != answer:
        rt()
        b += 1
    totall = total / answer
    cc = c / answer
    print(f"total time: {total}s, {c}")
    print(f"average time: {totall}s, {cc}")
    input("press enter to continue")
    menu()


menu()
