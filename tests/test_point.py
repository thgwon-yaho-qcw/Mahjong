import pytest
from mahjong.point import *


@pytest.mark.parametrize('fu, han, expected', [
    (30, 4, (2000, 3900, 7700, 11600)),
    (70, 1, (600, 1200, 2300, 3400)),
    (110, 2, (1800, 3600, 7100, 10600)),
    (25, 4, (1600, 3200, 6400, 9600)),
    (25, 6, (3000, 6000, 12000, 18000)),
    (40, 5, (2000, 4000, 8000, 12000)),
    (70, 9, (4000, 8000, 16000, 24000)),
    (80, 11, (6000, 12000, 24000, 36000)),
])
def test_calculate_point(fu, han, expected):
    assert calculate_point(fu, han) == expected


@pytest.mark.parametrize('fu, han, expected', [
    (30, 13, (8000, 16000, 32000, 48000)),
    (30, 26, (16000, 32000, 64000, 96000)),
    (30, 39, (24000, 48000, 96000, 144000)),
    (30, 52, (32000, 64000, 128000, 192000)),
    (30, 65, (40000, 80000, 160000, 240000)),
    (30, 78, (48000, 96000, 192000, 288000)),
])
def test_calculate_point_yakuman(fu, han, expected):
    assert calculate_point(fu, han, is_yakuman=True) == expected
