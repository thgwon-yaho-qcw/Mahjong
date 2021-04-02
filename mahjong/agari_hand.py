from mahjong.agari import is_agari
from mahjong.convert import string_to_counts_and_call_counts
from mahjong.hand import Hand
from mahjong.validator import Validator


class AgariHand(Hand):
    class AgariTileString(Validator):
        def validate(self, value):
            assert is_agari(Hand(value))

    string = AgariTileString()

    def __init__(self, string, agari_tile):
        self.string = string
        self.agari_tile = agari_tile
