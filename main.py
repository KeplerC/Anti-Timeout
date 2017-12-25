#!/usr/local/cs/bin/python3
import time
import os
import datetime
def process():
    time_stamp = "{} : {}\n".format(os.getpid(), str(datetime.datetime.now()))
    with open("./log", "a") as log:
        log.write(time_stamp)
        log.close()

def main():
    counter = 0
    while True:
        process()
        time.sleep(3600)
        counter += 1
        if(time == 4):
            os.fork()


if __name__ == "__main__":
    main()
