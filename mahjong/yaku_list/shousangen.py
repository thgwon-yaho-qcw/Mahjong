from mahjong.constants import Tile, PartType
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_list.yaku import Yaku


class Shousangen(Yaku):
    def __init__(self):
        self.han_open = 2
        self.han_concealed = 2
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        if len(division.parts) != 5:
            return False

        dragons_part_count = 0
        for part in division.parts:
            if part.type == PartType.HEAD and sum(part.counts[t] for t in Tile.DRAGONS) == 0:
                return False

            if part.is_triple_or_quad and sum(part.counts[t] for t in Tile.DRAGONS) > 0:
                dragons_part_count += 1

        return dragons_part_count == 2

