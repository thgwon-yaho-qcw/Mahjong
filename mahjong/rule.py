import os
from dataclasses import dataclass
from dacite import from_dict
import json

from mahjong.util import PROJECT_ROOT_PATH


@dataclass
class YakuInfo:
    han_opened: int
    han_concealed: int
    is_yakuman: bool
    upper_yaku: list[str]


@dataclass
class Rule:
    has_opened_tanyao: bool
    yaku_list: dict[str, YakuInfo]


class RuleLoader:
    @staticmethod
    def load_rule(config_path=None):
        if config_path is None:
            config_path = os.path.join(PROJECT_ROOT_PATH, 'config', 'riichi_standard.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        return from_dict(data_class=Rule, data=config)
