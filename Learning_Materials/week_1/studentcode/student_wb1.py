# Save student_wb1.py correctly

from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """Simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # Check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "This code only works for 4-digit locks"

    # Create an empty candidate solution
    my_attempt = CandidateSolution()  # ✅ Fixed
    my_attempt.variable_values = [0, 0, 0, 0]  # ✅ Initialize properly

    # Loop through all possible values for each tumbler
    for digit1 in puzzle.value_set:
        for digit2 in puzzle.value_set:
            for digit3 in puzzle.value_set:
                for digit4 in puzzle.value_set:
                    
                    # Assign the current combination to the candidate solution
                    my_attempt.variable_values = [digit1, digit2, digit3, digit4]

                    # Debug: Print current attempt
                    print(f"Trying: {my_attempt.variable_values}")

                    # Evaluate the attempt and return if correct
                    if puzzle.evaluate(my_attempt.variable_values):  # ✅ Ensure we pass only the list
                        return my_attempt.variable_values

    # If no solution is found, return an invalid combination
    return [-1, -1, -1, -1]
