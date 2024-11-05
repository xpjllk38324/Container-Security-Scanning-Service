class Board:
    def __init__(self, size):
        """Initialize the board with a given size and no queens placed."""
        self._size = size
        self._queens = [-1] * size  # Holds queen positions for each row
        self._solutions = []

    def _is_safe(self, row, col):
        """Check if placing a queen at (row, col) is safe."""
        for r in range(row):
            if self._queens[r] == col or abs(self._queens[r] - col) == abs(r - row):
                return False
        return True

    def _place_queens(self, row=0):
        """Recursive function to place queens row by row."""
        if row == self._size:
            self._add_solution()
            return

        for col in range(self._size):
            if self._is_safe(row, col):
                self._queens[row] = col  # Place queen
                self._place_queens(row + 1)  # Proceed to next row
                self._queens[row] = -1  # Backtrack

    def _add_solution(self):
        """Add the current configuration as a solution."""
        self._solutions.append(self._queens[:])

    def solve(self):
        """Solve the N-Queens problem and store all solutions."""
        self._solutions.clear()
        self._place_queens()

    def display_solution(self, solution_idx, unicode=False):
        """Display a specific solution by index, using unicode queens if specified."""
        if solution_idx < 0 or solution_idx >= len(self._solutions):
            raise IndexError("Solution index out of range.")

        queen_symbol = "♛" if unicode else "Q"
        empty_symbol = "."

        solution = self._solutions[solution_idx]
        for row in range(self._size):
            row_display = ""
            for col in range(self._size):
                row_display += f"{queen_symbol} " if solution[row] == col else f"{empty_symbol} "
            print(row_display)
        print("\n")

    def display_all_solutions(self, unicode=False):
        """Display all solutions, formatted with either unicode or plain characters."""
        for idx, _ in enumerate(self._solutions):
            print(f"Solution {idx + 1}:")
            self.display_solution(idx, unicode=unicode)

    @property
    def solutions(self):
        """Property to access the number of solutions found."""
        return len(self._solutions)


if __name__ == '__main__':
    board = Board(8)
    board.solve()

    # board.display_all_solutions(unicode=False)
    board.display_all_solutions(unicode=True)
