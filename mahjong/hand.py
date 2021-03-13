from mahjong.convert import string_to_counts, string_to_counts_and_call_counts
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

    @property
    def counts(self):
        return string_to_counts_and_call_counts(self.string)

    @property
    def concealed_counts(self) -> list[list[int]]:
        return self.counts[0]

    @property
    def call_counts(self) -> list[list[int]]:
        return self.counts[1]
