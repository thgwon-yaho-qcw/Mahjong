import itertools

from mahjong.constants import PartType
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.util import find_earliest_nonzero_index
from mahjong.yaku_list.yaku import Yaku


class Sanshoku(Yaku):
    def __init__(self):
        self.han_open = 1
        self.han_closed = 2
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule):
        for part1, part2, part3 in tuple(itertools.combinations(division.parts, 3)):
            if not (part1.type == part2.type == part3.type == PartType.STRAIGHT):
                continue
            num1 = find_earliest_nonzero_index(part1.counts)
            num2 = find_earliest_nonzero_index(part2.counts)
            num3 = find_earliest_nonzero_index(part3.counts)

            if num1 % 9 == num2 % 9 == num3 % 9 and num1 != num2 and num2 != num3 and num3 != num1:
                return True

        return False
