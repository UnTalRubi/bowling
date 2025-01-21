class ScoreCard():
    total_score = 0
    ZERO = 0
    TEN = 10

    def __init__ (self, score_card):
        self.pins = score_card
        self.pins_list = []
        self.frames = []

    def __decode_pins__(self):
        for pin in self.pins:
            if pin.isdigit():
                pin = int(pin)
            elif pin == "-":
                pin = self.ZERO
            elif pin == "/":
                pin = self.TEN - self.pins_list[-1]
            elif pin == "X":
                pin = self.TEN
            self.pins_list.append(pin)

        for pos in range(len(self.pins)):
            if self.pins[pos] == "/":
                self.pins_list[pos] += self.pins_list[pos + 1]
            if self.pins[pos] == "X":
                self.pins_list[pos] += self.pins_list[pos + 1] + self.pins_list[pos + 2]
        
        if self.pins[-2] == "/" or self.pins[-2] == "X":
            self.pins_list.pop()
        
        return self.pins_list
    
    def card(self):
        return ScoreCard
    
    def get_pins(self):
        return self.pins
    
    def calculate_total(self):
        print(self.pins_list)
        return sum(self.__decode_pins__())