from bowling_game import Game


def test__score_function__returns_zero__when_every_roll_scores_zero_pins():
    game = Game()

    for i in range(20):
        game.roll(0)

    assert game.score() == 0

def test__score_function__returns_twenty__when_every_roll_scores_one_pin():
    game = Game()

    for i in range(20):
        game.roll(1)

    assert game.score() == 20
    
def test__score_function__returns_the_correct_score__when_have_a_spare():
    game = Game()

    pins_per_roll = [2,1,1,4,5,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    for pin in pins_per_roll:
        game.roll(pin)

    assert game.score() == 33
    
def test__score_function__returns_the_correct_score__when_have_a_spare_at_the_last_frame():
    game = Game()

    pins_per_roll = [2,1,1,4,5,5,1,1,1,1,1,1,1,1,1,1,1,1,5,5]
    
    for pin in pins_per_roll:
        game.roll(pin)

    assert game.score() == 41

def test__score_function__returns_the_correct_score__when_have_a_strike():
    game = Game()

    pins_per_roll = [10,0,1,4,5,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    for pin in pins_per_roll:
        game.roll(pin)

    assert game.score() == 45

def test__score_function__returns_the_correct_score__when_have_a_spare_in_tenth_frame():
    game = Game()

    pins_per_roll = [10,0,1,4,5,5,1,1,1,1,1,1,1,1,1,1,1,1,7,3,8]
    
    for pin in pins_per_roll:
        game.roll(pin)

    assert game.score() == 61
