from mahjong.agari_hand import AgariHand
from mahjong.divider import divide_hand
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.shanten import *
import pytest

from mahjong.yaku_list.chinrotou import Chinrotou
from mahjong.yaku_list.daisangen import Daisangen
from mahjong.yaku_list.daisuushii import Daisuushii
from mahjong.yaku_list.shousuushii import Shousuushii
from mahjong.yaku_list.suuankou import Suuankou
from mahjong.yaku_list.suukantsu import Suukantsu
from mahjong.yaku_list.tsuuiisou import Tsuuiisou


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22244466678889m', Tile.MAN2, False),
    ('22244466688899m', Tile.MAN2, True),
    ('22444666888999m', Tile.MAN2, True),
 ])
def test_suuankou_tsumo(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Suuankou().is_satisfied(division, HandInfo(is_tsumo=True), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22244466678889m', Tile.MAN2, False),
    ('22244466688899m', Tile.MAN2, False),
    ('22444666888999m', Tile.MAN2, True),
 ])
def test_suuankou_ron(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Suuankou().is_satisfied(division, HandInfo(is_tsumo=False), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('12399m555666777z', Tile.MAN2, True),
    ('22m888s,pon555z,cnk6666z,bmk7777z', Tile.MAN2, True),
    ('11223399m556677z', Tile.MAN2, False),
 ])
def test_daisangen(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Daisangen().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('123m11222333444z', Tile.MAN2, True),
    ('222m11z,pon222z,cnk3333z,bmk4444z', Tile.MAN2, True),
    ('22m111z,pon222z,cnk3333z,bmk4444z', Tile.MAN2, False),
    ('112233m11223344z', Tile.MAN2, False),
 ])
def test_shousuushii(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Shousuushii().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('123m11222333444z', Tile.MAN2, False),
    ('222m11z,pon222z,cnk3333z,bmk4444z', Tile.MAN2, False),
    ('22m111z,pon222z,cnk3333z,bmk4444z', Tile.MAN2, True),
    ('112233m11223344z', Tile.MAN2, False),
 ])
def test_daisuushii(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Daisuushii().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('11222333444555z', Tile.EAST, True),
    ('11z,pon222z,cnk6666z,bmk4444z,pon777z', Tile.EAST, True),
    ('11133355z,pon222z,bmk4444z', Tile.HAKU, True),
    ('11223344556677z', Tile.HATSU, True),
 ])
def test_tsuuiisou(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Tsuuiisou().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('111999p111999s11m', Tile.MAN1, True),
    ('11m,pon999p,cnk1111s,bmk9999s,pon111p', Tile.MAN1, True),
    ('1199m1199p1199s11z', Tile.MAN1, False)
 ])
def test_chinrotou(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Chinrotou().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('11m,cnk2222p,bmk3333s,cnk4444m,smk5555z', Tile.MAN1, True),
])
def test_suukantsu(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Suukantsu().is_satisfied(division, HandInfo(), Rule())
    assert result == expected
