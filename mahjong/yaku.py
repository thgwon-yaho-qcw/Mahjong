from abc import ABC, abstractmethod


class Yaku(ABC):
    yaku_code = None
    han_open = None
    han_closed = None
    is_yakuman = None

    @abstractmethod
    def _is_satisfied(self, division):
        pass
