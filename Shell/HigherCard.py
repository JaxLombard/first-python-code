import random
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king",
         "ace"]
my_face = random.choice(faces)
your_face = random.choice(faces)
print("My card: " + my_face+ ". Your card: " + your_face + ".")
if faces.index(my_face) > faces.index(your_face):
    print("I win!")
elif faces.index(my_face) < faces.index(your_face):
    print("You win!")
else:
    print("It's a tie!")
          
          
     
         
         
