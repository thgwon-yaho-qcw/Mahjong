from mahjong.shanten import *
import pytest


@pytest.mark.parametrize('test_input, expected', [
    ('123m456p789s1112z', 0),
    ('123m456p789s11122z', -1),
    ('135m466p479s1122z', 3),
    ('334m33889p1457s4z', 3),
    ('3558m4p25668s345z', 4),
    ('1199m4p1147s13457z', 3),
    ('1199m1199s1199p12z', 0),
    ('19m149s18p1223456z', 1),
])
def test_calculate_shanten(test_input, expected):
    assert calculate_shanten(Hand(test_input)) == expected


@pytest.mark.parametrize('test_input, expected', [
    ('1199m4p1147s13457z', 5),
    ('135m466p479s1122z', 3),
    ('334m33889p1457s4z', 4),
    ('3558m4p25668s345z', 5),
    ('1199m1199s1199p12z', 3),
    ('1199m1199s1199p12z', 3),
    ('19m149s18p1223456z', 7),
])
def test_calculate_shanten_normal(test_input, expected):
    assert calculate_shanten(Hand(test_input), False, False) == expected
