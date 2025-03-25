
class DepthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "depth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """void in superclass
        In sub-classes should implement different algorithms
        depending on what item it picks from self.open_list
        and what it then does to the open list

        Returns
        -------
        next working candidate (solution) taken from open list
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here
        # my_index ← GetLastIndex(open_list)
        # the_candidate ← open_list[my_index]
        # RemoveFromOpenList(my_index)
        # Return(the_candidate)

        # ====> Actual Code:
        my_index = len(self.open_list) - 1  
        the_candidate = self.open_list[my_index]  
        self.open_list.pop(my_index)  

        # <==== insert your pseudo-code and code above here
        return next_soln

class BestFirstSearch(SingleMemberSearch):
    """Implementation of Best-First search."""

    def __str__(self):
        return "best-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements Best First by finding, popping and returning member from openlist
        with best quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # If open_list is empty, return None
        if not self.open_list:
            return None

        # Find the candidate with the lowest quality
        next_soln = min(self.open_list, key=lambda c: c.quality)

        # Remove it from the open_list
        self.open_list.remove(next_soln)

        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    
    from maze import Maze
    m = Maze(5, 5)  # rows, cols

    m.set_start(0, 0)
    m.set_goal(1, 3)

    walls = [
        (0, 2), (0, 3), (0, 4),
        (1, 2),         (1, 4),
        (2, 2), (2, 3), (2, 4),
        (3, 0),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
    ]
    for r, c in walls:
        m.set(r, c, wall_colour)

    # Uncomment during dev only
    # m.show_maze()

    m.save('maze-breaks-depth.txt')
    
    # <==== insert your code above here
