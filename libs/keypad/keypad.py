"""
Author: Armcod
Date: 2022-06-22
Version: 0.1
Description:Matric keypad driver

"""

import gpio



class KEYPAD():
    
    keys = [                                                                     # keypad matrix 4x4
        [1, 2, 3, 'A'],
        [4, 5, 6, 'B'],
        [7, 8, 9, 'C'],
        ['*', 0, '#', 'D']
    ]

    # init
    def __init__(self, pin_list_in, pin_list_out):
        self.pin_list_in = pin_list_in
        self.pin_list_out = pin_list_out
        self.init()


    def init(self):
        for pin in self.pin_list_in:
            gpio.mode(pin, INPUT)
        for pin in self.pin_list_out:
            gpio.mode(pin, OUTPUT)
            

    # get key
    def get_key(self):
        i,j = 0,0
        for pin in self.pin_list_out:
            gpio.set(pin, LOW)
        while i<4:
            gpio.set(self.pin_list_out[i], HIGH)
            j=0
            while j<4:
                if gpio.get(self.pin_list_in[j]) == HIGH:
                    return self.keys[i][j]
                j += 1
            i+=1
        return None