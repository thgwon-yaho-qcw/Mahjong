from mahjong.convert import string_to_counts
from mahjong.validator import Validator


class Hand:
    class TileString(Validator):
        def validate(self, value):
            string_to_counts(value)

    string = TileString()

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
