import schedule
import time
import random
print("only used to generate sensor data...")
def sensor1():
    with open("sensor1.txt","a+") as f1:
        info=str(random.randint(5,50))
        f1.write(info)
def sensor2():
    with open("sensor2.txt","a+") as f2:
        info=str(random.randint(10,50))
        f2.write(info)
schedule.every(20).seconds.do(sensor1)
schedule.every(10).seconds.do(sensor2)

while True:
    schedule.run_pending()
