from mahjong.agari_hand import AgariHand
from mahjong.divider import divide_hand
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.shanten import *
import pytest


from mahjong.yaku_list.iipeikou import Iipeikou
from mahjong.yaku_list.ittsuu import Ittsuu
from mahjong.yaku_list.ryanpeikou import Ryanpeikou
from mahjong.yaku_list.sanshoku import Sanshoku
from mahjong.yaku_list.tanyao import Tanyao

# TODO: 핑후 TC 작성


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('234m445566p67888s', Tile.MAN2, True),
    ('666777888m678p77s', Tile.MAN6, True),
    ('123m456p22345678s', Tile.MAN2, False),
    ('22333m444p555s666z', Tile.MAN2, False),
])
def test_tanyao(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Tanyao().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('234m445566p67888s', Tile.MAN2, True),
    ('666777888m678p77s', Tile.MAN6, True),
    ('123m456p22345678s', Tile.MAN2, False),
    ('22333m444p555s666z', Tile.MAN2, False),
])
def test_iipeikou(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Iipeikou().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('223344m445566p88s', Tile.MAN2, True),
    ('666677778888m77s', Tile.MAN6, True),
    ('123m456p22345678s', Tile.MAN2, False),
    ('22333m444p555s666z', Tile.MAN2, False),
])
def test_ryanpeikou(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Ryanpeikou().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('234m234567p23488s', Tile.MAN2, True),
    ('234m567p23488s,chi234p', Tile.MAN2, True),
    ('111123s123p12399m', Tile.MAN2, True),
    ('234m123456p234s11z', Tile.MAN2, False),
    ('22333m444p555s666z', Tile.MAN2, False),
])
def test_sanshoku(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Sanshoku().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('123456789m45688s', Tile.MAN2, True),
    ('123789p22299m,chi456p', Tile.MAN2, True),
    ('11112345678999m', Tile.MAN2, True),
    ('11123455678999m', Tile.MAN2, False),
    ('123345567789m11z', Tile.MAN2, False),
])
def test_ittsuu(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Ittsuu().is_satisfied(division, HandInfo(), Rule())
    assert result == expected

