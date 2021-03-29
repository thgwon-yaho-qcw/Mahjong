from abc import ABC, abstractmethod


class Yaku(ABC):
    yaku_code = None
    han_open = None
    han_closed = None
    is_yakuman = None

    @abstractmethod
    def is_satisfied(self, division, hand_info, rule):
        pass

    def get_han(self, is_opened):
        return self.han_open if is_opened else self.han_closed
