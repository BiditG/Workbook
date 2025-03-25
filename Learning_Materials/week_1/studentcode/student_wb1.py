from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "this code only works for 4 digits"

    # create an empty candidate solution
    my_attempt = CandidateSolution()

#insert your code below here
    for digit1 in puzzle.value_set:
        for digit2 in puzzle.value_set:
            for digit3 in puzzle.value_set:
                for digit4 in puzzle.value_set:
                    my_attempt.variable_values = [digit1, digit2, digit3, digit4]
                    try:
                        result = puzzle.evaluate(my_attempt.variable_values)
                        if result == 1:
                            return my_attempt.variable_values
                    except Exception:
                        pass
#insert your code above here
#should never get here
    return [-1, -1, -1, -1]


def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    for i in range(namearray.shape[0]):
        # Slice the last 6 characters of each row
        family_chars = namearray[i, -6:]
        family_name = ''.join(family_chars).strip()
        family_names.append(family_name)
    
    # <==== insert your code above here
    return family_names


def check_sudoku_array(attempt: np.ndarray) -> int:
    tests_passed = 0
    slices = []  # this will be a list of numpy arrays

    # ====> insert your code below here

    # Assert the shape is exactly (9, 9)
    assert attempt.ndim == 2 and attempt.shape[0] == 9 and attempt.shape[1] == 9, "Input must be a 9x9 2D array."

    # Add 9 row slices
    for i in range(9):
        slices.append(attempt[i, :])

    # Add 9 column slices
    for j in range(9):
        slices.append(attempt[:, j])

    # Add 9 sub-squares (3x3)
    for row in range(0, 9, 3):        # rows: 0, 3, 6
        for col in range(0, 9, 3):    # cols: 0, 3, 6
            square = attempt[row:row+3, col:col+3]
            slices.append(square.flatten())  # flatten 3x3 into 1D for uniqueness check

    # Check uniqueness for each slice
    for slice in slices:
        if len(np.unique(slice)) == 9:
            tests_passed += 1

    # <==== insert your code above here

    # return count of tests passed
    return tests_passed
