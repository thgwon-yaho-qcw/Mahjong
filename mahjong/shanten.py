from mahjong.constants import Tile, HandType
from mahjong.error import TileCountError
from mahjong.hand import Hand
from mahjong.util import find_earlist_nonzero_index, modify_list


def calculate_shanten(hand: Hand, use_seven_pairs=True, use_thirteen_orphans=True) -> int:
    if hand.type == HandType.INVALID:
        raise TileCountError(hand.string, HandType.BEFORE_DRAW)

    results = [_calculate_normal_shanten(hand)]
    if use_seven_pairs:
        results.append(_calculate_seven_pairs_shanten(hand))
    if use_thirteen_orphans:
        results.append(_calculate_thirteen_orphans_shanten(hand))

    return min(results)


def _erase_partial_set(index, counts, complete_sets, partial_sets, pair, best_shanten):
    index = find_earlist_nonzero_index(counts, index)
    if index >= len(Tile.ANY):
        current_shanten = 8 - (complete_sets * 2) - partial_sets - pair
        if current_shanten < best_shanten[0]:
            best_shanten[0] = current_shanten
        return

    if complete_sets + partial_sets < 4:
        if counts[index] == 2:
            modify_list(counts, [index], -2)
            _erase_partial_set(index, counts, complete_sets, partial_sets + 1, pair, best_shanten)
            modify_list(counts, [index], 2)

        if index in Tile.MAKE_EDGE_OR_SIDE and counts[index + 1] > 0:
            modify_list(counts, [index, index + 1], -1)
            _erase_partial_set(index, counts, complete_sets, partial_sets + 1, pair, best_shanten)
            modify_list(counts, [index, index + 1], 1)

        if index in Tile.MAKE_STRAIGHTS and counts[index + 2] > 0:
            modify_list(counts, [index, index + 2], -1)
            _erase_partial_set(index, counts, complete_sets, partial_sets + 1, pair, best_shanten)
            modify_list(counts, [index, index + 2], 1)

    _erase_partial_set(index + 1, counts, complete_sets, partial_sets, pair, best_shanten)


def _erase_complete_set(index: int, counts, complete_sets, pair, best_shanten):
    index = find_earlist_nonzero_index(counts, index)
    if index >= len(Tile.ANY):
        _erase_partial_set(0, counts, complete_sets, 0, pair, best_shanten)
        return

    if counts[index] >= 3:
        modify_list(counts, [index], -3)
        _erase_complete_set(index, counts, complete_sets + 1, pair, best_shanten)
        modify_list(counts, [index], 3)

    if index in Tile.MAKE_STRAIGHTS and counts[index + 1] > 0 and counts[index + 2] > 0:
        modify_list(counts, [index, index + 1, index + 2], -1)
        _erase_complete_set(index, counts, complete_sets + 1, pair, best_shanten)
        modify_list(counts, [index, index + 1, index + 2], 1)

    _erase_complete_set(index + 1, counts, complete_sets, pair, best_shanten)


def _calculate_normal_shanten(hand: Hand):
    concealed_counts = hand.concealed_counts[:]
    num_call = len(hand.call_counts)
    best_shanten = [8]

    for t in Tile.ANY:
        if concealed_counts[t] >= 2:
            modify_list(concealed_counts, [t], -2)
            _erase_complete_set(0, concealed_counts, num_call, 1, best_shanten)
            modify_list(concealed_counts, [t], 2)

    _erase_complete_set(0, concealed_counts, num_call, 0, best_shanten)

    return best_shanten[0]


def _calculate_seven_pairs_shanten(hand: Hand) -> int:
    if hand.is_opened:
        return 100

    concealed_counts = hand.concealed_counts
    num_excess = sum([x - 2 for x in concealed_counts if x > 2])
    num_single = len([x for x in concealed_counts if x == 1])

    return num_excess + ((num_single - num_excess - 1) // 2 if num_single > num_excess else 0)


def _calculate_thirteen_orphans_shanten(hand: Hand) -> int:
    if hand.is_opened:
        return 100

    concealed_counts = hand.concealed_counts
    terminals_and_honors = [t for t in Tile.TERMINALS_AND_HONORS if concealed_counts[t] > 0]
    num_terminals_and_honors = len(terminals_and_honors)
    has_terminals_and_honors_pairs = any(concealed_counts[t] >= 2 for t in terminals_and_honors)
    return 13 - num_terminals_and_honors - int(has_terminals_and_honors_pairs)
