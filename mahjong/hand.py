from mahjong.constants import HandType
from mahjong.convert import string_to_counts, string_to_counts_and_call_counts
from mahjong.validator import Validator


class Hand:
    class TileString(Validator):
        def validate(self, value):
            string_to_counts_and_call_counts(value)

    string = TileString()

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    @property
    def counts(self) -> tuple[list[int], list[list[int]]]:
        return string_to_counts_and_call_counts(self.string)

    @property
    def concealed_counts(self) -> list[int]:
        return self.counts[0]

    @property
    def call_counts(self) -> list[list[int]]:
        return self.counts[1]

    @property
    def is_called(self):
        return len(self.call_counts) > 0

    @property
    def hand_type(self):
        if len(self.call_counts) * 3 + sum(self.concealed_counts) == 14:
            return HandType.AFTER_DRAW
        elif len(self.format_34[1]) * 3 + sum(self.format_34[0]) == 13:
            return HandType.BEFORE_DRAW
        else:
            return HandType.INVALID
