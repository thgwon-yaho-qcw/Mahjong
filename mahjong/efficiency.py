from mahjong.constants import HandType, Tile
from mahjong.hand import Hand
from mahjong.error import TileCountError
from mahjong.shanten import calculate_shanten


def _calculate_efficient_tiles(hand):
    efficient_tiles = []
    num_tiles = 0

    shanten = calculate_shanten(hand)
    for i in Tile.ANY:
        if hand.count_tile(i) == 4:
            continue

        hand.draw(i)
        if shanten - 1 == calculate_shanten(hand):
            efficient_tiles.append(i)
            num_tiles += 5 - hand.count_tile(i)
        hand.discard(i)

    return efficient_tiles, num_tiles


def calculate_efficiency(hand: Hand):
    if hand.hand_type != HandType.AFTER_DRAW:
        raise TileCountError(hand.string, HandType.AFTER_DRAW)

    shanten = calculate_shanten(hand)
    efficiency = []
    for i in Tile.ANY:
        if hand.count_tile(i) == 0:
            continue
        hand.discard(i)
        if shanten == calculate_shanten(hand):
            data = (i, *_calculate_efficient_tiles(hand))
            if data[2] > 0:
                efficiency.append(data)
        hand.draw(i)

    efficiency.sort(key=lambda x: x[2], reverse=True)
    return efficiency
