from mahjong.agari_hand import AgariHand
from mahjong.constants import Tile
from mahjong.divider import Division, divide_hand
from mahjong.hand_info import HandInfo
from mahjong.rule import RuleLoader

from mahjong.yaku_loader import YakuLoader


def calculate_han(division: Division, hand_info: HandInfo, rule):
    """
    calculate han
    :param division: Division obj
    :param hand_info: HandInfo obj
    :param rule: Rule obj
    :return: int, list of tuple(int, str), boolean
    """
    han = 0
    yaku_loader = YakuLoader(rule)
    yaku_list, yakuman_list = yaku_loader.yaku_list, yaku_loader.yakuman_list
    han_info = []
    for yakuman in yakuman_list:
        if yakuman.is_satisfied(division, hand_info):
            now_han = yakuman.get_han(division.is_opened)
            han += now_han
            han_info.append((now_han, yakuman.yaku_name))

    if han > 0:
        return han, han_info, True

    for yaku in yaku_list:
        if yaku.is_satisfied(division, hand_info):
            now_han = yaku.get_han(division.is_opened)
            han += now_han
            han_info.append((now_han, yaku.yaku_name))

    return han, han_info, False
