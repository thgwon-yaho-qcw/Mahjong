from mahjong.constants import Tile


class TileInputError(Exception):
    """
    tile_string이 valid하지 않음
    """

    def __init__(self, tile_string):
        self.tile_string = tile_string

    def __str__(self):
        return self.tile_string + '은 올바른 타일 입력이 아닙니다.'


class TileCountError(Exception):
    """
    함수를 호출할때, 손패의 장수가 다름
    """

    def __init__(self, tile_string, hand_type):
        self.tile_string = tile_string
        self.hand_type = hand_type

    def __str__(self):
        return '{}의 손패 갯수가 3n+{}개가 아닙니다.'.format(self.tile_string, self.hand_type)


class TileDiscardError(Exception):
    """
    타패할 타일이 손에 없음
    """

    def __init__(self, tile_string, tile):
        self.tile_string = tile_string
        self.tile = tile

    def __str__(self):
        return '{}에 {}를 버릴 수 없습니다.'.format(self.tile_string, self.tile)


class TileDrawError(Exception):
    """
    쯔모할 타일이 이미 손에 전부 들고 있음
    """

    def __init__(self, tile_string, tile):
        self.tile_string = tile_string
        self.tile = tile

    def __str__(self):
        return '{}에 {}를 뽑을 수 없습니다.'.format(self.tile_string, Tile.STRING[self.tile])
