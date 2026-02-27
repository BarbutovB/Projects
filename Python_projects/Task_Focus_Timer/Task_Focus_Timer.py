import time


def start_timer(minutes, label):
    seconds = minutes * 60
    print(f"\n Timer started for: {label} ({minutes} minutes)")

    while seconds > 0:

        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"

        print(f"Time remaining: {timer_display}", end="\r")

        time.sleep(1)
        seconds -= 1

    print("\n Time's up! Great job on your task.")


print("--- Focus Task Timer ---")
task_name = input("What are you working on? ")
duration = int(input("How many minutes do you want to focus? "))

start_timer(duration, task_name)


