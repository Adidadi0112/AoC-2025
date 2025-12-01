from typing import List

class SafeDial:

    def __init__(self):
        self.dial_size: int = 100 # size of dial [0-99]
        self.current_number = 50 # actual selected number on dial, initial is 50
        self.zeros_sum = 0

    def parse(self, input_data: List[str]) -> List[int]:
        parsed_input = []
        for line in input_data:
            val_str = line.strip().replace("R", "").replace("L", "-")
            parsed_input.append(int(val_str))
        return parsed_input

    def rotate(self, rotation: int) -> None:
        '''
        Optimized rotate function, which compares start position, our current_number, with end position, which is 
        sum of current_number and rotation value. Using '//' operator, function checks how many times dial fully rotates.
        If 0 was passed, left side of substraction should be higher than the right side by the value of fully crossed dial. eg. current_number = 289, dial_size = 100 and rotation = 540. end_pos // dial_size is 8 and start_pos //
        dial_size is 2 -> so zero was passed 6 times. If the result of equation is 0 - then 0 was not passed on dial. 
        '''
        start_pos = self.current_number
        end_pos = start_pos + rotation

        passed_zeros = 0

        if rotation > 0:
            passed_zeros = (end_pos // self.dial_size) - (start_pos // self.dial_size)
        elif rotation < 0:
            # -1 is for case when current_number is 0 and we move to the left. Thanks to that, function consider
            # 0 as 99 and will not count zero incorrectly
            passed_zeros = ((start_pos - 1) // self.dial_size) - ((end_pos - 1) // self.dial_size)
        
        self.zeros_sum += passed_zeros

        self.current_number = end_pos