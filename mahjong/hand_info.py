class HandInfo:
    def __init__(
            self,
            is_tsumo=False,
            round_wind=None,
            player_wind=None,
            is_ready_hand=False,
            is_opened=False
    ):
        self.is_tsumo = is_tsumo
        self.round_wind = round_wind
        self.player_wind = player_wind
        self.is_ready_hand = is_ready_hand
        self.is_opened = is_opened
