class DecisionTree:
    def __init__(self, root_node):
        self.fringe = [root_node]

    def run(self):
        while not self._solution_found():
            self._expand_next()

        return self._solution_found()

    def _expand_next(self):
        cheapest_node = self.fringe[0]
        for node in self.fringe[1:]:
            if node.f < cheapest_node.f:
                cheapest_node = node

        self.fringe.remove(cheapest_node)
        print(cheapest_node.f, cheapest_node.h)
        self.fringe.extend(cheapest_node.expand())

    def _solution_found(self):
        for node in self.fringe:
            if node.h == 0:
                return node
        return False
