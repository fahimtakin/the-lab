from data import asset_mapping



class Player:
    def __init__(self):
        self.assets = asset_mapping.player_assets["death"]
        self.state="idle"


