class Maze:
    def __init__(self, m: int, n : int) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.grid_representation = []
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.grid_representation.append(grid_row)
    
    def add_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        self.grid_representation[x][y] =1
        pass
    def remove_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        self.grid_representation[x][y] =0
        pass
    def is_ghost(self, x : int, y: int) -> bool:
        # IMPLEMENT YOUR FUNCTION HERE
        if(self.grid_representation[x][y]==1):
            return True
        return False
    def print_grid(self) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        x = len(self.grid_representation)
        y = len(self.grid_representation[0])
        for i in range(x):
            for j in range(y):
                print(str(self.grid_representation[i][j]), end =" ")
            print("")
        return False