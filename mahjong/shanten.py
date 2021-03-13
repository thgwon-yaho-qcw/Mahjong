from mahjong.constants import Tile, HandType
from mahjong.error import TileCountError
from mahjong.hand import Hand


def calculate_shanten(hand: Hand, use_seven_pairs=True, use_thirteen_orphans=True) -> int:
    if hand.hand_type == HandType.INVALID:
        raise TileCountError(hand.string, HandType.BEFORE_DRAW)

    results = [_calculate_normal_shanten(hand)]
    if use_seven_pairs:
        results.append(_calculate_seven_pairs_shanten(hand))
    if use_thirteen_orphans:
        results.append(_calculate_thirteen_orphans_shanten(hand))

    return min(results)


def _calculate_normal_shanten(hand: Hand):
    best_shanten = 8
    concealed_counts = hand.concealed_counts[:]

    complete_sets = len(hand.call_counts)
    partial_sets = 0
    pair = 0

    def _erase_partial_set(index: int):
        nonlocal partial_sets
        nonlocal complete_sets
        nonlocal concealed_counts
        nonlocal best_shanten

        while index < len(Tile.ANY) and concealed_counts[index] == 0:
            index += 1

        if index >= len(Tile.ANY):
            current_shanten = 8 - (complete_sets * 2) - partial_sets - pair
            if current_shanten < best_shanten:
                best_shanten = current_shanten
            return

        if complete_sets + partial_sets < 4:
            if concealed_counts[index] == 2:
                partial_sets += 1
                concealed_counts[index] -= 2
                _erase_partial_set(index)
                concealed_counts[index] += 2
                partial_sets -= 1

            if index in Tile.MAKE_EDGE_OR_SIDE and concealed_counts[index + 1] > 0:
                partial_sets += 1
                concealed_counts[index] -= 1
                concealed_counts[index + 1] -= 1
                _erase_partial_set(index)
                concealed_counts[index + 1] += 1
                concealed_counts[index] += 1
                partial_sets -= 1

            if index in Tile.MAKE_STRAIGHTS and concealed_counts[index + 2] > 0:
                partial_sets += 1
                concealed_counts[index] -= 1
                concealed_counts[index + 2] -= 1
                _erase_partial_set(index)
                concealed_counts[index + 2] += 1
                concealed_counts[index] += 1
                partial_sets -= 1

        _erase_partial_set(index + 1)

    def _erase_complete_set(index: int):
        nonlocal complete_sets
        nonlocal concealed_counts

        while index < len(Tile.ANY) and concealed_counts[index] == 0:
            index += 1

        if index >= len(Tile.ANY):
            _erase_partial_set(0)
            return

        if concealed_counts[index] >= 3:
            complete_sets += 1
            concealed_counts[index] -= 3
            _erase_complete_set(index)
            concealed_counts[index] += 3
            complete_sets -= 1

        if index in Tile.MAKE_STRAIGHTS and concealed_counts[index + 1] > 0 and concealed_counts[index + 2] > 0:
            complete_sets += 1
            concealed_counts[index] -= 1
            concealed_counts[index + 1] -= 1
            concealed_counts[index + 2] -= 1
            _erase_complete_set(index)
            concealed_counts[index] += 1
            concealed_counts[index + 1] += 1
            concealed_counts[index + 2] += 1
            complete_sets -= 1

        _erase_complete_set(index + 1)

    for t in Tile.ANY:
        if concealed_counts[t] >= 2:
            pair += 1
            concealed_counts[t] -= 2
            _erase_complete_set(0)
            concealed_counts[t] += 2
            pair -= 1

    _erase_complete_set(0)

    return best_shanten


def _calculate_seven_pairs_shanten(hand: Hand) -> int:
    if hand.is_called:
        return 100

    concealed_counts = hand.concealed_counts
    num_excess = sum([x - 2 for x in concealed_counts if x > 2])
    num_single = len([x for x in concealed_counts if x == 1])

    return num_excess + ((num_single - num_excess - 1) // 2 if num_single > num_excess else 0)


def _calculate_thirteen_orphans_shanten(hand: Hand) -> int:
    if hand.is_called:
        return 100

    has_terminals_and_honors_pair = False
    num_terminals_and_honors = 0
    concealed_counts = hand.concealed_counts

    for t in Tile.TERMINALS_AND_HONORS:
        if concealed_counts[t] >= 1:
            num_terminals_and_honors += 1
            if concealed_counts[t] >= 2:
                has_terminals_and_honors_pair = True

    return 13 - num_terminals_and_honors - int(has_terminals_and_honors_pair)
