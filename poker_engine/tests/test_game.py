from poker_engine.game import Game

class TestRelativePotRaises:
    def test_relative_pot_raise_when_actor_has_already_bet(self):
        big_blind = 100
        bet_size = big_blind * 45
        starting_stack = big_blind * 100
        game = Game(starting_stacks=[starting_stack] * 6)
        game.raise_bet(bet_size)
        game.fold()
        game.fold()
        game.fold()
        game.fold()

        assert game.state.pot_completion_betting_or_raising_to_amount == big_blind * 100
        game.relative_pot_sized_raise(percentage=0.5)
        total_pot = game.state.total_pot_amount
        call_amount = game.state.checking_or_calling_amount
        assert total_pot / call_amount == 3

    def test_relative_pot_raise_when_actor_has_not_yet_bet(self):
        big_blind = 100
        starting_stack = big_blind * 100
        bet_size = big_blind * 23
        game = Game(starting_stacks=[starting_stack] * 6)
        game.raise_bet(bet_size)
        game.call()
        game.relative_pot_sized_raise(1.0)
        game.fold()
        game.fold()
        game.fold()
        total_pot = game.state.total_pot_amount
        call_amount = game.state.checking_or_calling_amount
        assert total_pot / call_amount == 2
