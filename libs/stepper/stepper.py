import gpio

class Stepper():

    def __init__(self, pin1, pin2, pin3, pin4, revolve_steps=2048):
        self.pins = [pin1, pin2, pin3, pin4]

        for pin in self.pins:
            gpio.mode(pin, OUTPUT)
            gpio.set(pin, LOW)

        self.current_step = 0

    def rotate(self, angle, direction):
        steps = int(angle * self.revolve_steps / 360)
        self.rotateSteps(steps, direction)

    def rotateSteps(self, steps, direction):
        for i in range(steps):
            self._step(direction)


    def _step(self, direction):
        steps = [
            [self.pins[0]],
            [self.pins[0], self.pins[1]],
            [self.pins[1]],
            [self.pins[1], self.pins[2]],
            [self.pins[2]],
            [self.pins[2], self.pins[3]],
            [self.pins[3]],
            [self.pins[3], self.pins[0]]
        ]

        if direction == 1:
            self.current_step = (self.current_step + 1) % 8
        else:
            self.current_step = (self.current_step - 1) % 8

        high_pins = steps[self.current_step]
        for pin in self.pins:
            gpio.set(pin, LOW)
        for pin in high_pins:
            gpio.set(pin, HIGH)
        sleep(2)
