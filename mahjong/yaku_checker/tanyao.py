from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule, RuleLoader
from mahjong.yaku_checker.yaku import Yaku


class Tanyao(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        terminals_and_honors_count = 0
        for part in division.parts:
            terminals_and_honors_count += sum(part.counts[t] for t in Tile.TERMINALS_AND_HONORS)

        if terminals_and_honors_count != 0:
            return False

        return self.rule.has_opened_tanyao or not division.is_opened
