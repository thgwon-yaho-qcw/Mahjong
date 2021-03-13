import pytest
from mahjong.agari import *


@pytest.mark.parametrize("test_input, expected", [
    ('19m19s19p12344567z', True),
    ('19m19s119p1234567z', True),
    ('225566m4466p44s44z', True),
    ('11223344556677z', True),
    ('23344577m444p111z', True),
    ('123456789m11133z', True),
    ('123456789m11133z', True),
    ('11122233344455z', True),
    ('12222355567789p', True),
    ('22223333444455p', True),
    ('19m1p19s123344567z', False),
    ('19m19p18s12334567z', False),
    ('226666m4466p44s44z', False),
    ('23456789m1s11133z', False),
    ('12234455677999m', False),
    ('123456789m44567z', False),
    ('123m456s77z,chi123s,chi123p', True),
    ('22z,chi123s,chi456m,chi789p,pon555z', True),
    ('122334m99p,cnk1111z,bmk5555p', True),
    ('123m457s77z,chi123s,chi123p', False),
    ('23z,chi123s,chi456m,chi789p,pon555z', False),
])
def test_is_agari(test_input, expected):
    assert is_agari(Hand(test_input)) == expected
