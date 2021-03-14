from mahjong.constants import Tile, PartType, CALL_TYPE_TO_PART_TYPE
from mahjong.agari_hand import AgariHand
from mahjong.agari import *
from mahjong.convert import counts_to_string


class Finger:
    class Part:
        def __init__(self, part_type, counts):
            self.part_type = part_type
            self.counts = counts

        def __str__(self):
            return '{} type : {}'.format(self.part_type, self.counts)

        def __repr__(self):
            return self.__str__()

    def __init__(self, divs, agari_tile_index):
        self.parts = [self.Part(part_type, counts) for (part_type, counts) in divs]
        self.agari_tile_index = agari_tile_index


def divide_hand(hand: AgariHand):
    """
    divide hand into each bodies to calculate han and fu.
    returns list of division
    :param hand: agari hand obj
    :return: list of division objs
    """

    concealed_counts = hand.concealed_counts[:]
    call_parts = list(map(lambda x: (CALL_TYPE_TO_PART_TYPE[x[0]], x[1]), hand.calls))
    divisions = []

    def _calculate_normal_divisions(counts):
        normal_parts_list = []
        head_type = Tile.Type.HONORS
        for t in Tile.Type.ANY:
            type_count = sum([counts[tile] for tile in Tile.TYPE_DICT[t]])
            if type_count % 3 == 2:
                head_type = t

        head_candidates = []
        empty_honor = [t for t in Tile.HONORS if counts[t] == 0][-1]
        counts[empty_honor] += 2
        for candidate in [t for t in Tile.TYPE_DICT[head_type] if counts[t] >= 2 and t != empty_honor]:
            counts[candidate] -= 2
            if is_normal_agari(Hand(counts_to_string(counts))):
                head_candidates.append(candidate)
            counts[candidate] += 2
        counts[empty_honor] -= 2

        for head in head_candidates:
            counts[head] -= 2
            parts = [(PartType.HEAD, [(2 if head == t else 0) for t in Tile.ANY])]

            def _divide_bodies(index: int):
                nonlocal head
                nonlocal counts
                nonlocal normal_parts_list
                while index < len(Tile.ANY) and counts[index] == 0:
                    index += 1
                if index >= len(Tile.ANY):
                    normal_parts_list.append(parts[:])
                    return

                if counts[index] >= 3:
                    counts[index] -= 3
                    parts.append((PartType.CONCEALED_TRIPLE, [(3 if index == t else 0) for t in Tile.ANY]))
                    _divide_bodies(index)
                    parts.pop()
                    counts[index] += 3

                if index in Tile.MAKE_STRAIGHTS and counts[index + 1] >= 1 and counts[index + 2] >= 1:
                    counts[index] -= 1
                    counts[index + 1] -= 1
                    counts[index + 2] -= 1
                    parts.append(
                        (PartType.STRAIGHT, [(1 if t in [index, index + 1, index + 2] else 0) for t in Tile.ANY]))
                    _divide_bodies(index)
                    parts.pop()
                    counts[index] += 1
                    counts[index + 1] += 1
                    counts[index + 2] += 1

            _divide_bodies(0)
            counts[head] += 2

        return normal_parts_list

    if is_normal_agari(hand):
        concealed_divisions = _calculate_normal_divisions(concealed_counts)

        for concealed_parts in concealed_divisions:
            for ind, concealed_part in enumerate([cp for cp in concealed_parts if cp[1][hand.agari_tile] > 0]):
                is_final_tile_open_triple = concealed_part[0] == PartType.CONCEALED_TRIPLE and not hand.is_tsumo_agari

                if is_final_tile_open_triple:
                    concealed_parts[ind] = (PartType.OPENED_TRIPLE, concealed_parts[ind][1])

                divisions.append(Finger(concealed_parts + call_parts, ind))

                if is_final_tile_open_triple:
                    concealed_parts[ind] = (PartType.CONCEALED_TRIPLE, concealed_parts[ind][1])

    if is_thirteen_orphan_agari(hand):
        divisions.append(Finger([(PartType.THIRTEEN_ORPHANS, concealed_counts)], 0))

    head_indices = [t for t in Tile.ANY if concealed_counts[t] == 2]
    if is_seven_pairs_agari(hand):
        parts = []
        agari_tile_index = 0
        for head_index in head_indices:
            now_counts = [(2 if head_index == t else 0) for t in Tile.ANY]
            if hand.agari_tile == head_index:
                agari_tile_index = len(parts)
            parts.append((PartType.HEAD, now_counts))

        divisions.append(Finger(parts, agari_tile_index))

    return divisions
