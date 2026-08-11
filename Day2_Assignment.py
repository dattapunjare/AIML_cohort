# -*- coding: utf-8 -*-
''' Day 2: Python Fundamentals
   Name: Datta Punjare
   Email :dattapunjare3050@gmail.com
   Date : 10 Aug
   Description : This file contains the assignment given on day 2.
   '''


'''arithamatic operration'''

x = 20
y = 6

# Exponent
x ** 6

# Modulus
x % y

# Integer Division
x // y

# Divsion
x / y

# multiplication
x * y

# Addition
x + y

# Substraction
x - y

# String Concatination

a='I am using '
b='Python'
c=" "
d= a+c+b

# String Replication

text = "Hellos"
result = text * 3
print(result)


text = "Hellos"
result = text * 3
print(result)

#lets change the value
var1=3.14

var1="alice"

print(var1)

#Datatype Convertion

print('I have completed' + str(5) + 'Assignment')

#round function

round(999.99)

round(6.9999)

# abs() function (absolute)

abs(-456)

#Equal to
a = 77
b = 77

if a == b:
    print("a is equal y")
else:
    print("b is not equal y")

#isnot equal
a = 55
b = 77
if a != b:
    print("a is not equal y")
else:
    print("b is equal y")

# Greater than
a = 7
b = 34

if a > b:
    print("a is greater than y")
else:
    print("b is not greater than y")

#Less than
a = 67
b = 21
if a < b:
    print("a is less than y")
else:
    print("b is not less than y")

print("SYSTEM: You are locked inside the Python Vault.")


print("Your Mission: Collect enough power to escape the vault.")

#level 1
energy=10
print("LEVEL 1 — ENERGY CORE")
print(f"You start with {energy} energy.")

found = int(input("You found an energy crystal worth: "))

energy = energy + found

print("Energy collected!")
print(f"Your energy is now: {energy}")

#level 2
print("LEVEL 2 — POWER BOOST")

boost = int(input("Choose your power multiplier (1–5): "))

powered_energy = energy * boost

print("POWER ACTIVATED!")
print(f"Your energy became: {powered_energy}")

#level 3
print("LEVEL 3 — LASER WALL")

laser_cost = int(input("How much energy does the laser wall cost? "))

remaining = powered_energy - laser_cost

print("Laser wall disabled!")
print(f"Energy remaining: {remaining}")

#level 4
print("LEVEL 4 — TEAM UP")

team_size = int(input("How many hackers are in your team? "))

share = remaining / team_size

print(f"Each hacker gets {share:.2f} energy.")

#level 5
print("LEVEL 5 — BUILD THE SQUAD")

energy_per_hacker = int(input("Energy required per hacker: "))

full_hackers = remaining // energy_per_hacker

print(f"You can fully power {full_hackers} hackers.")

#level 6
leftover = remaining % energy_per_hacker

print(f"Energy left unused: {leftover}")

#level 7
print("LEVEL 7 — THE FINAL VAULT")

power_level = int(input("Enter your final power level: "))

final_power = power_level ** 2

print(f"Your final power is: {final_power}")

#escape

print("VAULT UNLOCKED!")


print(f"""
 MISSION COMPLETE!

 Final energy      : {remaining}
 Full hackers      : {full_hackers}
 Leftover energy   : {leftover}
 Final power       : {final_power}


""")