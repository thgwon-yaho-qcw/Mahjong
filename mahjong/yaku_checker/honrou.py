from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Honrou(Yaku):
    def __init__(self):
        self.han_open = 2
        self.han_concealed = 2
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        honors_count = 0
        for part in division.parts:
            simples_count = sum(part.counts[t] for t in Tile.SIMPLES)
            honors_count += sum(part.counts[t] for t in Tile.HONORS)
            if simples_count > 0:
                return False
        return honors_count > 0

