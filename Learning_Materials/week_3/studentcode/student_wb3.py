
from approvedimports import *

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
        and what it then does to the openlist

        Returns
        -------
        next working candidate (solution) taken from openlist
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
