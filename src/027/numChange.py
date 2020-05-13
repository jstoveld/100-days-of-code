from random import randint
x=0
x, last = 0, -1
while (x < 10):
    number = randint(0, 9)
    if (number == last):
        print ("Same number")
    else:
        print("Last number is {0} now it is {1}".format(last,number))
    last = number
    x += 1