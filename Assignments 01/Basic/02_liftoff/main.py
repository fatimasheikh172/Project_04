import time

def count_start(start = 10):
    for i in range(start , -1 , -1):
        print(i)
    time.sleep(1)

    print("liftoff !")

count_start()