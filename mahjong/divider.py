from mahjong.constants import PartType, CALL_TYPE_TO_PART_TYPE
from mahjong.agari_hand import AgariHand
from mahjong.agari import *
from mahjong.convert import counts_to_string


class Division:
    class Part:
        def __init__(self, type_, counts):
            self.type = type_
            self.counts = counts

        def __str__(self):
            return '{} type : {}'.format(self.type, self.counts)

        def __repr__(self):
            return self.__str__()

        def __eq__(self, other):
            if not isinstance(other, Division.Part):
                return False
            return self.type == other.type and self.counts == other.counts

        @property
        def is_triple(self):
            return self.type in [PartType.CONCEALED_TRIPLE, PartType.OPENED_TRIPLE]

        @property
        def is_quad(self):
            return self.type in [PartType.CONCEALED_QUAD, PartType.OPENED_QUAD]

        @property
        def is_triple_or_quad(self):
            return self.is_triple or self.is_quad

    def __init__(self, divs, agari_tile_index, agari_tile, is_opened=False):
        self.parts = [self.Part(part_type, counts) for (part_type, counts) in divs]
        self.agari_tile_index = agari_tile_index
        self.agari_tile = agari_tile
        self.is_opened = is_opened


def _divide_bodies(index, counts, normal_parts_list, parts):
    index = find_earliest_nonzero_index(counts, index)
    if index >= len(Tile.ANY):
        normal_parts_list.append(parts[:])
        return

    if counts[index] >= 3:
        modify_list(counts, [index], -3)
        parts.append((PartType.CONCEALED_TRIPLE, [(3 if index == t else 0) for t in Tile.ANY]))
        _divide_bodies(index, counts, normal_parts_list, parts)
        parts.pop()
        modify_list(counts, [index], 3)

    if index in Tile.MAKE_STRAIGHTS and counts[index + 1] >= 1 and counts[index + 2] >= 1:
        modify_list(counts, [index, index + 1, index + 2], -1)
        parts.append(
            (PartType.STRAIGHT, [(1 if t in [index, index + 1, index + 2] else 0) for t in Tile.ANY]))
        _divide_bodies(index, counts, normal_parts_list, parts)
        parts.pop()
        modify_list(counts, [index, index + 1, index + 2], 1)


def _calculate_concealed_parts_list(counts):
    normal_parts_list = []
    head_type = Tile.Type.HONORS
    for t in Tile.Type.ANY:
        type_count = sum([counts[tile] for tile in Tile.TYPE_DICT[t]])
        if type_count % 3 == 2:
            head_type = t

    head_candidates = []
    empty_honor = [t for t in Tile.HONORS if counts[t] == 0][-1]

    modify_list(counts, [empty_honor], 2)
    for candidate in [t for t in Tile.TYPE_DICT[head_type] if counts[t] >= 2 and t != empty_honor]:
        modify_list(counts, [candidate], -2)
        if is_normal_agari(Hand(counts_to_string(counts))):
            head_candidates.append(candidate)
        modify_list(counts, [candidate], 2)
    modify_list(counts, [empty_honor], -2)

    for head in head_candidates:
        modify_list(counts, [head], -2)
        parts = [(PartType.HEAD, [(2 if head == t else 0) for t in Tile.ANY])]
        _divide_bodies(0, counts, normal_parts_list, parts)
        modify_list(counts, [head], 2)

    return normal_parts_list


def _calculate_thirteen_orphans_divisions(hand: AgariHand):
    if is_thirteen_orphan_agari(hand):
        return [Division([(PartType.THIRTEEN_ORPHANS, hand.concealed_counts)], 0, hand.agari_tile)]
    return []


def _calculate_seven_pairs_divisions(hand: AgariHand):
    if not is_seven_pairs_agari(hand):
        return []

    divisions = []
    parts = []
    concealed_counts = hand.concealed_counts
    agari_tile_index = 0

    for head in Tile.ANY:
        if concealed_counts[head] != 2:
            continue

        now_counts = [(2 if head == t else 0) for t in Tile.ANY]
        if hand.agari_tile == head:
            agari_tile_index = len(parts)
        parts.append((PartType.HEAD, now_counts))

    divisions.append(Division(parts, agari_tile_index, hand.agari_tile))
    return divisions


def _calculate_normal_divisions(hand: AgariHand):
    if not is_normal_agari(hand):
        return []

    divisions = []
    concealed_counts = hand.concealed_counts[:]
    concealed_parts_list = _calculate_concealed_parts_list(concealed_counts)
    call_parts = list(map(lambda x: (CALL_TYPE_TO_PART_TYPE[x[0]], x[1]), hand.calls))

    for concealed_parts in concealed_parts_list:
        for ind, concealed_part in enumerate(concealed_parts):
            if concealed_part[1][hand.agari_tile] == 0:
                continue

            is_final_tile_open_triple = concealed_part[0] == PartType.CONCEALED_TRIPLE and not hand.is_tsumo_agari
            if is_final_tile_open_triple:
                concealed_parts[ind] = (PartType.OPENED_TRIPLE, concealed_parts[ind][1])
            divisions.append(Division(concealed_parts + call_parts, ind, hand.agari_tile, hand.is_opened))
            if is_final_tile_open_triple:
                concealed_parts[ind] = (PartType.CONCEALED_TRIPLE, concealed_parts[ind][1])

    return divisions


def divide_hand(hand: AgariHand):
    """
    divide hand into each bodies to calculate han and fu.
    returns list of division
    :param hand: agari hand obj
    :return: list of division objs
    """

    normal_divisions = _calculate_normal_divisions(hand)
    thirteen_orphans_divisions = _calculate_thirteen_orphans_divisions(hand)
    seven_pairs_divisions = _calculate_seven_pairs_divisions(hand)

    return normal_divisions + thirteen_orphans_divisions + seven_pairs_divisions
