# File: D (Python 2.4)

import DistributedSZTreasure

class DistributedTTTreasure(DistributedSZTreasure.DistributedSZTreasure):
    
    def __init__(self, cr):
        DistributedSZTreasure.DistributedSZTreasure.__init__(self, cr)
        self.modelPath = 'phase_4/models/props/icecream'
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.mp3'


