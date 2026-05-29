class Game:
    def __init__(self):
        self.current_player = 'X'
        self.is_winner = False
        self.endgame = False
        self.row_size = 6
        self.col_size = 7
        self.board = self.create_board()

    def create_board(self):
        grid = []
        for row in range(self.row_size):
            current_row = []
            for col in range(self.col_size):
                current_row.append(' ')
            grid.append(current_row)
        return grid

    def switch_players(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def is_draw(self):
        for col in range(self.col_size):
            if self.board[0][col] == ' ':
                return False
        return True

    def count_direction(self, row, col, row_step, col_step, player):
        count = 0
        row += row_step
        col += col_step

        while (
            0 <= row < self.row_size
            and 0 <= col < self.col_size
            and self.board[row][col] == player
        ):
            count += 1
            row += row_step
            col += col_step

        return count

    def check_win(self, row, col, player):
        directions = [
            (0, 1),    # horizontal
            (1, 0),    # vertical
            (1, 1),    # diagonal down-right / up-left
            (-1, 1)    # diagonal up-right / down-left
        ]

        for row_step, col_step in directions:
            count = 1
            count += self.count_direction(row, col, row_step, col_step, player)
            count += self.count_direction(row, col, -row_step, -col_step, player)

            if count >= 4:
                return True

        return False

    def player_move(self, selected_column):
        if self.endgame:
            return "Game has already ended"

        if not isinstance(selected_column, int):
            return "The column has to be an int"

        if selected_column < 0 or selected_column >= self.col_size:
            return "Invalid column selected"

        for row in range(self.row_size - 1, -1, -1):
            if self.board[row][selected_column] == ' ':
                self.board[row][selected_column] = self.current_player

                if self.check_win(row, selected_column, self.current_player):
                    self.is_winner = True
                    self.endgame = True
                    return f"Current player {self.current_player} has won"

                if self.is_draw():
                    self.endgame = True
                    return "Game is a draw"

                self.switch_players()
                return "Move accepted"

        return "Column is full"

    def display_board(self):
        for row in self.board:
            print(row)