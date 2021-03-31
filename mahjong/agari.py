from mahjong.constants import HandType, Tile
from mahjong.error import TileCountError
from mahjong.hand import Hand
from mahjong.util import find_earliest_nonzero_index, modify_list


def is_agari(hand: Hand) -> bool:
    """
    decide given hand is agari-state
    :param hand: Hand object
    :return: boolean
    """
    if hand.type != HandType.AFTER_DRAW:
        raise TileCountError(hand.string, HandType.AFTER_DRAW)
    return is_thirteen_orphan_agari(hand) or is_seven_pairs_agari(hand) or is_normal_agari(hand)


def is_thirteen_orphan_agari(hand: Hand) -> bool:
    if hand.is_opened:
        return False

    concealed_counts = hand.concealed_counts
    for t in Tile.ANY:
        if t not in Tile.TERMINALS_AND_HONORS and concealed_counts[t] > 0:
            return False
        if t in Tile.TERMINALS_AND_HONORS and (concealed_counts[t] == 0 or concealed_counts[t] > 2):
            return False
    return True


def is_seven_pairs_agari(hand: Hand) -> bool:
    if hand.is_opened:
        return False
    pair_counts = len([t for t in Tile.ANY if hand.concealed_counts[t] == 2])
    return pair_counts == 7


def is_normal_agari(hand: Hand) -> bool:
    return _is_normal_agari_rec(0, hand.concealed_counts[:], False)


def _is_normal_agari_rec(index, counts, has_head):
    index = find_earliest_nonzero_index(counts, index)
    if index >= len(counts):
        return True

    if counts[index] >= 2 and not has_head:
        modify_list(counts, [index], -2)
        if _is_normal_agari_rec(index, counts, True):
            return True
        modify_list(counts, [index], 2)

    if counts[index] >= 3:
        modify_list(counts, [index], -3)
        if _is_normal_agari_rec(index, counts, has_head):
            return True
        modify_list(counts, [index], 3)

    if index in Tile.MAKE_STRAIGHTS and counts[index + 1] > 0 and counts[index + 2] > 0:
        modify_list(counts, [index, index + 1, index + 2], -1)
        if _is_normal_agari_rec(index, counts, has_head):
            return True
        modify_list(counts, [index, index + 1, index + 2], 1)

    return False
