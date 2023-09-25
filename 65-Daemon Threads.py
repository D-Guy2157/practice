# daemon thread = a thread that runs in the background, not important f or program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes
import threading
import time


def timer():
    time.sleep(0.1)
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, " seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)  # sets to daemon, cannot be used while thread is running
# print(x.isDaemon())  # prints true/false

answer = input("Do you wish to exit?")
print(answer)
# this is jank asf btw
