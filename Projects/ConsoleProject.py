# first_name = "Neil Jordan"
# last_name = "Bagabagon"
# email = "neiljbagabagon@gmail.com"
#
# print("Hello, I am {} with family name of {}. You can contact me on my email, {}".format(first_name,last_name,email))

# def multiplication():
#     a = 250
#     b = 6
#     print(a * b)
#
# multiplication()

# def division():
#     a = input("Enter first number: ")
#     b = input("Enter second number: ")
#     print("The sum of ",a," and ",b," is ",int(a) * int(b))
#
# division()

# def user_info(name, age, location, email, company, *args, **kwargs):
#     print("I am {}, {} years old, from {} with an email of {}.".format(name, age, location, email))
#
# user_info("Neil Jordan", 30, "Santa Cruz", "@gmail.com", "Gameops", 30000, hire_date="Dec 18, 2026")

# age = input("What is your age?")
# if int(age) < 18:
#     print("Not old enough")
# elif int(age) > 60:
#     print("Too Old")
# else:
#     print("Old enough")

# name = input("What is your name?")
# if name == "Neil":
#     print("Hello {}, How are you?".format(name))
# else:
#     print("You're not what we are looking for")


# def main():
#     print("WELCOME!!")
#     print("Please select a number below :)")
#     print("1. Addition")
#     print("2. Subtraction")
#
#     number = int(input("Number: "))
#     if number == 1:
#         one()
#     elif number == 2:
#         two()
#
# def one():
#     print("Welcome to Addition Calculator")
#     print("1. Start Adding")
#     print("2. Exit")
#
#     number_add = input("Number: ")
#     if number_add == "1":
#         print("You've selected number {}".format(number_add))
#     elif number_add == "2":
#         main()
#
# def two():
#     print("Welcome to Subtraction Calculator")
#     print("1. Start Subtracting")
#     print("2. Exit")
#
#     number_sub = input("Number: ")
#     if number_sub == "1":
#         print("You've selected number {}".format(number_sub))
#     elif number_sub == "2":
#         main()
#
#
# #ENTRY POINT
# if __name__ == "__main__":
#     main()


# cars = ["Toyota","Honda","Mitsubishi","Kawasaki"]
# for car in cars:
#     print("Do you want {}?".format(car))

for number in range(1,11):
    if number == 5:
        continue
    print("Number: {}".format(number))

# temperature = 50
# while temperature > 0:
#     print("Temperature is {}, it's cold".format(temperature))
#     temperature -= 1
#     if temperature == 40:
#         break


