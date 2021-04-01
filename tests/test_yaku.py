from mahjong.agari_hand import AgariHand
from mahjong.divider import divide_hand
from mahjong.hand_info import HandInfo
from mahjong.rule import Rule
from mahjong.shanten import *
import pytest

from mahjong.yaku_list.chun import Chun
from mahjong.yaku_list.haku import Haku
from mahjong.yaku_list.hatsu import Hatsu
from mahjong.yaku_list.iipeikou import Iipeikou
from mahjong.yaku_list.ittsuu import Ittsuu
from mahjong.yaku_list.pinfu import Pinfu
from mahjong.yaku_list.ryanpeikou import Ryanpeikou
from mahjong.yaku_list.sanankou import Sanankou
from mahjong.yaku_list.sankantsu import Sankantsu
from mahjong.yaku_list.sanshoku import Sanshoku
from mahjong.yaku_list.sanshoku_doukou import SanshokuDoukou
from mahjong.yaku_list.tanyao import Tanyao
from mahjong.yaku_list.toitoi import Toitoi


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('234m445566p67888s', Tile.MAN2, True),
    ('666777888m678p77s', Tile.MAN6, True),
    ('123m456p22345678s', Tile.MAN2, False),
    ('22333m444p555s666z', Tile.MAN2, False),
])
def test_pinfu(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Pinfu().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


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


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22244466688899m', Tile.MAN2, True),
    ('22m,pon333p,bmk5555p,cnk1111z,smk3333z', Tile.MAN2, True),
    ('22223333444455m', Tile.MAN2, False),
    ('22334455m111z,chi234m', Tile.MAN2, False),
 ])
def test_toitoi(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Toitoi().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22244466678889m', Tile.MAN2, True),
    ('22m111444p789s,cnk2222z', Tile.MAN2, True),
    ('222m444666p88s,chi123p', Tile.MAN2, True),
    ('22244466688899m', Tile.MAN2, False),
 ])
def test_sanankou_tsumo(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Sanankou().is_satisfied(division, HandInfo(is_tsumo=True), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22244466678889m', Tile.MAN2, False),
    ('22m111444p789s,cnk2222z', Tile.MAN2, True),
    ('222m444666p88s,chi123p', Tile.MAN2, False),
    ('22244466688899m', Tile.MAN2, True),
 ])
def test_sanankou_ron(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile, is_tsumo_agari=False)):
        result |= Sanankou().is_satisfied(division, HandInfo(is_tsumo=False), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('222m222p22278999s', Tile.MAN2, True),
    ('222m11z,cnk2222p,pon222s,chi123s', Tile.MAN2, True),
    ('22234m222p222333s', Tile.MAN2, False),
    ('222m222p333s22233z', Tile.MAN2, False),
])
def test_sanshoku_doukou(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= SanshokuDoukou().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22m,cnk1111z,cnk2222z,cnk3333z,chi789s', Tile.MAN2, True),
    ('222m11z,cnk2222p,bmk2222s,smk2222z', Tile.MAN2, True),
    ('22m,cnk1111p,smk2222p,cnk3333p,bmk4444p', Tile.MAN2, False),
    ('22223488m,smk1111z,smk2222z', Tile.MAN2, False),
])
def test_sankantsu(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Sankantsu().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22m,cnk1111m,chi123p,cnk5555z,chi789s', Tile.MAN2, True),
    ('222m456789s88p555z', Tile.MAN2, True),
])
def test_haku(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Haku().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22m,cnk1111m,chi123p,cnk6666z,chi789s', Tile.MAN2, True),
    ('222m456789s88p666z', Tile.MAN2, True),
])
def test_hatsu(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Hatsu().is_satisfied(division, HandInfo(), Rule())
    assert result == expected


@pytest.mark.parametrize('test_input, agari_tile, expected', [
    ('22m,cnk1111m,chi123p,cnk7777z,chi789s', Tile.MAN2, True),
    ('222m456789s88p777z', Tile.MAN2, True),
])
def test_chun(test_input, agari_tile, expected):
    result = False
    for division in divide_hand(AgariHand(test_input, agari_tile)):
        result |= Chun().is_satisfied(division, HandInfo(), Rule())
    assert result == expected
