from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Ryuuiisou(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        non_greens = (t for t in Tile.ANY if t not in Tile.GREENS)
        for part in division.parts:
            non_greens_count = sum(part.counts[t] for t in non_greens)
            if non_greens_count > 0:
                return False
        return True
