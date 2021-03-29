class HandInfo:
    def __init__(
            self,
            is_tsumo=False,
            round_wind=None,
            player_wind=None,
            is_ready_hand=False,
            is_double_ready_hand=False,
            is_one_shot=False,
            is_last_tile=False,
            is_last_discard=False,
            is_dead_wall_draw=False,
            is_robbing_a_quad=False
    ):
        self.is_tsumo = is_tsumo
        self.round_wind = round_wind
        self.player_wind = player_wind
        self.is_ready_hand = is_ready_hand
        self.is_double_ready_hand = is_double_ready_hand
        self.is_one_shot = is_one_shot
        self.is_last_tile = is_last_tile
        self.is_last_discard = is_last_discard
        self.is_dead_wall_draw = is_dead_wall_draw
        self.is_robbing_a_quad = is_robbing_a_quad
