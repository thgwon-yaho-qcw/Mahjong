from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Chanta(Yaku):
    def __init__(self):
        self.han_open = 1
        self.han_concealed = 2
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        honors_count = 0
        for part in division.parts:
            terminals_and_honors_count = sum(part.counts[t] for t in Tile.TERMINALS_AND_HONORS)
            honors_count += sum(part.counts[t] for t in Tile.HONORS)
            if terminals_and_honors_count == 0:
                return False

        return honors_count > 0
