from mahjong.constants import HandType, Tile
from mahjong.hand import Hand
from mahjong.error import TileCountError
from mahjong.shanten import calculate_shanten


def calculate_efficiency(hand: Hand):
    """
    calculate efficiency list like Tenhou
    :param hand: hand object
    :return: list of tuple(int, list[int], int)s
    """
    if hand.type != HandType.AFTER_DRAW:
        raise TileCountError(hand.string, HandType.AFTER_DRAW)

    shanten = calculate_shanten(hand)
    efficiency = []

    for discard_candidate in Tile.ANY:
        if hand.count_tile(discard_candidate) == 0:
            continue

        hand.discard(discard_candidate)
        if shanten == calculate_shanten(hand):
            efficiency_data = (discard_candidate, *_calculate_efficient_tiles(hand))
            if efficiency_data[2] > 0:
                efficiency.append(efficiency_data)
        hand.draw(discard_candidate)

    efficiency.sort(key=lambda x: x[2], reverse=True)
    return efficiency


def _calculate_efficient_tiles(hand: Hand):
    efficient_tiles = []
    num_tiles = 0

    shanten = calculate_shanten(hand)
    for draw_candidate in Tile.ANY:
        if hand.count_tile(draw_candidate) == 4:
            continue
        hand.draw(draw_candidate)
        if shanten - 1 == calculate_shanten(hand):
            efficient_tiles.append(draw_candidate)
            num_tiles += 5 - hand.count_tile(draw_candidate)
        hand.discard(draw_candidate)

    return efficient_tiles, num_tiles
