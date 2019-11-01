from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])#Run opponent's move for self.board
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)

        # #Random Moves
        # index = randint(0,len(moves)-1)#Inclusive of both bounds
        # inner_index =  randint(0,len(moves[index])-1)
        # move = moves[index][inner_index]
        # print("Points: ", self.board_points())
        # self.board.make_move(move,self.color)
        # print("Points: ", self.board_points())

        #Print avail moves
        print("%%%%%%%%%%%%%%%%%%% STUDENT-AI's BOARD")
        self.board.show_board()
        print("%%%%%%%%%%%%%%%%%%% STUDENT-AI's POSSIBLE MOVES")
        for i,checker_moves in enumerate(moves):
            print(i,':[',end="")
            for j, move in enumerate(checker_moves):
                print(j,":",move,end=", ")
            print("]")

        #Look one move ahead
        max_pts = -1000000
        cur_move = moves[0][0]
        for i in range(len(moves)):
            for j in range(len(moves[i])):#For each possible move
                self.board.make_move(moves[i][j], self.color)#Try move
                if self.board_points() > max_pts:#Check eval function for board
                    max_pts = self.board_points()#Update max points
                    cur_move = moves[i][j]#update to move w/ most points
                self.board.undo()
        print("MOVE MADE: ", cur_move)
        self.board.make_move(move, self.color)#Make the optimal move
        move = cur_move
        return move
    def board_points(self): #5 + row number for pawns, 5 + row number + 2 for kings
        pts = 0
        for i in range(self.row):
            for j in range(self.col):
                checker = self.board.board[i][j]
                if checker.color == 'B':#For black side pieces
                    pts += 5 + checker.row
                    if checker.is_king:#2 additional pts for king
                        pts += 2
                elif checker.color ==  'W':#FOr white side pieces
                    pts -= 11 - checker.row #5 + (6 - Row)
                    if checker.is_king:#2 additional pts for king
                        pts -= 2
        return pts if self.color == "B" else -pts

