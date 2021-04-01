from mahjong.constants import Tile, PartType
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Daisangen(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        if len(division.parts) != 5:
            return False

        dragons_part_count = 0
        for part in division.parts:
            if part.is_triple_or_quad and sum(part.counts[t] for t in Tile.DRAGONS) > 0:
                dragons_part_count += 1

        return dragons_part_count == 3
