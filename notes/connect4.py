class Game:
    def __init__(self):
        self.current_player = 'X'
        self.row_size = 6
        self.col_size = 7
        self.board = self.create_board()
        self.is_winner = False
        self.quit = False
        
    def create_board(self):
        grid = []
        for rows in range(self.row_size):
            rows = []
            for cols in range(self.col_size):
                rows.append(' ')
            grid.append(rows)
        return grid
    
    def switch_players(self):
        if self.current_player == 'X':
            self.current_player = 'O'
            return "Player 2's turn"
        else:
            self.current_player = 'X'
            return "Player 1's turn"
        
    def count_directions(self,row,col,col_step,row_step,player):
        count = 0
        row += row_step
        col += col_step
        
        while (0<= row < self.row_size
               and 0<= col <self.col_size
               and self.board[row][col] == player):
            count += 1
            row += row_step
            col += col_step
        return count
    
    def check_winner(self,row,selected_col,player):
        direction = [(0,1),(1,1),(1,0),(-1,1)]
        
        for row_step, col_step in direction:
            count = 1
            
            count += self.count_directions(row,selected_col,col_step,row_step,player)
            count += self.count_directions(row,selected_col,-col_step,-row_step,player)
            
            if count >= 4:
                return True
        return False

        
    def show_game(self):
        for rows in self.board:
            print(rows)
    
    def is_draw(self):
        for col in range(self.col_size):
            if self.board[0][col] == ' ':
                return False
        return True
       
        
        
        
    def make_move(self,selected_col):
        for row in range(self.row_size - 1, -1 , -1):
            if self.board[row][selected_col] == ' ':
                self.board[row][selected_col] = self.current_player
                if self.check_winner(row,selected_col,self.current_player):
                    self.is_winner = True
                    return f"Game Over player: {self.current_player} Won"
                if self.is_draw():
                    return "Its a tie"
                else:
                    self.switch_players()
                    return "Move accepted"
            
                
                
            