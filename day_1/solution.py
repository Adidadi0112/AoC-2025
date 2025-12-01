from safe_dial import SafeDial

safe = SafeDial()

with open("day_1/input.txt") as file:
    sequence = file.read().split("\n")
    sequence.remove(sequence[-1])

sequence = safe.parse(sequence)

for number in sequence:
    safe.rotate(number)

print(safe.zeros_sum)

# test_input = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
# sequence = safe.parse(test_input)

# for number in sequence:
#     safe.rotate(number)

# print(safe.zeros_sum)

# 1975 is too low