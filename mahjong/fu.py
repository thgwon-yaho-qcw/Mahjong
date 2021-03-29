from mahjong.constants import Tile, PartType, FuReason
from mahjong.divider import Division
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule


def _calculate_part_fu(part, hand_info):
    if part.type == PartType.HEAD:
        head = [index for index, val in enumerate(part.counts) if val != 0][0]
        if head == hand_info.player_wind and head == hand_info.round_wind:
            return FuReason.DOUBLE_WIND_PAIR
        if head in [hand_info.player_wind, hand_info.round_wind] + Tile.DRAGONS:
            return FuReason.VALUE_PAIR
        return None

    if part.type == PartType.STRAIGHT:
        return None

    is_terminals_and_honors_body = False
    for t in Tile.TERMINALS_AND_HONORS:
        is_terminals_and_honors_body |= (part.counts[t] > 0)

    fu_dict = {PartType.OPENED_TRIPLE: [FuReason.OPENED_NORMAL_TRIPLE, FuReason.OPENED_OUTSIDE_TRIPLE],
               PartType.CONCEALED_TRIPLE: [FuReason.CONCEALED_NORMAL_TRIPLE, FuReason.CONCEALED_OUTSIDE_TRIPLE],
               PartType.OPENED_QUAD: [FuReason.OPENED_NORMAL_QUAD, FuReason.OPENED_OUTSIDE_QUAD],
               PartType.CONCEALED_QUAD: [FuReason.CONCEALED_NORMAL_QUAD, FuReason.CONCEALED_OUTSIDE_QUAD],
               }

    return fu_dict[part.type][is_terminals_and_honors_body]


def _calculate_waiting_fu(part, agari_tile):
    if part.type == PartType.HEAD:
        return FuReason.HEAD_WAIT

    if part.type != PartType.STRAIGHT:
        return None

    if agari_tile in [Tile.MAN3, Tile.PIN3, Tile.SOU3] and \
            part.counts[agari_tile - 1] == 1 and part.counts[agari_tile - 2] == 1:
        return FuReason.EDGE_WAIT

    if agari_tile in [Tile.MAN7, Tile.PIN7, Tile.SOU7] and \
            part.counts[agari_tile - 1] == 1 and part.counts[agari_tile - 2] == 1:
        return FuReason.EDGE_WAIT

    if agari_tile in Tile.SIMPLES and part.counts[agari_tile - 1] == 1 and part.counts[agari_tile + 1] == 1:
        return FuReason.CLOSED_WAIT

    return None


def calculate_fu(division: Division, hand_info: HandInfo, rule: Rule):
    """
    calculate fu
    :param division: Division obj
    :param hand_info: HandInfo obj
    :param rule: Rule obj
    :return: int
    """

    if len(division.parts) == 7:
        return 25, [FuReason.SEVEN_PAIRS]

    fu_infos = [FuReason.BASE]
    for part in division.parts:
        part_fu = _calculate_part_fu(part, hand_info)
        if part_fu:
            fu_infos.append(part_fu)

    waiting_part = division.parts[division.agari_tile_index]
    waiting_fu = _calculate_waiting_fu(waiting_part, division.agari_tile)
    if waiting_fu:
        fu_infos.append(waiting_fu)

    if len(fu_infos) == 1 and not division.is_opened:
        if not hand_info.is_tsumo:
            fu_infos.append(FuReason.CONCEALED_RON)
    elif hand_info.is_tsumo:
        fu_infos.append(FuReason.TSUMO)
    elif not division.is_opened:
        fu_infos.append(FuReason.CONCEALED_RON)

    fu = sum([fu_info[0] for fu_info in fu_infos])
    return (fu + 9) // 10 * 10, fu_infos
