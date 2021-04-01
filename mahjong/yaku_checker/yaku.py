from abc import ABC, abstractmethod

from mahjong.rule import Rule, RuleLoader
from mahjong.util import camel_to_snake


class Yaku(ABC):
    def __init__(self, rule: Rule = None):
        self.yaku_name = camel_to_snake(type(self).__name__)
        self.rule = RuleLoader.load_rule() if rule is None else rule

    @abstractmethod
    def is_satisfied(self, division, hand_info):
        pass

    def get_han(self, is_opened):
        if is_opened:
            return self.rule.yaku_list[self.yaku_name].han_opened
        else:
            return self.rule.yaku_list[self.yaku_name].han_concealed

    @property
    def is_yakuman(self):
        return self.rule.yaku_list[self.yaku_name].is_yakuman
