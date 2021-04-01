import itertools

from mahjong.constants import PartType, Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.util import find_earliest_nonzero_index
from mahjong.yaku_list.yaku import Yaku


class Ittsuu(Yaku):
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
            nums = sorted([num1, num2, num3])

            if nums in [[Tile.MAN1, Tile.MAN4, Tile.MAN7],
                        [Tile.PIN1, Tile.PIN4, Tile.PIN7],
                        [Tile.SOU1, Tile.SOU4, Tile.SOU7]]:
                return True
        return False
