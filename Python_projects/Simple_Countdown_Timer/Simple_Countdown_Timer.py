import time

total_seconds = int(input())

for i in range(total_seconds, -1, -1):
    mins, secs = divmod(i, 60)
    print(f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)

print("\nTime is up!")
