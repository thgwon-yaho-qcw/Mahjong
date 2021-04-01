from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.yaku_checker.yaku import Yaku


class PlayerWind(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        for part in division.parts:
            if part.is_triple_or_quad and part.counts[hand_info.player_wind] >= 3:
                return True
        return False
