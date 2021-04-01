from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Junchan(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        for part in division.parts:
            terminals_count = sum(part.counts[t] for t in Tile.TERMINALS)
            if terminals_count == 0:
                return False

        return True
