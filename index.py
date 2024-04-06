import time
my_time = int(input("Enter the time in seconds:"))

for x in range(my_time,0,-1):
    # print(x)
    seconds = x % 60
    minutes = (x /60) % 60
    hours = int(x / 3600)
    print(f"{seconds:01}")
    time.sleep(1)

print("Time's Up!")






