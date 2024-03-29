class Tile:
    class Type:
        MANS = 'm'
        PINS = 'p'
        SOUS = 's'
        HONORS = 'z'
        ANY = [MANS, PINS, SOUS, HONORS]
        OFFSET = {MANS: -1, PINS: 8, SOUS: 17, HONORS: 26}

    RE_STRING = '([1-9]+)([' + Type.MANS + Type.PINS + Type.SOUS + Type.HONORS + '])'

    MAN1, MAN2, MAN3, MAN4, MAN5, MAN6, MAN7, MAN8, MAN9 = 0, 1, 2, 3, 4, 5, 6, 7, 8
    PIN1, PIN2, PIN3, PIN4, PIN5, PIN6, PIN7, PIN8, PIN9 = 9, 10, 11, 12, 13, 14, 15, 16, 17
    SOU1, SOU2, SOU3, SOU4, SOU5, SOU6, SOU7, SOU8, SOU9 = 18, 19, 20, 21, 22, 23, 24, 25, 26
    EAST, SOUTH, WEST, NORTH, HAKU, HATSU, CHUN = 27, 28, 29, 30, 31, 32, 33

    MANS = [MAN1, MAN2, MAN3, MAN4, MAN5, MAN6, MAN7, MAN8, MAN9]
    PINS = [PIN1, PIN2, PIN3, PIN4, PIN5, PIN6, PIN7, PIN8, PIN9]
    SOUS = [SOU1, SOU2, SOU3, SOU4, SOU5, SOU6, SOU7, SOU8, SOU9]
    WINDS = [EAST, SOUTH, WEST, NORTH]
    DRAGONS = [HAKU, HATSU, CHUN]
    HONORS = WINDS + DRAGONS
    ANY = MANS + PINS + SOUS + HONORS
    TERMINALS = [MAN1, MAN9, PIN1, PIN9, SOU1, SOU9]
    TERMINALS_AND_HONORS = TERMINALS + HONORS
    GREENS = [SOU2, SOU3, SOU4, SOU6, SOU8, HATSU]

    MAKE_STRAIGHTS = MANS[0:7] + PINS[0:7] + SOUS[0:7]
    MAKE_EDGE_OR_SIDE = MANS[0:8] + PINS[0:8] + SOUS[0:8]
    SIMPLES = MANS[1:8] + PINS[1:8] + SOUS[1:8]
    TYPE_DICT = {Type.MANS: MANS, Type.PINS: PINS, Type.SOUS: SOUS, Type.HONORS: HONORS}

    STRING = {MAN1: '1m', MAN2: '2m', MAN3: '3m', MAN4: '4m', MAN5: '5m',
              MAN6: '6m', MAN7: '7m', MAN8: '8m', MAN9: '9m',
              PIN1: '1p', PIN2: '2p', PIN3: '3p', PIN4: '4p', PIN5: '5p',
              PIN6: '6p', PIN7: '7p', PIN8: '8p', PIN9: '9p',
              SOU1: '1s', SOU2: '2s', SOU3: '3s', SOU4: '4s', SOU5: '5s',
              SOU6: '6s', SOU7: '7s', SOU8: '8s', SOU9: '9s',
              EAST: '1z', SOUTH: '2z', WEST: '3z', NORTH: '4z', HAKU: '5z', HATSU: '6z', CHUN: '7z'}


class CallType:
    CHI = 'chi'
    PON = 'pon'
    CONCEALED_KAN = 'cnk'
    BIG_MELDED_KAN = 'bmk'
    SMALL_MELDED_KAN = 'smk'
    BONUS = 'bns'

    CONCEALED = [CONCEALED_KAN, BONUS]
    OPENED = [CHI, PON, BIG_MELDED_KAN, SMALL_MELDED_KAN]
    ANY = OPENED + CONCEALED
    KANS = [CONCEALED_KAN, BIG_MELDED_KAN, SMALL_MELDED_KAN]


class HandType:
    INVALID = 0
    BEFORE_DRAW = 1
    AFTER_DRAW = 2


class PartType:
    HEAD = 0
    STRAIGHT = 1
    OPENED_TRIPLE = 2
    CONCEALED_TRIPLE = 3
    OPENED_QUAD = 4
    CONCEALED_QUAD = 5
    THIRTEEN_ORPHANS = 6


CALL_TYPE_TO_PART_TYPE = {CallType.CHI: PartType.STRAIGHT,
                          CallType.PON: PartType.OPENED_TRIPLE,
                          CallType.SMALL_MELDED_KAN: PartType.OPENED_QUAD,
                          CallType.BIG_MELDED_KAN: PartType.OPENED_QUAD,
                          CallType.CONCEALED_KAN: PartType.CONCEALED_QUAD,
                          }


class FuReason:
    SEVEN_PAIRS = (25, '치또이츠')
    BASE = (20, '부저')
    HEAD_WAIT = (2, '단기 대기')
    CLOSED_WAIT = (2, '간짱 대기')
    EDGE_WAIT = (2, '변짱 대기')
    CONCEALED_RON = (10, '멘젠 론')
    TSUMO = (2, '쯔모')
    DOUBLE_WIND_PAIR = (4, '연풍패 머리')
    VALUE_PAIR = (2, '역패 머리')

    OPENED_NORMAL_TRIPLE = (2, '중장패 밍커')
    OPENED_OUTSIDE_TRIPLE = (4, '요구패 밍커')
    CONCEALED_NORMAL_TRIPLE = (4, '중장패 안커')
    CONCEALED_OUTSIDE_TRIPLE = (8, '요구패 안커')
    OPENED_NORMAL_QUAD = (8, '중장패 밍깡')
    OPENED_OUTSIDE_QUAD = (16, '요구패 밍깡')
    CONCEALED_NORMAL_QUAD = (16, '중장패 안깡')
    CONCEALED_OUTSIDE_QUAD = (32, '요구패 안깡')
