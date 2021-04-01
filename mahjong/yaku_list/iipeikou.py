import itertools

from mahjong.constants import PartType
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_list.yaku import Yaku


class Iipeikou(Yaku):
    def __init__(self):
        self.han_open = 0
        self.han_closed = 1
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule):
        same_straight_count = 0
        for part1, part2 in tuple(itertools.combinations(division.parts, 2)):
            if part1 == part2 and part1.type == PartType.STRAIGHT:
                same_straight_count += 1

        return same_straight_count == 1 or same_straight_count == 3
