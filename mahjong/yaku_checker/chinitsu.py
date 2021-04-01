from mahjong.constants import Tile
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.yaku_checker.yaku import Yaku


class Chinitsu(Yaku):
    def is_satisfied(self, division: Division, hand_info: HandInfo):
        mans_count = 0
        pins_count = 0
        sous_count = 0

        for part in division.parts:
            mans_count += sum(part.counts[t] for t in Tile.MANS)
            sous_count += sum(part.counts[t] for t in Tile.SOUS)
            pins_count += sum(part.counts[t] for t in Tile.PINS)
            honors_count = sum(part.counts[t] for t in Tile.HONORS)

            if honors_count > 0:
                return False

        max_count = max(mans_count, sous_count, pins_count)
        return mans_count + sous_count + pins_count == max_count
