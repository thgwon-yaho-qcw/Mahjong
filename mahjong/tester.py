from mahjong.agari_hand import AgariHand
from mahjong.constants import Tile
from mahjong.efficiency import calculate_efficiency
from mahjong.hand import Hand
from mahjong.hand_info import HandInfo
from mahjong.point import calculate_hand_point
from mahjong.shanten import calculate_shanten


def calc_efficiency():
    use_chiitoi_and_kokushi = True
    print('조패효율 계산입니다.')
    while True:
        print('특수형도 포함합니다.' if use_chiitoi_and_kokushi else '일반형만 계산합니다.')
        hand_str = input('손패 코드를 입력해주세요 ( 종료 : q, 일반형/특수형 변환 : c ): ')
        if hand_str == 'q':
            break
        elif hand_str == 'c':
            use_chiitoi_and_kokushi = not use_chiitoi_and_kokushi
            continue

        hand = Hand(hand_str)
        shanten = calculate_shanten(hand, use_chiitoi_and_kokushi, use_chiitoi_and_kokushi)

        def print_shanten(num):
            if num == -1:
                print("화료형입니다.")
            elif num == 0:
                print("텐파이입니다.")
            else:
                print("{}샨텐입니다.".format(num))

        print_shanten(shanten)

        def print_efficiency(efficiency):
            for data in efficiency:
                print("타 {} : [{}], {}장".format(
                    Tile.STRING[data[0]],
                    ', '.join(map(lambda x: Tile.STRING[x], data[1])),
                    data[2])
                )
        print_efficiency(calculate_efficiency(hand, use_chiitoi_and_kokushi, use_chiitoi_and_kokushi))


def calc_point():

    print('점수 계산입니다.')
    while True:
        hand_str = input('손패 코드를 입력해주세요 ( 종료 : q ): ')
        if hand_str == 'q':
            break

        agari_tile_str = input('화료 패 코드를 입력하세요: ')
        agari_tile = 0
        for item in Tile.STRING.items():
            if item[1] == agari_tile_str:
                agari_tile = item[0]
                break

        hand = AgariHand(hand_str, agari_tile, is_tsumo_agari=False)
        hand_info = HandInfo()
        print(calculate_hand_point(hand, hand_info))


if __name__ == '__main__':
    while True:
        print('**********************마작 계산기*********************')
        print('무엇을 하시겠습니까?')
        n = int(input('1. 조패효율 계산   2. 점수계산  0. 종료: '))

        if n == 1:
            calc_efficiency()
        elif n == 2:
            calc_point()
        else:
            break
    print("감사합니다")

