from mahjong.agari_hand import AgariHand
from mahjong.constants import Tile, PartType
from mahjong.divider import Division, divide_hand
from mahjong.hand_info import HandInfo


def _calculate_part_fu(part, hand_info):
    if part.part_type == PartType.HEAD:
        value_head = [hand_info.player_wind, hand_info.round_wind] + Tile.DRAGONS
        return sum(2 for t in value_head if part.counts[t] == 2)

    if part.part_type == PartType.STRAIGHT:
        return 0

    is_terminals_and_honors_body = False
    for t in Tile.TERMINALS_AND_HONORS:
        is_terminals_and_honors_body |= (part.counts[t] > 0)
    return PartType.FU_DICT[part.part_type] * (2 if is_terminals_and_honors_body else 1)


def _calculate_waiting_fu(part, agari_tile):
    if part.part_type == PartType.HEAD:
        return 2

    if part.part_type != PartType.STRAIGHT:
        return 0

    if agari_tile in [Tile.MAN3, Tile.PIN3, Tile.SOU3] and \
            part.counts[agari_tile - 1] == 1 and part.counts[agari_tile - 2] == 1:
        return 2

    if agari_tile in [Tile.MAN7, Tile.PIN7, Tile.SOU7] and \
            part.counts[agari_tile - 1] == 1 and part.counts[agari_tile - 2] == 1:
        return 2

    if agari_tile in Tile.SIMPLES and part.counts[agari_tile - 1] == 1 and part.counts[agari_tile + 1] == 1:
        return 2

    return 0


def calculate_fu(division: Division, hand_info: HandInfo):
    if len(division.parts) == 7:
        return 25

    fu = 20
    for part in division.parts:
        fu += _calculate_part_fu(part, hand_info)

    waiting_part = division.parts[division.agari_tile_index]
    fu += _calculate_waiting_fu(waiting_part, division.agari_tile)

    if fu == 20 and not division.is_opened:
        return fu + (0 if hand_info.is_tsumo else 10)

    if hand_info.is_tsumo:
        fu += 2
    elif not division.is_opened:
        fu += 10

    return (fu + 9) // 10
