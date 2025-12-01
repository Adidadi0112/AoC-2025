from typing import Any, List

class SafeDial:

    def __init__(self):
        self.dial = list(range(100)) # a list from 0 to 99, which represents safe dial from task description
        self.current_number = 50 # actual selected number on dial, initial is 50
        self.zeros_sum = 0

    # a parser method for input data - it just create a list from text file and replace L with - and delete R
    def parse(self, input_data: List[str]):
        rotation_sequence = [number.replace("R", "") for number in input_data]
        rotation_sequence = [number.replace("L", "-") for number in rotation_sequence]
        rotation_sequence = [int(number) for number in rotation_sequence]
        return rotation_sequence

    # setter for current number
    def set_current_number(self, new_number):
        self.current_number = self.dial[new_number]

    '''
    rotate method

    accepts rotation: int

    if rotation and current number on dial is higher than entire dial (more than 100), then 
    it's calculated module from dividing rotation and current number by dial length. Thanks to that
    We can avoid out of bounds error
    '''
    def rotate(self, rotation):
        if rotation + self.current_number > len(self.dial) - 1 or rotation + self.current_number < -len(self.dial) - 1: 
            print(f'big: {self.current_number} and {rotation} result: {(rotation + self.current_number) % len(self.dial)}')
            self.set_current_number(self.dial[(rotation + self.current_number) % len(self.dial)])
        else:
            print(f'small: {self.current_number} and {rotation}')
            self.set_current_number(rotation + self.current_number)
        if self.current_number == 0:
            self.zeros_sum += 1
        