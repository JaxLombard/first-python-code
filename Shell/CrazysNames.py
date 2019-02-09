from random import *
import random


peopleInMyFamily = ['Jax','Lawson','Harley','Dad','Mom']
name = input("What is your name? ")
numberOfTimes = input("How many times do you want to say me to say " + name + "? ")
for currentNumber  in range(int(numberOfTimes)):

     
    randomNumberOfSpaces = randint(0,50) 
    stringToPrint = ' ' * randomNumberOfSpaces + name + " likes to play with " + random.choice(peopleInMyFamily)
    print (stringToPrint)
    

