from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_list.yaku import Yaku


class AllSimples(Yaku):
    def __init__(self):
        self.han_open = 1
        self.han_concealed = 1
        self.is_yakuman = False

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        terminals_and_honors_count = 0
        for part in division.parts:
            terminals_and_honors_count += sum(part.counts[t] for t in Tile.TERMINALS_AND_HONORS)

        if terminals_and_honors_count != 0:
            return False

        return rule.has_opened_all_simple or not division.is_opened
