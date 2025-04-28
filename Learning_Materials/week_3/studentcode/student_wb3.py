
from approvedimports import *

class DepthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__ method.
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm.
    """

    def __str__(self):
        return "depth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """void in superclass
        In sub-classes should implement different algorithms
        depending on what item it picks from self.open_list
        and what it then does to the openlist

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # Pseudocode:
        # 1. Set my_index to the last index in the open list
        # 2. Retrieve the candidate solution at that index
        # 3. Remove that candidate from the open list
        # 4. Return the retrieved candidate

        my_index = len(self.open_list) - 1              
        next_soln = self.open_list[my_index]            
        self.open_list.pop(my_index)                    

        # <==== insert your pseudo-code and code above here
        return next_soln

class BreadthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "breadth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements the breadth-first search algorithm

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # Pseudocode:
        # 1. Set the index of the next node to explore
        # 2. Retrieve the candidate solution from the front of the open_list
        # 3. Remove it from the open_list 
        # 4. Return that candidate solution for further exploration

        my_index = 0
        next_soln = self.open_list[my_index]
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

        # Pseudocode:
        # 1. If the open list is empty, return None 
        # 2. Initialize best_index to 0 (assume first element is best initially)
        # 3. Loop through all elements in open_list:
        #       -> If an element has better (lower) quality than the current best,
        #         update best_index
        # 4. Remove and return the candidate solution at best_index

        if not self.open_list:                      
            return None

        best_index = 0                              
        for i in range(len(self.open_list)):        
            if self.open_list[i].quality < self.open_list[best_index].quality:
                best_index = i                      

        next_soln = self.open_list.pop(best_index)  

        # <==== insert your pseudo-code and code above here
        return next_soln

class AStarSearch(SingleMemberSearch):
    """Implementation of A-Star  search."""

    def __str__(self):
        return "A Star"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements A-Star by finding, popping and returning member from openlist
        with lowest combined length+quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # Pseudocode:
        # 1. If the open list is empty return none
        # 2. Set best_index to 0 
        # 3. For each candidate in the open list:
        #    a. Calculate the total estimated cost:
        #       f(n) = g(n) + h(n)
        #       where:
        #         g(n) = path cost so far (length of variable_values)
        #         h(n) = heuristic estimate to goal (quality)
        #    b. If f(n) is lower than the best so far, update best_index
        # 4. Remove the candidate at best_index from the open list
        # 5. Return it as the next solution

        # IF IsEmpty(open_list) THEN
        if not self.open_list:
            return None
        
        # bestChild <-- GetMemberWithHighestcombined(openList)
        best_index = 0
        for i in range(len(self.open_list)):
            combined_cost = len(self.open_list[i].variable_values) + self.open_list[i].quality
            best_combined_cost = len(self.open_list[best_index].variable_values) + self.open_list[best_index].quality
            if combined_cost < best_combined_cost:
                best_index = i
        
        # RETURN bestChild
        next_soln = self.open_list.pop(best_index)

        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour = 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # Load base maze
    maze = Maze(mazefile="maze.txt")

    maze.contents[3][4] = hole_colour  # Open path to trick DFS
    maze.contents[8][4] = wall_colour  # Block DFS at the end

    maze.contents[10][6] = hole_colour  # Another DFS trap
    maze.contents[14][6] = wall_colour  # Dead-end
    maze.contents[16][1] = hole_colour  # Dead-end
    maze.contents[19][4] = hole_colour  # Dead-end

    maze.contents[8][1] = hole_colour
    maze.contents[12][9] = wall_colour
    maze.contents[11][12] = wall_colour
    maze.contents[9][2] = wall_colour
    maze.contents[10][19] = wall_colour
    maze.contents[18][5] = wall_colour
    
    

    
    # Save the maze
    maze.save_to_txt("maze-breaks-depth.txt")


    # <==== insert your code above here

def create_maze_depth_better():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work
    maze = Maze(mazefile="maze.txt")
    maze.contents[1][8] = wall_colour
    maze.contents[9][10] = wall_colour
    maze.contents[15][6] = wall_colour
    maze.contents[13][2] = wall_colour
    maze.contents[12][13] = wall_colour
    maze.contents[2][13] = wall_colour
    maze.save_to_txt("maze-depth-better.txt")



    # <==== insert your code above here
