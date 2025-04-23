import pokerkit

class Game:
    def __init__(self, starting_stacks: list[float] = None):
        big_blind = 1.0
        small_blind = big_blind / 2
        min_bet = big_blind
        default_starting_stack = 100 * big_blind
        number_of_players = 6
        antes = {}
        if starting_stacks is None:
            starting_stacks = [default_starting_stack] * number_of_players
        else:
            assert len(starting_stacks) == number_of_players
        blinds = (small_blind, big_blind)

        self.game = pokerkit.NoLimitTexasHoldem(
            automations=(
                pokerkit.Automation.ANTE_POSTING,
                pokerkit.Automation.BET_COLLECTION,
                pokerkit.Automation.BLIND_OR_STRADDLE_POSTING,
                pokerkit.Automation.BOARD_DEALING,
                pokerkit.Automation.CARD_BURNING,
                pokerkit.Automation.CHIPS_PULLING,
                pokerkit.Automation.CHIPS_PUSHING,
                pokerkit.Automation.HAND_KILLING,
                pokerkit.Automation.HOLE_DEALING,
                pokerkit.Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
            ),
            ante_trimming_status=False,
            raw_antes=antes,
            raw_blinds_or_straddles=blinds,
            min_bet=min_bet,
            mode=pokerkit.Mode.CASH_GAME,
        )

        self.state = self.game(
            raw_starting_stacks=starting_stacks,
            player_count=number_of_players,
        )

    def fold(self):
        self.state.fold()

    def relative_pot_sized_raise(self, percentage):
        raise_amount = self.calculate_relative_pot_sized_betting(percentage)
        self.incremental_raise_bet(raise_amount)

    def incremental_raise_bet(self, amount):
        player_seat = self.state.actor_index
        raise_value = self.state.bets[player_seat] + amount
        self.state.complete_bet_or_raise_to(raise_value)

    def raise_bet(self, total_raise):
        self.state.complete_bet_or_raise_to(total_raise)

    def call(self):
        self.state.check_or_call()

    def check(self):
        self.state.check_or_call()

    def calculate_relative_pot_sized_betting(self, percentage):
        calling_amount = max(self.state.bets) - self.state.bets[self.state.actor_index]
        pot_sized_bet = self.state.total_pot_amount + calling_amount

        return pot_sized_bet * percentage + calling_amount

    def actions(self):
        self.hh = pokerkit.HandHistory.from_game_state(self.game, self.state)
        return self.hh.actions
