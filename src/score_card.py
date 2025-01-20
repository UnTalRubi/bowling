class ScoreCard():
    total_score = 0
    pins_list = []
    ZERO = 0
    TEN = 10

    def __init__ (self, score_card):
        self.pins = score_card

    def __decode_pins__(self):
        for pin in self.pins:
            if pin.isdigit():
                self.pins_list.append(int(pin)) 
            elif pin == "-":
                self.pins_list.append(self.ZERO)
            elif pin == "/":
                self.pins_list.append(self.TEN - self.pins_list[-1])
        return self.pins_list

    def card(self):
        return ScoreCard
    
    def get_pins(self):
        return self.pins
    
    def calculate_total(self):
        self.__decode_pins__()
        self.total_score = sum(self.pins_list)
        return self.total_score