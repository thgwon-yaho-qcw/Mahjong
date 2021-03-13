from mahjong.constants import HandType
from mahjong.convert import string_to_counts_and_call_counts, counts_to_string
from mahjong.error import TileDiscardError, TileDrawError
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

    def count_tile(self, tile):
        return self.concealed_counts[tile]

    def discard(self, tile):
        if self.concealed_counts[tile] == 0:
            raise TileDiscardError(self.string, tile)

        new_concealed_counts = self.concealed_counts[:]
        new_concealed_counts[tile] -= 1
        self.string = counts_to_string(new_concealed_counts)

    def draw(self, tile):
        if self.concealed_counts[tile] == 4:
            raise TileDrawError(self.string, tile)

        new_concealed_counts = self.concealed_counts[:]
        new_concealed_counts[tile] += 1
        self.string = counts_to_string(new_concealed_counts)

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
        tile_num = len(self.call_counts) * 3 + sum(self.concealed_counts)
        if tile_num == 14:
            return HandType.AFTER_DRAW
        elif tile_num == 13:
            return HandType.BEFORE_DRAW
        else:
            return HandType.INVALID
