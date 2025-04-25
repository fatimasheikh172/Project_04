import time

def start_timer():
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    total_seconds = minutes * 60 + seconds

    print(f"⏱ Countdown started for {minutes} minutes and {seconds} seconds...\n")
    
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("⏰ Time’s up!")

# Run it
start_timer()
