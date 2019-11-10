from random import randint

from BoardClasses import Board


# The following part should be completed by students.
# Students can modify anything except the class name and exisiting functions and varibles.

class Tree():
    def __init__(self, color, move=None):
        self.color = color
        self.move = move
        self.value = None
        self.children = []


class StudentAI():

    def __init__(self, col, row, p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col, row, p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1: 2, 2: 1}
        self.color = 2

    def get_move(self, move):
        if len(move) != 0:
            self.board.make_move(move, self.opponent[self.color])  # Run opponent's move for self.board
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        # print("ALL MOVES: ", moves)

        # #Random Moves
        # index = randint(0,len(moves)-1)#Inclusive of both bounds
        # inner_index =  randint(0,len(moves[index])-1)
        # move = moves[index][inner_index]

        # #Print heuristic points before/after move
        # print("Points: ", self.board_points())
        # self.board.make_move(move,self.color)
        # print("Points: ", self.board_points())

        # #Print avail moves
        # print("%%%%%%%%%%%%%%%%%%% STUDENT-AI's BOARD")
        # self.board.show_board()
        # print("%%%%%%%%%%%%%%%%%%% STUDENT-AI's POSSIBLE MOVES")
        '''
        for i,checker_moves in enumerate(moves):
            print(i,':[',end="")
            for j, move in enumerate(checker_moves):
                print(j,":",move,end=", ")
            print("]")
            '''

        # Look one move ahead
        max_pts = -1000000
        cur_move = moves[0][0]

        '''
        for i in range(len(moves)):
            for j in range(len(moves[i])):  # For each possible move
                self.board.make_move(moves[i][j], self.color)  # Try move
                if self.board_points() > max_pts:  # Check eval function for board
                    max_pts = self.board_points()  # Update max points
                    cur_move = moves[i][j]  # update to move w/ most points
                self.board.undo()
        '''

        # # Start Tree
        # root = Tree(self.opponent[self.color])  # Tree root
        # for i in range(len(moves)):
        #     for j in range(len(moves[i])):  # For each first move
        #         root.children.append(Tree(self.color, moves[i][j]))  # Add children to root node
        # '''
        # Root
        # Children
        # '''
        #
        # l1_win = False
        # l2_win = False
        # win_move = None
        #
        # # Create Tree
        # for l1_node in root.children:
        #     # print("l1node")
        #     self.board.make_move(l1_node.move, l1_node.color)
        #     if (self.board.is_win(l1_node.color) == self.color):
        #         l1_win = True
        #         win_move = l1_node.move
        #         break
        #     l1_moves = self.board.get_all_possible_moves(self.opponent[l1_node.color])
        #     # print(l1_node, "\n", l1_moves)
        #     for i in range(len(l1_moves)):
        #         for j in range(len(l1_moves[i])):
        #             l1_node.children.append(Tree(self.opponent[l1_node.color], l1_moves[i][j]))
        #             '''
        #                 l0: Root
        #                 l1: Children
        #                 l2: ChildrenChildren
        #             '''
        #     for l2_node in l1_node.children:
        #         self.board.make_move(l2_node.move, l2_node.color)
        #         if (self.board.is_win(l2_node.color) == self.color):
        #             l2_win = True
        #             break
        #         l2_moves = self.board.get_all_possible_moves(self.opponent[l2_node.color])
        #         # print(l2_node, "\n", l2_moves)
        #         for i in range(len(l2_moves)):
        #             for j in range(len(l2_moves[i])):
        #                 l2_node.children.append(Tree(self.opponent[l2_node.color], l2_moves[i][j]))
        #                 '''
        #                     l0: Root
        #                     l1: Children
        #                     l2: Children^2
        #                     l3: Children^3
        #                 '''
        #         self.board.undo()
        #     if l2_win:
        #         win_move = l1_node.move
        #         break
        #     self.board.undo()
        #
        # if l1_win or l2_win:
        #     cur_move = win_move
        #
        # else:
        #     # Apply heuristic values for tree
        #     for l1_node in root.children:
        #         self.board.make_move(l1_node.move, l1_node.color)
        #         for l2_node in l1_node.children:
        #             self.board.make_move(l2_node.move, l2_node.color)
        #             l2_moves = self.board.get_all_possible_moves(l1_node.color)
        #             for l3_node in l2_node.children:
        #                 self.board.make_move(l3_node.move, l3_node.color)
        #                 l3_node.value = {self.board_points(): []}
        #                 self.board.undo()
        #
        #             self.board.undo()
        #             # print("l2_node_children")
        #             l2_node.value = self.min_max(l2_node.children, l2_node.color)
        #
        #         self.board.undo()
        #
        #         # print("l1_node children")
        #         l1_node.value = self.min_max(l1_node.children, l1_node.color)
        #
        #     # print("root children")
        #     root.value = self.min_max(root.children, root.value)
        #
        #     # self.print_tree(root)
        #
        #     # root.value is dict that should only contain one entry
        #     moves = root.value[list(root.value)[0]]
        #     i = randint(0, len(moves) - 1)
        #     cur_move = moves[i]

        root = Tree(self.opponent[self.color]) #Tree root
        self.rec_tree(root, 6)
        self.rec_heuristic(root)

        avail_moves = root.value[list(root.value)[0]]
        cur_move = avail_moves[0]
        #print(avail_moves)

        self.board.make_move(cur_move, self.color)  # Make the optimal move
        move = cur_move
        return move

    def ftu(self, color): #Function to use (min vs max by color)
        if color == self.color:  # Calculate Min
            return max
        else:  # Calculate Max
            return min

    def min_max(self, children, color):  # Returns dict -> {Max/min value: Moves to get here}
        ftu = self.ftu(color) #Use corresponding min or max depending on color
        value_map = {}
        for child in children:
            for v in child.value.keys():
                value_map.setdefault(v, []).append(child.move)  # D: {heuristic value: Move to make to get here}
        # print(value_map)
        return {ftu(value_map): value_map[ftu(value_map)]}

    def board_points(self):  # 5 + row number for pawns, 5 + row number + 2 for kings
        pts = 0
        for i in range(self.row):
            for j in range(self.col):
                checker = self.board.board[i][j]
                if checker.color == 'B':  # For black side pieces
                    pts += 5 + checker.row
                    if checker.is_king:  # 2 additional pts for king
                        pts += 2
                elif checker.color == 'W':  # FOr white side pieces
                    pts -= 11 - checker.row  # 5 + (6 - Row)
                    if checker.is_king:  # 2 additional pts for king
                        pts -= 2
        return pts if self.color == "B" else -pts

    def print_tree(self, root, level=0):
        # print("PRINTING TREE")

        print("\t" * level, root.value, "->", root.move)
        if len(root.children) != 0:  # Not Leaf node
            for child in root.children:
                self.print_tree(child, level + 1)

    def rec_tree(self, root: Tree, level=1):
        if level == 0:
            pass
        else:
            if root.move is not None:  # Not root of tree
                self.board.make_move(root.move, root.color)
            #Check if win here maybe?
            avail_moves = self.board.get_all_possible_moves(self.opponent[root.color])
            for i in range(len(avail_moves)):
                for j in range(len(avail_moves[i])):
                    #print(root)
                    root.children.append( Tree(self.opponent[root.color], avail_moves[i][j] ) )
            for child in root.children:
                self.rec_tree(child, level - 1)

            if root.move is not None:
                self.board.undo()

    def rec_heuristic(self, root: Tree):
        if root.move is not None:
            self.board.make_move(root.move, root.color)
        if len(root.children) == 0: #Passed node has no children
            pass #Evaluate heuristic for board(and return?)
            root.value = {self.board_points(): []}
        else: #Evaluate rec_heuristic for children, then retrieve values and apply min/max as appropriate
            for child in root.children:
                self.rec_heuristic(child)
            root.value = self.min_max(root.children, root.color)

        if root.move is not None:
            self.board.undo()
'''
    def min_max2(self, children, color):  # Returns dict = {Max/min value: Moves to get here}
        ftu = self.ftu(color)
        value_map = {}
        for child in children:
            for v in child.value.keys():
                value_map.setdefault(v, []).append(child.move)  # D: {heuristic value: Move to make to get here}

        return {ftu(value_map): value_map[ftu(value_map)]}
'''
