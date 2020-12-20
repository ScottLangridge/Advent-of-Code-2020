from day20.ImageTile import ImageTile


class State:
    def __init__(self, tile_matrix):
        self._tile_matrix = tile_matrix
        self._tile_pos_dict = None
        self._build_tile_pos_dict()

    def _build_tile_pos_dict(self):
        tile_pos_dict = {}
        for y in range(len(self._tile_matrix)):
            for x in range(len(self._tile_matrix[0])):
                tile = self._tile_matrix[y][x]
                tile_pos_dict[tile.tid] = (x, y)
        self._tile_pos_dict = tile_pos_dict

    def get_tids(self):
        return list(self._tile_pos_dict.keys())

    def get_tile(self, tid):
        tile_pos = self._tile_pos_dict[tid]
        return self._tile_matrix[tile_pos[1]][tile_pos[0]]

    def get_tile_pos(self, tid):
        return self._tile_pos_dict[tid]

    def set_tile(self, x, y, tile):
        self._tile_matrix[y][x] = tile
        self._build_tile_pos_dict()

    def count_mismatches(self):
        mismatches = 0
        side_length = len(self._tile_matrix)

        for y in range(side_length):
            for x in range(side_length):
                tile = self._tile_matrix[y][x]
                tile_right = self._tile_matrix[y][x + 1] if x + 1 < side_length else False
                tile_below = self._tile_matrix[y + 1][x] if y + 1 < side_length else False

                if tile_right:
                    if tile.borders['e'] != tile_right.borders['w']:
                        mismatches += 1
                if tile_below:
                    if tile.borders['s'] != tile_below.borders['n']:
                        mismatches += 1

        return mismatches
