from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Honrou(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        honors_count = 0
        for part in division.parts:
            simples_count = sum(part.counts[t] for t in Tile.SIMPLES)
            honors_count += sum(part.counts[t] for t in Tile.HONORS)
            if simples_count > 0:
                return False
        return honors_count > 0

