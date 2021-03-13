import re
from operator import add
from mahjong.constants import Tile, CallType
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


def string_to_counts_and_call_counts(string: str) -> tuple[list[int], list[list[int]]]:
    """
    convert tile string to counts and call counts list
    :param string: string
    :return: int list, list of int lists
    """
    parts = string.split(',')
    all_tiles_counts = concealed_tile_counts = string_to_counts(parts[0])

    calls = []
    for part in parts[1:]:
        call_type = part[:3]
        if call_type not in CallType.ANY:
            raise TileInputError(part)

        call_counts = string_to_counts(part[3:])

        if call_type in CallType.KAN and sum(call_counts) != 4:
            raise TileInputError(part)

        if call_type not in CallType.KAN and sum(call_counts) != 3:
            raise TileInputError(part)

        calls.append(call_counts)
        all_tiles_counts = map(add, all_tiles_counts, call_counts)

    for t in all_tiles_counts:
        if t < 0 or t > 4:
            raise TileInputError(string)

    return concealed_tile_counts, calls
