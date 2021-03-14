def calculate_point(fu: int, han: int, is_yakuman=False) -> tuple[int, int, int, int]:
    """
    calculate point of give fu and han
    return four points which is child_tsumo, parent_tsumo, child_ron, parent_ron
    :param fu: int
    :param han: int
    :param is_yakuman: boolean
    :return: int, int, int, int
    """
    if han < 3 or (han == 3 and fu < 70) or (han == 4 and fu < 40):
        base = fu * pow(2, 2 + han)
    elif han <= 5:
        base = 2000
    elif han <= 7:
        base = 3000
    elif han <= 10:
        base = 4000
    elif han <= 12:
        base = 6000
    else:
        base = 8000 * (han // 13 if is_yakuman else 1)

    child_tsumo = (base + 99) // 100 * 100
    parent_tsumo = (2 * base + 99) // 100 * 100
    child_ron = (4 * base + 99) // 100 * 100
    parent_ron = (6 * base + 99) // 100 * 100

    return child_tsumo, parent_tsumo, child_ron, parent_ron
