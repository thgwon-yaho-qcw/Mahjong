import re
from mahjong.constants import Tile
from mahjong.error import TileInputError


def string_to_counts(string: str) -> list[int]:
    """
    convert tile string to list of appearance of each tile
    :param string: string
    :return: int list
    """
    pattern = re.compile(Tile.RE_STRING)
    matches = pattern.findall(string)

    if ''.join([x + y for (x, y) in matches]) != string:
        raise TileInputError(string)

    counts = [0] * len(Tile.ANY)
    for nums, tile_type in matches:
        if tile_type == Tile.Type.HONORS and ('8' in nums or '9' in nums):
            raise TileInputError(string)
        for c in nums:
            counts[ord(c) - ord('0') + Tile.Type.OFFSET[tile_type]] += 1

    return counts
