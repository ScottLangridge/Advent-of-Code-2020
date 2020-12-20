class ImageTile:
    def __init__(self, tile_string):
        tile_rows = tile_string.splitlines()
        self.tid = int(tile_rows[0].strip(':').split(' ')[1])
        self.image = [list(row) for row in tile_rows[1:]]

        east_border, west_border = [], []
        for row in self.image:
            east_border.append(row[-1])
            west_border.append(row[0])

        self.borders = {
            'n': self.image[0],
            's': self.image[-1],
            'e': east_border,
            'w': west_border
        }

    def __str__(self):
        mid = ''
        for row in range(1, len(self.image) - 1):
            mid = mid + self.borders['w'][row] + '........' + self.borders['e'][row] + '\n'

        return f'Tile {self.tid}:\n{"".join(self.borders["t"])}\n{mid}{"".join(self.borders["b"])}'

    def rotate_right(self):
        temp = self.borders['n']
        self.borders['n'] = list(reversed(self.borders['w']))
        self.borders['w'] = self.borders['s']
        self.borders['s'] = list(reversed(self.borders['e']))
        self.borders['e'] = temp

    def rotate_left(self):
        temp = list(reversed(self.borders['n']))
        self.borders['n'] = self.borders['e']
        self.borders['e'] = list(reversed(self.borders['s']))
        self.borders['s'] = self.borders['w']
        self.borders['w'] = temp
