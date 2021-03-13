class TileInputError(Exception):
    def __init__(self, tile_string):
        self.tile_string = tile_string

    def __str__(self):
        return self.tile_string + '은 올바른 타일 입력이 아닙니다.'
