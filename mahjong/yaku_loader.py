import importlib

from mahjong.rule import Rule, RuleLoader
from mahjong.util import snake_to_camel


class YakuLoader:
    def __init__(self, rule: Rule = None):
        rule = RuleLoader.load_rule() if rule is None else rule
        self.yakus = []
        for yaku_name, yaku_info in rule.yaku_list.items():
            module = importlib.import_module('mahjong.yaku_checker.'+yaku_name)
            CheckerClass = getattr(module, snake_to_camel(yaku_name))
            self.yakus.append(CheckerClass(rule))

    @property
    def yaku_list(self):
        return [checker for checker in self.yakus if not checker.is_yakuman]

    @property
    def yakuman_list(self):
        return [checker for checker in self.yakus if checker.is_yakuman]
