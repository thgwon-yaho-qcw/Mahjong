from mahjong.divider import Division
from mahjong.hand_info import HandInfo

from mahjong.yaku_list.chiitoi import Chiitoi
from mahjong.yaku_list.kokushi import Kokushi
from mahjong.yaku_list.riichi import Riichi
from mahjong.yaku_list.tanyao import Tanyao
from mahjong.yaku_list.tsumo import Tsumo


def _get_yaku_list():
    # TODO get yaku list 다시 구현
    return [Riichi(), Tsumo(), Tanyao(), Chiitoi()], [Kokushi()]


def calculate_han(division: Division, hand_info: HandInfo, rule):
    """
    calculate han
    :param division: Division obj
    :param hand_info: HandInfo obj
    :param rule: Rule obj
    :return: int, boolean
    """
    han = 0
    yaku_list, yakuman_list = _get_yaku_list()

    for yakuman in yakuman_list:
        if yakuman.is_satisfied(division, hand_info, rule):
            han += yakuman.get_han(division.is_opened)

    if han > 0:
        return han, True

    for yaku in yaku_list:
        if yaku.is_satisfied(division, hand_info, rule):
            han += yaku.get_han(division.is_opened)

    return han, False
