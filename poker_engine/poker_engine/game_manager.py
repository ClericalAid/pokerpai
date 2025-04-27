from poker_engine.game import Game

class GameManager:
    def __init__(self):
        self.game_dictionary = {}

    def create_game(self, starting_stacks: list[int] = None, game_id: int = None, players: list[str] = []):
        game_id = len(self.game_dictionary)
        self.game_dictionary[game_id] = {
            "game": Game(starting_stacks=starting_stacks),
            "players": players,
        }
        return game_id

    def get_command(self, game_id: int, command: str):
        game = self.game_dictionary[game_id]
        if command == "fold":
            game.fold()
        elif command == "call":
            game.call()
        elif command == "check":
            game.check()
        elif command.startswith("raise"):
            raise_amount = int(command.split(" ")[1])
            game.raise_bet(raise_amount)
        elif command.startswith("relative_pot_raise"):
            raise_percentage = float(command.split(" ")[1])
            game.relative_pot_sized_raise(raise_percentage)
