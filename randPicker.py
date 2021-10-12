from random import choices
from time import sleep
count = 0
names = ["Nadav", "Kevin", "Emily", "Ben", "Claire", "Safal", "Jude", "Hans", "Jacob", "Alex Matty", "Alex Zizzo", "Alex Woo", "Anna", "Sunwoo", "Connor", "Luca", "Daniel", "Xavier", "Evan", "Junlin", "Hannah", "Kyle", "Brian"]

for count in range(0, 3):
    print(choices(names))
    count += 1
    sleep(1)