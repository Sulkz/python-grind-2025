import random

class Player:

    def __init__(self, name):

        self.name = name

        self.total_score = 0

class DiceGame:

    def __init__(self, player1_name="Player 1", player2_name="Player 2", winning_score=100):

        self.players = [

            Player(player1_name),

            Player(player2_name)

        ]

        self.current_player_index = 0

        self.turn_score = 0

        self.winning_score = winning_score

        self.game_over = False

        self.winner = None

    def current_player(self):

        return self.players[self.current_player_index]

    def switch_player(self):

        self.current_player_index = 1 - self.current_player_index

        self.turn_score = 0

    def roll(self):

        if self.game_over:

            return "Game already ended"

        roll_value = random.randint(1, 6)

        if roll_value == 1:

            self.turn_score = 0

            player_name = self.current_player().name

            self.switch_player()

            return f"{player_name} rolled a 1. Turn lost."

        self.turn_score += roll_value

        return f"{self.current_player().name} rolled {roll_value}. Turn score: {self.turn_score}"

    def hold(self):

        if self.game_over:

            return "Game already ended"

        player = self.current_player()

        player.total_score += self.turn_score

        if player.total_score >= self.winning_score:

            self.game_over = True

            self.winner = player

            return f"{player.name} wins with {player.total_score} points"

        message = f"{player.name} holds. Total score: {player.total_score}"

        self.switch_player()

        return message

    def get_scores(self):

        return {

            player.name: player.total_score

            for player in self.players

        }

    def display_state(self):

        return {

            "current_player": self.current_player().name,

            "turn_score": self.turn_score,

            "scores": self.get_scores(),

            "game_over": self.game_over,

            "winner": self.winner.name if self.winner else None

        }

# Demo

game = DiceGame("Reuel", "Alex")

print(game.display_state())

print(game.roll())

print(game.roll())

print(game.hold())

print(game.display_state())