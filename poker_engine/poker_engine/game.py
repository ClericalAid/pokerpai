import pokerkit

class Game:
    def __init__(self, starting_stacks: list[float] = None, big_blind=1.0, small_blind=0.5):
        self.big_blind = big_blind
        self.small_blind = small_blind
        min_bet = self.big_blind
        default_starting_stack = 100 * self.big_blind
        antes = {}

        if starting_stacks is None:
            self.number_of_players = 6
            starting_stacks = [default_starting_stack] * self.number_of_players
        else:
            self.number_of_players = len(starting_stacks)

        self.blinds = (self.small_blind, self.big_blind)

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
            raw_blinds_or_straddles=self.blinds,
            min_bet=min_bet,
            mode=pokerkit.Mode.CASH_GAME,
        )

        self.state = self.game(
            raw_starting_stacks=starting_stacks,
            player_count=self.number_of_players,
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

    def status(self):
        hand_actions = self.actions()
        hole_cards = self.state.hole_cards
        hole_cards = [[self.card_to_str(card) for card in player_cards] for player_cards in hole_cards]

        board_cards = self.state.board_cards
        board_cards = [self.card_to_str(board_card[0]) for board_card in board_cards]
        # board_cards = [self.card_to_str(card) for card in board_cards]

        players_statuses = self.state.statuses
        game_ended = not self.state.status

        return {
            "player_count": self.number_of_players,
            "blinds": self.blinds,
            "starting_stacks": self.state.starting_stacks,
            "current_stacks": self.state.stacks,
            "current_bets": self.state.bets,
            "total_pot_amount": self.state.total_pot_amount,
            "actor_index": self.state.actor_index,
            "hole_cards": hole_cards,
            "board": board_cards,
            "hand_actions": hand_actions,
        }

    def card_to_str(self, card):
        return f"{card.rank}{card.suit}"
