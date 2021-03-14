from mahjong.constants import HandType, Tile
from mahjong.error import TileCountError
from mahjong.hand import Hand


def is_agari(hand: Hand) -> bool:
    """
    decide given hand is agari-state
    :param hand: Hand object
    :return: boolean
    """
    if hand.hand_type != HandType.AFTER_DRAW:
        raise TileCountError(hand.string, HandType.AFTER_DRAW)
    return is_thirteen_orphan_agari(hand) or is_seven_pairs_agari(hand) or is_normal_agari(hand)


def is_thirteen_orphan_agari(hand: Hand) -> bool:
    if hand.is_called:
        return False

    concealed_counts = hand.concealed_counts
    for t in Tile.ANY:
        if t not in Tile.TERMINALS_AND_HONORS and concealed_counts[t] > 0:
            return False
        if t in Tile.TERMINALS_AND_HONORS and (concealed_counts[t] == 0 or concealed_counts[t] > 2):
            return False
    return True


def is_seven_pairs_agari(hand: Hand) -> bool:
    if hand.is_called:
        return False
    return len([t for t in Tile.ANY if hand.concealed_counts[t] == 2]) == 7


def is_normal_agari(hand: Hand) -> bool:
    def _is_normal_form_rec(counts, has_head):
        if sum(counts) == 0:
            return has_head

        min_index, _ = min([(x, y) for x, y in enumerate(counts) if y > 0])

        if counts[min_index] >= 2 and not has_head:
            new_counts = counts[:]
            new_counts[min_index] -= 2
            if _is_normal_form_rec(new_counts, True):
                return True

        if counts[min_index] >= 3:
            new_counts = counts[:]
            new_counts[min_index] -= 3
            if _is_normal_form_rec(new_counts, has_head):
                return True

        if min_index in Tile.MAKE_STRAIGHTS and counts[min_index] > 0 \
                and counts[min_index + 1] > 0 and counts[min_index + 2] > 0:
            new_counts = counts[:]
            new_counts[min_index] -= 1
            new_counts[min_index + 1] -= 1
            new_counts[min_index + 2] -= 1
            if _is_normal_form_rec(new_counts, has_head):
                return True

        return False

    return _is_normal_form_rec(hand.concealed_counts, False)
