class HandInfo:
    def __init__(
            self,
            is_tsumo=False,
            round_wind=None,
            player_wind=None,
    ):
        self.is_tsumo = is_tsumo
        self.round_wind = round_wind
        self.player_wind = player_wind
