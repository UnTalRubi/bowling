class ScoreCard():

    def __init__ (self, score_card):
        self.pins = score_card
        self.pins_list = []

    def __decode_pins(self):
        TEN = 10
        ZERO = 0
        for pin in self.pins:
            if pin.isdigit():
                pin = int(pin)
            elif pin == "-":
                pin = ZERO
            elif pin == "/":
                pin = TEN - self.pins_list[-1]
            elif pin == "X":
                pin = TEN
            self.pins_list.append(pin)
        return self.pin_list

    def calculate_rolls(self):
        for roll in range(self.get_number_rolls()):
            if self.pins[roll] == "/" and roll + 2 < self.get_number_rolls():
                self.pins_list[roll] += self.pins_list[roll + 1]
                
            if self.pins[roll] == "X" and roll + 3 < self.get_number_rolls():
                self.pins_list[roll] += self.pins_list[roll + 1] + self.pins_list[roll + 2]

        return self.pins_list

    def get_pins(self):
        return self.pins

    def get_number_rolls(self):
        return len(self.pins)

    def calculate_total(self):
        self.__decode_pins()
        return sum(self.__decode_pins())