from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_list.yaku import Yaku


class Chiihou(Yaku):
    def __init__(self):
        self.han_open = 13
        self.han_concealed = 13
        self.is_yakuman = True

    def is_satisfied(self, division: Division, hand_info: HandInfo, rule: Rule):
        return hand_info.is_first_turn and hand_info.player_wind != Tile.EAST and hand_info.is_tsumo_agari
