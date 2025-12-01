from safe_dial import SafeDial

safe = SafeDial()

with open("day_1/input.txt") as file:
    sequence = file.read().split("\n")
    sequence.remove(sequence[-1])
    print(sequence)

sequence = safe.parse(sequence)

for number in sequence:
    safe.rotate(number)

print(safe.zeros_sum)