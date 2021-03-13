class TileInputError(Exception):
    def __init__(self, tile_string):
        self.tile_string = tile_string

    def __str__(self):
        return self.tile_string + '은 올바른 타일 입력이 아닙니다.'


class TileCountError(Exception):
    def __init__(self, tile_string, hand_type):
        self.tile_string = tile_string
        self.hand_type = hand_type

    def __str__(self):
        return '{}의 손패 갯수가 3n+{}개가 아닙니다.'.format(self.tile_string, self.hand_type)
