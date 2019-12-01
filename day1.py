import math


def fuel_requirement(mass):
    return math.floor(mass / 3) - 2


def fuel_requirement2(mass):
    additional_fuel = fuel_requirement(mass)

    if mass <= 0 or additional_fuel < 0:
        return 0

    return additional_fuel + fuel_requirement2(additional_fuel)


tests = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
]

for mass, fuel in tests:
    assert fuel_requirement(mass) == fuel

assert fuel_requirement2(1969) == 966
assert fuel_requirement2(100756) == 50346

# -----

# TASK 1

total_fuel = 0
with open('day1_data.txt') as f:
    for ln in f:
        total_fuel += fuel_requirement(int(ln))

print('Total fuel needed:', total_fuel)

# TASK 2

total_fuel = 0
with open('day1_data.txt') as f:
    for ln in f:
        total_fuel += fuel_requirement2(int(ln))

print('Total fuel needed:', total_fuel)
