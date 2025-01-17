class ScoreCard():

    def __init__ (self, score_card):
        self.pins = score_card
    
    def __decoder_pins__(self):
        self.pins = self.pins.replace("-","0")
        self.pins = self.pins.replace()

    def card(self):
        return ScoreCard
    
    def get_pins(self):
        return self.pins
    
    def calculate_total(self):
        self.__decoder_pins__()
        total_score = 0
        for pin in self.pins:
            total_score += int(pin)
        return total_score