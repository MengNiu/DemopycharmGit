# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


cal_to_units = 24


def days_to_units(days, name_of_unit):
    print(f"{days} days are {days * cal_to_units} {name_of_unit}")
    return f"{days} days are {days * cal_to_units} {name_of_unit}"



#my_var=days_to_units(20,"hours")
#print (my_var)
user_input=input("enter days:\n")
print(user_input)
days_to_units(int(user_input),"hours")

