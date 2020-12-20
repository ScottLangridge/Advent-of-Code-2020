from day20.Action import Rotate, Swap


class DecisionTreeNode:
    def __init__(self, *, parent_node=None, action=None, state=None):
        argument_err_msg = 'Acceptable arguments for DecisionTreeNode are (state=Foo) or (parent_node=foo, action=bar)'
        if state is None and ((parent_node is None) or (action is None)):
            raise SyntaxError(argument_err_msg)
        elif state is not None and not ((parent_node is None) and (action is None)):
            raise SyntaxError(argument_err_msg)

        # Init root node
        if parent_node is None and action is None:
            self.state = state  # set to default state
            self.h = self.state.count_mismatches()
            self.g = 0
            self.f = self.g + self.h

        # Init child node
        else:
            self.state = action.apply(parent_node.state)

            # See https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
            self.h = self.state.count_mismatches()
            self.g = parent_node.g + 1
            self.f = self.g + self.h

    def expand(self):
        tiles = self.state.get_tids()
        new_nodes = []

        # Expand rotates
        for tile in tiles:
            for i in range(1, 4):
                rotate = Rotate(tile, i)
                new_nodes.append(DecisionTreeNode(parent_node=self, action=rotate))

        # Expand swaps
        for tile in tiles:
            for tile2 in tiles:
                if tile != tile2:
                    swap = Swap(tile, tile2)
                    new_nodes.append(DecisionTreeNode(parent_node=self, action=swap))

        return new_nodes

# Expand swaps
