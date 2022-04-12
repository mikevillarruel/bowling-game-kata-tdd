from bowling_game import Game


def test__score_function__returns_zero__when_every_roll_scores_zero_pins():
    game = Game()

    for i in range(20):
        game.roll(0)

    assert game.score() == 0
