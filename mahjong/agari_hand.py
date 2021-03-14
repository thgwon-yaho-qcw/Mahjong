from mahjong.agari import is_agari
from mahjong.hand import Hand
from mahjong.validator import Validator


class AgariHand(Hand):
    class AgariTileString(Validator):
        def validate(self, value):
            assert is_agari(Hand(value))

    string = AgariTileString()

    def __init__(self, string, agari_tile, is_tsumo_agari=True):
        self.string = string
        self.agari_tile = agari_tile
        self.is_tsumo_agari = is_tsumo_agari
