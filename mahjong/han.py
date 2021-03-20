from mahjong.agari_hand import AgariHand
from mahjong.divider import Division, divide_hand
from mahjong.hand_info import HandInfo
from mahjong.yaku_list import *


def _get_yaku_list():
    # TODO get yaku list 다시 구현
    return [ReadyHand(), SelfPick(), AllSimples(), SevenPairs()], [ThirteenOrphans()]


def calculate_han(division: Division, hand_info: HandInfo):
    """
    calculate han
    :param division: Division obj
    :param hand_info: HandInfo obj
    :return: int, boolean
    """
    han = 0
    yaku_list, yakuman_list = _get_yaku_list()

    for yakuman in yakuman_list:
        if yakuman.is_satisfied(division, hand_info):
            han += yakuman.get_han(division.is_opened)

    if han > 0:
        return han, True

    for yaku in yaku_list:
        if yaku.is_satisfied(division, hand_info):
            han += yaku.get_han(division.is_opened)

    return han, False
