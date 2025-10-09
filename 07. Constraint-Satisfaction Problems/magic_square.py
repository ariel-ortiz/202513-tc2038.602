from typing import NamedTuple, cast
from csp import Constraint, CSP
from itertools import permutations, batched

type Grid = list[list[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


def convert_to_grid(assignment: dict[int, GridLocation]) -> Grid:
    square: Grid = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for var, (row, col) in assignment.items():
        square[row][col] = var
    return square


def is_magic_square(square: Grid) -> bool:
    ((a, b, c),
     (d, e, f),
     (g, h, i)) = square
    return (   (a + b + c) # Rows  
            == (d + e + f)
            == (g + h + i)
            == (a + d + g) # Columns
            == (b + e + h)
            == (c + f + i)
            == (a + e + i) # Diagonals 
            == (g + e + c))


class MagicSquareConstraint(Constraint[int, GridLocation]):

    def __init__(self, variables: list[int]) -> None:
        super().__init__(variables)
        self.variables: list[int] = variables

    def satisfied(self, assignment: dict[int, GridLocation]) -> bool:
        if len(assignment) != len(set(assignment.values())):
            return False
        if len(assignment) < 9:
            return True
        return is_magic_square(convert_to_grid(assignment))
    

def solve_magic_square() -> None:
    variables: list[int] = list(range(1, 10))
    all_grid_locations: list[GridLocation] = [GridLocation(r, c) 
                                              for r in range(3) 
                                              for c in range(3)]
    domains: dict[int, list[GridLocation]] = {
        var: all_grid_locations for var in variables
    }
    csp: CSP[int, GridLocation] = CSP(variables, domains)
    csp.add_constraint(MagicSquareConstraint(variables))
    solution: dict[int, GridLocation] | None = csp.backtracking_search()
    if solution:
        print(convert_to_grid(solution))
    else:
        print("No solution found :(")


def brute_force_magic_square():
    for p in permutations(range(1, 10)):
        grid: Grid = cast(Grid, list(batched(p, 3)))
        if is_magic_square(grid):
            print(grid)


if __name__ == "__main__":
    # a = GridLocation(1, 2)
    # b = GridLocation(2, 2)
    # print(a == b)
    # r, c = a
    # print(f'{r = }')
    # print(f'{c = }')
    # print(f'{b.row = }')
    # print(f'{b.column = }')
    # print(f'{b[0] = }')
    # print(f'{b[1] = }')
    # print(convert_to_grid({1: GridLocation(0, 0),
    #                        2: GridLocation(1, 0),
    #                        3: GridLocation(2, 0),
    #                        4: GridLocation(0, 1),
    #                        5: GridLocation(1, 1),
    #                        6: GridLocation(2, 1),
    #                        7: GridLocation(0, 2),
    #                        8: GridLocation(1, 2),
    #                        9: GridLocation(2, 2)}))
    # print(is_magic_square([[4, 3, 8],
    #                        [9, 5, 1],
    #                        [2, 7, 6]]))
    solve_magic_square()
    brute_force_magic_square()