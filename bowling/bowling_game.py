FRAMES_IN_GAME = 10
NUMBER_OF_PINS_FOR_BONUS = 10

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        frame_start = 0
        total = 0
        for _ in range(FRAMES_IN_GAME):
            first_roll = self.rolls[frame_start]
            is_strike = first_roll == NUMBER_OF_PINS_FOR_BONUS
            if is_strike:
                frame_score = first_roll
                next_roll = self.rolls[frame_start+1]
                next_next_roll = self.rolls[frame_start+2]
                bonus = next_roll + next_next_roll
            else:
                second_roll = self.rolls[frame_start+1]
                frame_score = first_roll + second_roll
                is_spare = frame_score == NUMBER_OF_PINS_FOR_BONUS
                bonus = self.rolls[frame_start+2] if is_spare else 0
            frame_start += 1 if is_strike else 2
            total += frame_score + bonus
        return total