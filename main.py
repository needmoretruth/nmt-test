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

if num == 0:
    print("wow 0.000001 chance! num is zero!")
    exit()


def hi():
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


print("hi")
answer = int(input("how many: "))
if answer == 0:
    print("no")
    exit()
while b != answer:
    hi()
    b += 1
totall = total / answer
cc = c / answer
print(f"total time: {total}s, {c}")
print(f"average time: {totall}s, {cc}")
