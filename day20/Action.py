import copy


class Rotate:
    def __init__(self, tid, rotations):
        self.tid = tid
        self.direction = 'left' if rotations < 0 else 'right'
        self.rotations = abs(rotations)

    def apply(self, state):
        state = copy.deepcopy(state)
        tile = state.get_tile(self.tid)
        rotate = tile.rotate_left if self.direction == 'left' else tile.rotate_right
        for _ in range(self.rotations):
            rotate()
        return state


class Swap:
    def __init__(self, tid1, tid2):
        self.tid1 = tid1
        self.tid2 = tid2

    def apply(self, state):
        state = copy.deepcopy(state)
        tile1 = state.get_tile(self.tid1)
        tile2 = state.get_tile(self.tid2)
        tile1_pos = state.get_tile_pos(self.tid1)
        tile2_pos = state.get_tile_pos(self.tid2)
        state.set_tile(tile1_pos[0], tile1_pos[1], tile2)
        state.set_tile(tile2_pos[0], tile2_pos[1], tile1)
        return state
