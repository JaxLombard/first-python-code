#AustinPizza.py

#Ask the person how many pizzas they want.
numberofpizzas = eval(input("How many pizzas do you want?"))
#Ask for the menu cost of each pizza.
costperpizza = eval(input("How much does each pizza cost?"))
#Calculate the total cost of the pizzas as our subtotal.
subtotal = numberofpizzas * costperpizza
#Calculate the sales tax owed, at 6.25 percent of the subtotal.
taxrate = 0.0825
salestax = subtotal * taxrate
#Add the sales tax to the subtotal for the final total.
total = subtotal + salestax
#Show the user the total amount due, including tax.
print("The total cost is $",total)
print("This includes $",subtotal, "for the pizza and")
print("$",salestax, "in sales tax.")
