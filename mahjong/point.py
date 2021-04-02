from mahjong.agari_hand import AgariHand
from mahjong.constants import Tile
from mahjong.divider import divide_hand
from mahjong.fu import calculate_fu
from mahjong.han import calculate_han
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule, RuleLoader


def calculate_base_point(fu: int, han: int, is_yakuman=False) -> int:
    """
    calculate point of give fu and han
    return four points which is child_tsumo, parent_tsumo, child_ron, parent_ron
    :param fu: int
    :param han: int
    :param is_yakuman: boolean
    :return: int
    """
    if han < 3 or (han == 3 and fu < 70) or (han == 4 and fu < 40):
        return fu * pow(2, 2 + han)
    elif han <= 5:
        return 2000
    elif han <= 7:
        return 3000
    elif han <= 10:
        return 4000
    elif han <= 12:
        return 6000
    else:
        return 8000 * (han // 13 if is_yakuman else 1)


def calculate_hand_point(agari_hand: AgariHand, hand_info: HandInfo, rule: Rule = None):
    if rule is None:
        rule = RuleLoader.load_rule()

    divisions = divide_hand(agari_hand)
    base_points = []
    for division in divisions:
        fu, fu_info = calculate_fu(division, hand_info, rule)
        han, han_info, is_yakuman = calculate_han(division, hand_info, rule)
        base_point = calculate_base_point(fu, han, is_yakuman)
        base_points.append((base_point, han, fu, han_info, fu_info))

    max_base_points = max(base_points)
    if hand_info.player_wind == Tile.EAST:
        if hand_info.is_tsumo_agari:
            point = (max_base_points[0] * 2 + 99) // 100 * 100
            point_string = str(point) + ' all'
        else:
            point = (max_base_points[0] * 6 + 99) // 100 * 100
            point_string = str(point)
    else:
        if hand_info.is_tsumo_agari:
            point1 = (max_base_points[0] + 99) // 100 * 100
            point2 = (max_base_points[0] * 2 + 99) // 100 * 100
            point_string = str(point1) + ', ' + str(point2)
        else:
            point = (max_base_points[0] * 4 + 99) // 100 * 100
            point_string = str(point)

    return point_string, *max_base_points[1:]
