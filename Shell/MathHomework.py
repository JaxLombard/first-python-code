print("Your Math Homewok")

#Ask the user to enter a math problem
problem = input("Enter a math problem, or 'q' to quit: ")

# Keep going untill the user enters 'q' to quit
while (problem != "q"):

    # Show the problem, and the answer using eval()
    print("The answer ", problem, "is:" , eval(problem) )
    problem = input("Enter another math problem, or 'q' to quit: ")

 
